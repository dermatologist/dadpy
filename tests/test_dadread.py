import pytest
from pkg_resources import resource_filename


@pytest.fixture
def dad_fixture():
    from src.dadpy.dadload import DadLoad
    return DadLoad


@pytest.fixture
def dad_read():
    from src.dadpy.dadread import DadRead
    return DadRead


def test_read_diagnosis(dad_fixture, dad_read, capsys):
    dl = dad_fixture(resource_filename('src.dadpy.resources', 'dadpy-test.csv'))
    dr = dad_read(dl.sample)
    print(dr.has_diagnosis('ZZ'))  # Obesity
    assert dr.count(dr.has_diagnosis('ZZ')) > 1


def test_read_treatment(dad_fixture, dad_read, capsys):
    dl = dad_fixture(resource_filename('src.dadpy.resources', 'dadpy-test.csv'))
    dr = dad_read(dl.sample)
    # Partial gastrectomy for repair of gastric diverticulum
    print(dr.has_treatment('1Z'))
    assert dr.count(dr.has_treatment('1Z')) > 1


def test_read_comorbidity(dad_fixture, dad_read, capsys):
    dl = dad_fixture(resource_filename('src.dadpy.resources', 'dadpy-test.csv'))
    dr = dad_read(dl.sample)
    print(dr.comorbidity('ZZ'))  # Obesity


def test_read_interventions(dad_fixture, dad_read, capsys):
    dl = dad_fixture(resource_filename('src.dadpy.resources', 'dadpy-test.csv'))
    dr = dad_read(dl.sample)
    # Partial gastrectomy for repair of gastric diverticulum
    print(dr.interventions('1Z'))


def test_read_vector(dad_fixture, dad_read, capsys):
    dl = dad_fixture(resource_filename('src.dadpy.resources', 'dadpy-test.csv'))
    dr = dad_read(dl.sample)
    print(dr.vector(dr.has_diagnosis('ZZ'), include_treatments=True))  # Obesity
