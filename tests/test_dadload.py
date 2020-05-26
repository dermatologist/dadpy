from dadpy import __version__
from dotenv import load_dotenv
load_dotenv()
import os
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def dad_fixture():
    from dadpy.dadload import DadLoad
    return DadLoad

def test_load_sample(dad_fixture, capsys):
    dl = dad_fixture(os.getenv("DAD_PATH"), "dad201617c")
    print(dl.sample.head(5))
    assert dl is not None

def test_load_count(dad_fixture, capsys):
    dl = dad_fixture(os.getenv("DAD_PATH"), "dad201617c")
    print(dl.count)
    assert dl.count > 100