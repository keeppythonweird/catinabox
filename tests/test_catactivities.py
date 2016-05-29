import pytest
import time

from catinabox import catactivities


def test__cat_nap__satisfying_nap(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    mock_sleep.return_value = None
    catactivities.cat_nap(301)
    assert True


def test__cat_nap__not_satisfying(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    mock_sleep.return_value = None
    with(pytest.raises(catactivities.NapWillNotBeSatisfying)):
        catactivities.cat_nap(299)
