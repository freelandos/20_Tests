import os

import pytest
from dotenv import load_dotenv


@pytest.fixture()
def token():
    load_dotenv()
    return os.getenv('TOKEN')


@pytest.fixture()
def folder_path():
    return 'Test_folder'
