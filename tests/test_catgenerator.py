import pytest
import requests

from catinabox import catgenerator


def test__get_name(mocker):
    mocker.patch("requests.get").return_value.json.return_value = ["Francis"]
    cat_name = catgenerator.get_name()
    assert cat_name == "Francis"


def test__get_name__requests_error__raises(mocker):
    mocker.patch("requests.get", side_effect=requests.exceptions.Timeout)
    with pytest.raises(catgenerator.CouldNotGetNameError):
        catgenerator.get_name()


def test__get_birthday(mocker):
    mocker.patch("time.time", return_value=catgenerator.SECONDS_IN_YEAR * 35)
    randint = mocker.patch("random.randint",
                           return_value=catgenerator.SECONDS_IN_YEAR * 2)
    birthday = catgenerator.get_birthday()
    assert birthday == "1972-01-01 00:00:00"
    randint.assert_called_with(catgenerator.SECONDS_IN_YEAR * 5,
                               catgenerator.SECONDS_IN_YEAR * 35)


def test__cat_generator(mocker):
    mocker.patch.object(catgenerator, "get_name", return_value="Moe")
    mocker.patch.object(catgenerator, "get_birthday", return_value="birthday")
    cat_generator = catgenerator.cat_generator()

    assert next(cat_generator) == {"name": "Moe",
                                   "birthday": "birthday"}
    assert next(cat_generator) == {"name": "Moe",
                                   "birthday": "birthday"}
