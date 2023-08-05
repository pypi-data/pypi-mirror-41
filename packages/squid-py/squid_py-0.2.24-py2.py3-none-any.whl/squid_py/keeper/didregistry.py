"""Keeper module to call keeper-contracts."""

from urllib.parse import urlparse

from web3 import Web3

from squid_py.did import did_to_id_bytes
from squid_py.did_resolver.resolver_value_type import ResolverValueType
from squid_py.keeper.contract_base import ContractBase


class DIDRegistry(ContractBase):
    """Class to register and update Ocean DID's."""

    @staticmethod
    def get_instance():
        """Returns a ContractBase instance of the DIDRegistry contract."""
        return DIDRegistry('DIDRegistry')

    def register(self, did_source, url=None, key=None, account=None):
        """
        Register or update a DID on the block chain using the DIDRegistry smart contract.

        :param did_source: DID to register/update, can be a 32 byte or hexstring
        :param url: URL of the resolved DID
        :param key: Optional 32 byte key ( 64 char hex )
        :param account: instance of Account to use to register/update the DID
        :return: Receipt
        """

        value_type = ResolverValueType.URL
        value = None

        did_source_id = did_to_id_bytes(did_source)

        if not did_source_id:
            raise ValueError(f'{did_source} must be a valid DID to register')

        if url:
            value = url
            if not urlparse(url):
                raise ValueError(f'Invalid URL {url} to register for DID {did_source}')

        if isinstance(key, str):
            key = Web3.sha3(text=key)

        if key is None:
            key = Web3.toBytes(0)

        if not isinstance(key, bytes):
            raise ValueError(f'Invalid key value {key}, must be bytes or string')

        if account is None:
            raise ValueError('You must provide an account to use to register a DID')

        account.unlock()
        transaction = self.register_attribute(did_source_id, value_type, key, value,
                                              account.address)
        receipt = self.get_tx_receipt(transaction)
        return receipt

    def register_attribute(self, did_hash, value_type, key, value, account_address):
        """Register an DID attribute as an event on the block chain.

            did_hash: 32 byte string/hex of the DID
            value_type: 0 = DID, 1 = DIDREf, 2 = URL, 3 = DDO
            key: 32 byte string/hex free format
            value: string can be anything, probably DDO or URL
            account_address: owner of this DID registration record
        """
        return self.contract_concise.registerAttribute(
            did_hash,
            value_type,
            key,
            value,
            transact={'from': account_address}
        )

    def get_update_at(self, did):
        """Return the block number the last did was updated on the block chain."""
        return self.contract_concise.getUpdateAt(did)

    def get_owner(self, did):
        """
        Return the owner of the did.

        :param did: Asset did, did
        :return:
        """
        return self.contract_concise.getOwner(did)
