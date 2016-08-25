import pytest
import requests

from catinabox import catgenerator


# Write tests for the refactored `catinabox.catgenerator`

def test__get_name(mocker):
    mocker.patch("requests.get").return_value.json.return_value = ["Kitty"]
    cat_name = catgenerator.get_name()
    assert cat_name == "Kitty"


def test__get_name__requests_error__raises(mocker):
    mocker.patch("requests.get", side_effect=requests.exceptions.Timeout)
    with pytest.raises(catgenerator.CouldNotGetNameError):
        catgenerator.get_name()


def test__get_birthday(mocker):
    mocker.patch("time.time", return_value=catgenerator.SECONDS_IN_YEAR * 35)
    randint = mocker.patch("random.randint",
                           return_value=catgenerator.SECONDS_IN_YEAR * 2)
    birthday = catgenerator.get_birthday()
    assert birthday == "1972-01-01 03:00:00"
    randint.assert_called_with(catgenerator.SECONDS_IN_YEAR * 5,
                               catgenerator.SECONDS_IN_YEAR * 35)


def test__cat_generator(mocker):
    mocker.patch.object(catgenerator, "get_name", return_value="Joseph")
    mocker.patch.object(catgenerator, "get_birthday", return_value="birthday")
    cat_generator = catgenerator.cat_generator()

    assert next(cat_generator) == {"name": "Joseph",
                                   "birthday": "birthday"}
    assert next(cat_generator) == {"name": "Joseph",
                                   "birthday": "birthday"}
