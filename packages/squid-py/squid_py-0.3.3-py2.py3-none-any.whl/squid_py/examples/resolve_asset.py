import logging

from squid_py import Ocean, ConfigProvider, Metadata
from squid_py.examples.example_config import ExampleConfig
from tests.resources.helper_functions import get_account_from_config

from time import sleep

import os
if 'TEST_NILE' in os.environ and os.environ['TEST_NILE'] == '1': ASYNC_DELAY = 5 # seconds
else: ASYNC_DELAY = 1  # seconds

def resolve_asset():
    ConfigProvider.set_config(ExampleConfig.get_config())
    ocn = Ocean()
    account = get_account_from_config(ocn.config, 'parity.address', 'parity.password')
    # get_registered_access_service_template(ocn, account)
    ddo = ocn.register_asset(
        Metadata.get_example(), account,
    )

    sleep(ASYNC_DELAY)

    logging.info(f'Registered asset: did={ddo.did}, ddo={ddo.as_text()}')
    resolved_ddo = ocn.resolve_asset_did(ddo.did)
    logging.info(f'resolved asset ddo: did={resolved_ddo.did}, ddo={resolved_ddo.as_text()}')


if __name__ == '__main__':
    resolve_asset()
