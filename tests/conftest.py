import logging

import pytest


@pytest.fixture(autouse=True, scope='session')
def setup_logging():
    logging.getLogger().setLevel(logging.DEBUG)
