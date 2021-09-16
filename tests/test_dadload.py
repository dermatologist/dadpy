from pkg_resources import resource_filename
import pytest

@pytest.fixture
def dad_fixture():
    from src.dadpy.dadload import DadLoad
    return DadLoad

def test_load_sample(dad_fixture, capsys):
    dl = dad_fixture(resource_filename('tests.resources', 'dadpy-test.csv'))
    print(dl.sample.head(5))
    assert dl is not None

def test_load_count(dad_fixture, capsys):
    dl = dad_fixture(resource_filename('tests.resources', 'dadpy-test.csv'))
    print(dl.count)
    assert dl.count > 1
