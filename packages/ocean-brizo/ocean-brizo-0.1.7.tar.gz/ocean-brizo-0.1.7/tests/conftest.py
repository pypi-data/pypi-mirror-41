import os

import pytest
from squid_py import Account, ConfigProvider
from squid_py.config import Config
from squid_py.keeper import Keeper
from squid_py.keeper.web3_provider import Web3Provider
from squid_py.ocean.ocean import Ocean

from brizo.run import app

app = app

PUBLISHER_INDEX = 1
CONSUMER_INDEX = 0


@pytest.fixture
def client():
    client = app.test_client()
    yield client


json_brizo = {
    "consumer_wallet": "",
    "algorithm_did": "algo.py",
    "asset_did": "data.txt",
    "docker_image": "python:3.6-alpine",
    "memory": 1.5,
    "cpu": 1
}


@pytest.fixture
def sla_template():
    return


@pytest.fixture
def publisher_ocean_instance():
    return get_publisher_ocean_instance()


@pytest.fixture
def consumer_ocean_instance():
    return get_consumer_ocean_instance()


def init_ocn_tokens(ocn, account, amount=100):
    account.request_tokens(amount)
    ocn.keeper.token.token_approve(
        ocn.keeper.payment_conditions.address,
        amount,
        account
    )


def make_ocean_instance(account_index):
    path_config = 'config_local.ini'
    os.environ['CONFIG_FILE'] = path_config
    ocn = Ocean(Config(path_config))
    account = list(ocn.accounts)[account_index]
    return ocn


def get_publisher_ocean_instance():
    ocn = make_ocean_instance(PUBLISHER_INDEX)
    account = get_publisher_account(ConfigProvider.get_config())
    init_ocn_tokens(ocn, account)
    ocn.main_account = account
    return ocn


def get_consumer_ocean_instance():
    ocn = make_ocean_instance(CONSUMER_INDEX)
    account = get_consumer_account(ConfigProvider.get_config())
    init_ocn_tokens(ocn, account)
    ocn.main_account = account
    return ocn


def get_publisher_account(config):
    return get_account_from_config(config, 'parity.address', 'parity.password')


def get_consumer_account(config):
    return get_account_from_config(config, 'parity.address1', 'parity.password1')


def get_account_from_config(config, config_account_key, config_account_password_key):
    address = None
    if config.has_option('keeper-contracts', config_account_key):
        address = config.get('keeper-contracts', config_account_key)

    if not address:
        return None

    password = None
    address = Web3Provider.get_web3().toChecksumAddress(address) if address else None
    if (address
            and address in Keeper.get_instance().accounts
            and config.has_option('keeper-contracts', config_account_password_key)):
        password = config.get('keeper-contracts', config_account_password_key)

    return Account(address, password)
