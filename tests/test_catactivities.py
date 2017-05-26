import pytest
import time

from catinabox import catactivities


def test__cat_nap__satisfying_nap(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    catactivities.cat_nap(1000)
    mock_sleep.assert_called_with(1000)
    # This method is a convenient way of asserting that calls are made
    # in a particular way


def test__cat_nap__not_satisfying(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(10)
    assert mock_sleep.call_count == 0
    # An integer telling you how many times the mock object has been called
