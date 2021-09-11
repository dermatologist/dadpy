from pkg_resources import resource_filename
import pytest
import os

@pytest.fixture
def dad_fixture():
    from dadpy.dadload import DadLoad
    return DadLoad

@pytest.fixture
def dad_embedding():
    from dadpy.dadembedding import DadEmbedding
    yield DadEmbedding
    os.remove('/tmp/dadembed_gensim.bin')

# def test_make_list(dad_fixture, dad_embedding, capsys):
#     dl = dad_fixture(resource_filename('src.dadpy.resources', 'dadpy-test.csv'))
#     de = dad_embedding(dl.sample)
#     print(de.list_embed()) # List of morbidities and interventions
#     assert len(de.list_embed()) > 100

def test_embedding(dad_fixture, dad_embedding, capsys):
    dl = dad_fixture(resource_filename('src.dadpy.resources', 'dadpy-test.csv'))
    de = dad_embedding(dl.sample)
    print(de.embedding().wv.most_similar_cosmul(['ZZZZ'])) #
    assert len(de.embedding().wv.most_similar_cosmul(['ZZZZ'])) > 0
    # assert len(de.list_embed()) > 100
