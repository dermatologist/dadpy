import pytest
from dotenv import load_dotenv
load_dotenv()
import os

@pytest.fixture
def dad_fixture():
    from dadpy.dadload import DadLoad
    return DadLoad

@pytest.fixture
def dad_embedding():
    from dadpy.dadembedding import DadEmbedding
    return DadEmbedding

def test_read_morbidity(dad_fixture, dad_embedding, capsys):
    dl = dad_fixture(os.getenv("DAD_PATH"))
    de = dad_embedding(dl.sample)
    print(de.list_embed()) # List of morbidities and interventions
    assert len(de.list_embed()) > 100
