import pytest
import requests
from catinabox import catgenerator


def test__get_name(mocker):
    with mocker.patch('requests.get', return_value="Chinmay"):
        assert catgenerator.get_name() == "Chinmay"
    pass


def test__get_name_request_error(mocker):
    with mocker.patch('requests.get',
                      side_effect=requests.exceptions.RequestException):
        with pytest.raises(catgenerator.CouldNotGetNameError):
            catgenerator.get_name()
    pass


def test__get_birthday(mocker):
    mocker.patch('time.strftime', return_value="2016-12-23 12:00:00")
    cat_birthday = catgenerator.get_birthday()
    assert cat_birthday == "2016-12-23 12:00:00"
    pass


def test__cat_generator(mocker):
    mocker.patch.object(catgenerator, "get_name", return_value="Chinmay")
    mocker.patch.object(catgenerator, "get_birthday", return_value="birthday")
    cat_generator = catgenerator.cat_generator()
    assert next(cat_generator) == {'name': "Chinmay",
                                   'birthday': "birthday"}
