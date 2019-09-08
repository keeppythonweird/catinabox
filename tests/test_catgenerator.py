import pytest
import mock
import time
from catinabox import catgenerator


@pytest.mark.parametrize('url, expected', [("http://namey.muffinlabs.com/name.json", "Jessica")])
def test_get_name(url, expected):
    return catgenerator.get_name(url) == expected


def test_get_time(mock):
    mock_time = mock.patch.object(time, "time", autospec=True)
    mock_time.return_value = 7
    assert catgenerator.get_current_time() == 7


@pytest.mark.parametrize('current_time, birthday', [(7, -102251259)])
def test_get_birthday(mock, current_time, birthday):
    mock_time = mock.patch.object(time, "time", autospec=True)
    mock_time.return_value = current_time
    assert catgenerator.get_birthday(current_time) == birthday


@pytest.mark.parametrize('birthday, datetime', [(-102251259, '1966-10-05 08:52:21')])
def test_to_datetime(birthday, datetime):
    assert catgenerator.to_datetime(birthday) == datetime


# def test_get_generator():
#     pass
