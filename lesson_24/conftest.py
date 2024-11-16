import pytest
import logging
from pathlib import Path

from lesson_24.src.user import User


@pytest.fixture(scope='session')
def log():
    logger = logging.getLogger(__name__)

    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    file_handler = logging.FileHandler(Path('test_search.log'))
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


@pytest.fixture(scope='class')
def authenticate(log):
    auth_info = User(log).get_token('test_user', 'test_pass')

    return auth_info
