"""DID Lib to do DID's and DDO's."""
import datetime
import json
import logging
import re
from base64 import b64decode, b64encode

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from web3 import Web3

from squid_py.ddo.public_key_hex import PublicKeyHex
from squid_py.did import did_to_id
from squid_py.service_agreement.service_types import ServiceTypes
from .authentication import Authentication
from .constants import DID_DDO_CONTEXT_URL, KEY_PAIR_MODULUS_BIT
from .public_key_base import PUBLIC_KEY_STORE_TYPE_PEM, PublicKeyBase
from .public_key_rsa import AUTHENTICATION_TYPE_RSA, PUBLIC_KEY_TYPE_RSA, PublicKeyRSA
from .service import Service

logger = logging.getLogger('ddo')


class DDO:
    """DDO class to create, import, export, validate DDO objects."""

    def __init__(self, did='', json_text=None, json_filename=None, created=None, dictionary=None):
        """Clear the DDO data values."""
        self._did = did
        self._public_keys = []
        self._authentications = []
        self._services = []
        self._proof = None
        self._created = None

        if created:
            self._created = created
        else:
            self._created = DDO.get_timestamp()

        if not json_text and json_filename:
            with open(json_filename, 'r') as file_handle:
                json_text = file_handle.read()

        if json_text:
            self._read_dict(json.loads(json_text))
        elif dictionary:
            self._read_dict(dictionary)

    def add_public_key(self, public_key):
        """
        Add a public key object to the list of public keys.

        :param public_key: Public key, PublicKeyHex
        :return: None
        """
        logger.debug(f'Adding public key {public_key}')
        self._public_keys.append(public_key)

    def add_authentication(self, key_id, authentication_type=None):
        """
        Add a authentication public key id and type to the list of authentications.

        :param key_id: Key id, Authentication
        :param authentication_type: Authentication type, str
        :return: None
        """
        if isinstance(key_id, Authentication):
            # adding an authentication object
            authentication = key_id
        elif isinstance(key_id, PublicKeyBase):
            public_key = key_id
            # this is going to be a embedded public key
            authentication = Authentication(public_key, public_key.get_authentication_type())
        else:
            # with key_id as a string, we also need to provide the authentication type
            if authentication_type is None:
                raise ValueError
            authentication = Authentication(key_id, authentication_type)

        logger.debug(f'Adding authentication {authentication}')
        self._authentications.append(authentication)

    def add_signature(self, public_key_store_type=PUBLIC_KEY_STORE_TYPE_PEM, is_embedded=False):
        """
        Add signature.

        Add a signature with a public key and authentication entry for validating this DDO
        returns the private key as part of the private/public key pair.

        :param public_key_store_type: Public key store type, str
        :param is_embedded: bool
        :return Private key pem, str
        """

        key_pair = RSA.generate(KEY_PAIR_MODULUS_BIT, e=65537)
        public_key_raw = key_pair.publickey()
        private_key_pem = key_pair.exportKey("PEM")

        # find the current public key count
        next_index = self.get_public_key_count() + 1
        key_id = f'{self._did}#keys={next_index}'

        public_key = PublicKeyRSA(key_id, owner=key_id)

        public_key.set_encode_key_value(public_key_raw, public_key_store_type)

        if is_embedded:
            # also add the authentication key as embedded key with the authentication
            self.add_authentication(public_key)
        else:
            # add the public key to the DDO list of public keys
            self.add_public_key(public_key)

            # add the public key id and type for this key to the authentication
            self.add_authentication(public_key.get_id(), public_key.get_authentication_type())

        logger.debug('Adding signature to the ddo object.')
        return private_key_pem

    def add_service(self, service_type, service_endpoint=None, values=None):
        """
        Add a service to the list of services on the DDO.

        :param service_type: Service
        :param service_endpoint: Service endpoint, str
        :param values: Python dict with serviceDefinitionId, templateId, serviceAgreementContract,
        list of conditions and purchase endpoint.
        :return:
        """
        if isinstance(service_type, Service):
            service = service_type
        else:
            service = Service(service_endpoint, service_type, values)
        logger.debug(f'Adding service with service type {service_type} with did {self._did}')
        self._services.append(service)

    def as_text(self, is_proof=True, is_pretty=False):
        """return the DDO as a JSON text
        if is_proof == False then do not include the 'proof' element"""
        data = self.as_dictionary(is_proof)
        if is_pretty:
            return json.dumps(data, indent=2, separators=(',', ': '))

        return json.dumps(data)

    def as_dictionary(self, is_proof=True):
        if self._created is None:
            self._created = DDO.get_timestamp()

        data = {
            '@context': DID_DDO_CONTEXT_URL,
            'id': self._did,
            'created': self._created,
        }
        if self._public_keys:
            values = []
            for public_key in self._public_keys:
                values.append(public_key.as_dictionary())
            data['publicKey'] = values
        if self._authentications:
            values = []
            for authentication in self._authentications:
                values.append(authentication.as_dictionary())
            data['authentication'] = values
        if self._services:
            values = []
            for service in self._services:
                values.append(service.as_dictionary())
            data['service'] = values
        if self._proof and is_proof:
            data['proof'] = self._proof

        return data

    def _read_dict(self, dictionary):
        """Import a JSON dict into this DDO."""
        values = dictionary
        self._did = values['id']
        self._created = values.get('created', None)
        if 'publicKey' in values:
            self._public_keys = []
            for value in values['publicKey']:
                if isinstance(value, str):
                    value = json.loads(value)
                self._public_keys.append(DDO.create_public_key_from_json(value))
        if 'authentication' in values:
            self._authentications = []
            for value in values['authentication']:
                if isinstance(value, str):
                    value = json.loads(value)
                self._authentications.append(DDO.create_authentication_from_json(value))
        if 'service' in values:
            self._services = []
            for value in values['service']:
                if isinstance(value, str):
                    value = json.loads(value)
                self.services.append(DDO.create_service_from_json(value))
        if 'proof' in values:
            self._proof = values['proof']

    def add_proof(self, authorisation_index, private_key=None, signature_text=None):
        """Add a proof to the DDO, based on the public_key id/index and signed with the private key
        add a static proof to the DDO, based on one of the public keys."""

        # find the key using an index, or key name
        if isinstance(authorisation_index, dict):
            self._proof = authorisation_index
            return

        if private_key is None:
            raise ValueError

        authentication = self._authentications[authorisation_index]
        if not authentication:
            raise IndexError
        if authentication.is_public_key():
            sign_key = authentication.get_public_key()
        else:
            sign_key = self.get_public_key(authentication.get_public_key_id())

        if sign_key is None:
            raise IndexError

        # get the signature text if not provided

        if signature_text is None:
            hash_text_list = self.hash_text_list()
            signature_text = "".join(hash_text_list)

        # just incase clear out the current static proof property
        self._proof = None

        signature = DDO.sign_text(signature_text, private_key, sign_key.get_type())

        self._proof = {
            'type': sign_key.get_type(),
            'created': DDO.get_timestamp(),
            'creator': sign_key.get_id(),
            'signatureValue': b64encode(signature).decode('utf-8'),
        }

    def validate_proof(self, signature_text=None):
        """Validate the static proof created with this DDO, return True if valid
        if no static proof exists then return False."""

        if not signature_text:
            hash_text_list = self.hash_text_list()
            signature_text = "".join(hash_text_list)
        if self._proof is None:
            return False
        if not isinstance(self._proof, dict):
            return False

        if 'creator' in self._proof and 'signatureValue' in self._proof:
            signature = b64decode(self._proof['signatureValue'])
            return self.validate_from_key(self._proof['creator'], signature_text, signature)
        return False

    def is_proof_defined(self):
        """Return true if a static proof exists in this DDO."""
        return not self._proof is None

    def validate_from_key(self, key_id, signature_text, signature_value):
        """Validate a signature based on a given public_key key_id/name."""

        public_key = self.get_public_key(key_id, True)
        if public_key is None:
            return False

        key_value = public_key.get_decode_value()
        if key_value is None:
            return False

        authentication = self.get_authentication_from_public_key_id(public_key.get_id())
        if authentication is None:
            return False

        # if public_key.get_store_type() != PUBLIC_KEY_STORE_TYPE_PEM:
        # key_value = key_value.decode()

        return DDO.validate_signature(signature_text, key_value, signature_value,
                                      authentication.get_type())

    def get_public_key(self, key_id, is_search_embedded=False):
        """Key_id can be a string, or int. If int then the index in the list of keys."""
        if isinstance(key_id, int):
            return self._public_keys[key_id]

        for item in self._public_keys:
            if item.get_id() == key_id:
                return item

        if is_search_embedded:
            for authentication in self._authentications:
                if authentication.get_public_key_id() == key_id:
                    return authentication.get_public_key()
        return None

    def get_public_key_count(self):
        """Return the count of public keys in the list and embedded."""
        index = len(self._public_keys)
        for authentication in self._authentications:
            if authentication.is_public_key():
                index += 1
        return index

    def get_authentication_from_public_key_id(self, key_id):
        """Return the authentication based on it's id."""
        for authentication in self._authentications:
            if authentication.is_key_id(key_id):
                return authentication
        return None

    def get_service(self, service_type=None):
        """Return a service using."""
        for service in self._services:
            if service.get_type() == service_type and service_type:
                return service
        return None

    def get_metadata(self):
        metadata_service = self.find_service_by_type(ServiceTypes.METADATA)
        return metadata_service.get_values()['metadata']

    def find_service_by_id(self, service_id):
        service_id_key = 'serviceDefinitionId'
        for s in self._services:
            if service_id_key in s.get_values() and s.get_values()[service_id_key] == service_id:
                return s

        return None

    def find_service_by_type(self, service_type):
        for s in self._services:
            if service_type == s.type:
                return s

        return None

    def validate(self):
        """Validate the ddo data structure."""
        if self._public_keys and self._authentications:
            for authentication in self._authentications:
                if not authentication.is_valid():
                    return False
                if authentication.is_public_key():
                    public_key = authentication.get_public_key()
                else:
                    key_id = authentication.get_public_key_id()
                    public_key = self.get_public_key(key_id)
                if not public_key.is_valid():
                    return False
        if self._services:
            for service in self._services:
                if not service.is_valid():
                    return False

        # validate if proof defined in this DDO
        if self.is_proof_defined:
            if not self.validate_proof:
                return False
        return True

    def hash_text_list(self):
        """Return a list of all of the hash text."""
        hash_text = []
        if self._created:
            hash_text.append(self._created)

        if self._public_keys:
            for public_key in self._public_keys:
                if public_key.get_type():
                    hash_text.append(public_key.get_type())
                if public_key.get_value():
                    hash_text.append(public_key.get_value())

        if self._authentications:
            for authentication in self._authentications:
                if authentication.is_public_key():
                    public_key = authentication.get_public_key()
                    if public_key.get_type():
                        hash_text.append(public_key.get_type())
                    if public_key.get_value():
                        hash_text.append(public_key.get_value())

        if self._services:
            for service in self._services:
                hash_text.append(service.get_type())
                hash_text.append(service.get_endpoint())

        # if no data can be found to hash then raise an error
        if not hash_text:
            raise ValueError
        return hash_text

    def calculate_hash(self):
        """Return a sha3 hash of important bits of the DDO, excluding any DID portion,
        as this hash can be used to generate the DID."""
        hash_text_list = self.hash_text_list()
        return Web3.sha3(text="".join(hash_text_list))

    def is_did_assigend(self):
        """Return true if a DID is assigned to this DDO."""
        return self._did != '' and self._did is not None

    def get_created_time(self):
        """Return the DDO created time, can be None."""
        return self._created

    def create_new(self, did):
        """Method to copy a DDO and assign a new did to all of the keys to an empty/non DID
        assigned DDO.
        we assume that this ddo has been created as empty ( no did )"""

        if self.is_did_assigend():
            raise Exception('Cannot assign a DID to a completed DDO object')
        ddo = DDO(did, created=self._created)
        for public_key in self._public_keys:
            public_key.assign_did(did)
            ddo.add_public_key(public_key)

        for authentication in self._authentications:
            authentication.assign_did(did)
            ddo.add_authentication(authentication)

        for service in self._services:
            ddo.add_service(service)

        if self.is_proof_defined():
            if re.match('^#.*', self._proof['creator']):
                proof = self._proof
                proof['creator'] = did + proof['creator']
            ddo.add_proof(proof)

        return ddo

    @property
    def did(self):
        """ Get the DID."""
        return self._did

    @property
    def asset_id(self):
        """The asset id part of the DID"""
        return did_to_id(self._did)

    @property
    def public_keys(self):
        """Get the list of public keys."""
        return self._public_keys

    @property
    def authentications(self):
        """Get the list authentication records."""
        return self._authentications

    @property
    def services(self):
        """Get the list of services."""
        return self._services

    @property
    def proof(self):
        """Get the static proof, or None."""
        return self._proof

    @property
    def is_valid(self):
        """Return True if this DDO is valid."""
        return self.validate()

    @staticmethod
    def sign_text(text, private_key, sign_type=PUBLIC_KEY_TYPE_RSA):
        """Sign some text using the private key provided."""
        if sign_type == PUBLIC_KEY_TYPE_RSA:
            signer = PKCS1_v1_5.new(RSA.import_key(private_key))
            text_hash = SHA256.new(text.encode('utf-8'))
            signed_text = signer.sign(text_hash)
            return signed_text

        raise NotImplementedError

    @staticmethod
    def validate_signature(text, key, signature, sign_type=AUTHENTICATION_TYPE_RSA):
        """Validate a signature based on some text, public key and signature."""
        result = False
        try:
            if sign_type == AUTHENTICATION_TYPE_RSA:
                rsa_key = RSA.import_key(key)
                verifier = PKCS1_v1_5.new(rsa_key)
                if verifier:
                    text_hash = SHA256.new(text.encode('utf-8'))
                    result = verifier.verify(text_hash, signature)
            else:
                raise NotImplementedError
        except (ValueError, TypeError):
            result = False

        return result

    @staticmethod
    def create_public_key_from_json(values):
        """Create a public key object based on the values from the JSON record."""
        # currently we only support RSA public keys
        _id = values.get('id')
        if not _id:
            # Make it more forgiving for now.
            _id = ''
            # raise ValueError('publicKey definition is missing the "id" value.')

        if values.get('type') == PUBLIC_KEY_TYPE_RSA:
            public_key = PublicKeyRSA(_id, owner=values.get('owner'))
        else:
            public_key = PublicKeyHex(_id, owner=values.get('owner'))

        public_key.set_key_value(values)
        return public_key

    @staticmethod
    def create_authentication_from_json(values):
        """Create authentitaciton object from a JSON string."""
        key_id = values.get('publicKey')
        authentication_type = values.get('type')
        if not key_id:
            raise ValueError(
                f'Invalid authentication definition, "publicKey" is missing: {values}')
        if isinstance(key_id, dict):
            public_key = DDO.create_public_key_from_json(key_id)
            authentication = Authentication(public_key, public_key.get_authentication_type())
        else:
            authentication = Authentication(key_id, authentication_type)

        return authentication

    @staticmethod
    def create_service_from_json(values):
        """Create a service object from a JSON string."""
        if not 'serviceEndpoint' in values:
            logger.error(
                'Service definition in DDO document is missing the "serviceEndpoint" key/value.')
            raise IndexError
        if not 'type' in values:
            logger.error('Service definition in DDO document is missing the "type" key/value.')
            raise IndexError
        service = Service(values['serviceEndpoint'], values['type'], values)
        return service

    @staticmethod
    def get_timestamp():
        """Return the current system timestamp."""
        return str(datetime.datetime.now())
