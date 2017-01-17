import pytest
import requests

from catinabox import catgenerator


# Write tests for the refactored `catinabox.catgenerator`


def test__get_name(mocker):
    mocker.patch('requests.get', autospec=True). \
        return_value.json.return_value = ['Bob']
    cat_name = catgenerator.get_name()
    assert cat_name == 'Bob'


def test__get_name_raises(mocker):
    mocker.patch('requests.get', side_effect=requests.exceptions.Timeout,
                 autospec=True)
    with pytest.raises(catgenerator.CouldNotGetNameError):
        catgenerator.get_name()


def test__get_birthday_datetime(mocker):
    mocker.patch('time.time', autospec=True).return_value = \
        catgenerator.SECONDS_IN_YEAR * 20
    mocker.patch('random.randint', autospec=True).return_value = \
        catgenerator.SECONDS_IN_YEAR * 1
    assert catgenerator.get_birthday_datetime() == '1971-01-01 00:00:00'


def test__cat_generator(mocker):
    mocker.patch.object(catgenerator, 'get_name',
                        autospec=True).return_value = 'Alice'
    mocker.patch.object(catgenerator, 'get_birthday_datetime',
                        autospec=True).return_value = '1979-12-30 01:00:00'
    cat = catgenerator.cat_generator()
    assert next(cat) == {"name": 'Alice', "birthday": '1979-12-30 01:00:00'}
    assert next(cat) == {"name": 'Alice', "birthday": '1979-12-30 01:00:00'}
