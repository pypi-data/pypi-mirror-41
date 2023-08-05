import pytest
from web3 import HTTPProvider, Web3

from squid_py.config_provider import ConfigProvider
from squid_py.examples.example_config import ExampleConfig
from tests.resources.helper_functions import (get_consumer_account, get_consumer_ocean_instance,
                                              get_publisher_ocean_instance, get_registered_ddo)
from tests.resources.mocks.secret_store_mock import SecretStoreClientMock
from tests.resources.tiers import should_run_test

if should_run_test('e2e'):
    ConfigProvider.set_config(ExampleConfig.get_config())


@pytest.fixture
def secret_store():
    return SecretStoreClientMock


@pytest.fixture
def publisher_ocean_instance():
    return get_publisher_ocean_instance()


@pytest.fixture
def consumer_ocean_instance():
    return get_consumer_ocean_instance()


@pytest.fixture
def registered_ddo():
    config = ExampleConfig.get_config()
    return get_registered_ddo(get_publisher_ocean_instance(), get_consumer_account(config))


@pytest.fixture
def web3_instance():
    config = ExampleConfig.get_config()
    return Web3(HTTPProvider(config.keeper_url))
