import pytest
import time

from catinabox import catactivities


def test__cat_nap__satisfying_nap(mocker):
    mock_time = mocker.patch.object(time, "sleep", autospec=True)
    catactivities.cat_nap(5*60)
    mock_time.assert_called_once_with(5*60)


def test__cat_nap__not_satisfying(mocker):
    mocker.patch.object(time, "sleep", autospec=True)
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(5)
