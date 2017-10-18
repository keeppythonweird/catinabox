import pytest
import time

from catinabox import catactivities


def test__cat_nap__satisfying_nap(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    '''try:
        catactivities.cat_nap(mock_sleep)
    except Exception:
        pytest.fail(catactivities.NapWillNotBeSatisfying)
    '''
    catactivities.cat_nap(1000)
    mock_sleep.assert_called_with(1000)
    assert mock_sleep.call_count == 1


def test__cat_nap__not_satisfying(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(1)
    assert mock_sleep.call_count == 0
