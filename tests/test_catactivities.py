import pytest
import time

from catinabox import catactivities


def test__cat_nap__satisfying_nap(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    catactivities.cat_nap(600)
    mock_sleep.assert_called_with(600)


def test__cat_nap__not_satisfying():
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(5)
