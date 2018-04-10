import pytest
import time

# why not necessary: ?
# from pytest_mock import mocker

from catinabox import catactivities


def test__cat_nap__satisfying_nap(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    # how to test: test for called_with value:
    # mock_sleep.return_value = 20
    # assert mock_sleep.called_with(20*60)
    # assert mock_sleep.call_args(20*60)
    catactivities.cat_nap(20*60)
    mock_sleep.assert_called_with(20*60)


def test__cat_nap__not_satisfying(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    # mock_sleep.called_with(4*60)
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(4*60)  # too short!
    assert mock_sleep.call_count == 0
