import pytest
import time

from catinabox import catgenerator
import requests


# Write tests for the refactored `catinabox.catgenerator`

def test__generate_name_success():
    assert catgenerator.generate_name() != ''


def test__generate_name__raises(mocker):
    mocker.patch.object(requests, 'get', autospec=True,
                        side_effect=requests.exceptions.RequestException)
    with pytest.raises(catgenerator.CouldNotGetNameError):
        catgenerator.generate_name()


def test__generate_birthday(mocker):
    current_time = time.time()
    mocker.patch.object(time, 'time', autospec=True, return_value=current_time)

    lower_bound = int(current_time) - \
        (catgenerator.SECONDS_IN_YEAR * catgenerator.MAX_YEARS_OLD)
    upper_bound = int(current_time)

    birthday = catgenerator.generate_birthday()

    assert birthday >= lower_bound and birthday <= upper_bound


def test__cat_generator(mocker):
    name = 'Snowball'
    birthday = 1475358387

    mocker.patch.object(catgenerator, 'generate_name', autospec=True,
                        return_value=name)
    mocker.patch.object(catgenerator, 'generate_birthday', autospec=True,
                        return_value=birthday)

    birthday_datetime = time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime(birthday))

    correct_cat = {"name": name, "birthday": birthday_datetime}

    cat = next(catgenerator.cat_generator())

    assert cat == correct_cat
