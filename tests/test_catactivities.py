import pytest
import time

from catinabox import catactivities


def test__cat_nap__satisfying_nap(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    mock_sleep = 1000
    try:
        catactivities.cat_nap(mock_sleep)
    except Exception:
        pytest.fail(catactivities.NapWillNotBeSatisfying)


def test__cat_nap__not_satisfying(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    mock_sleep = 1
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(mock_sleep)
