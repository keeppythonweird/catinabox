import pytest
import time

from catinabox import catactivities


def test__cat_nap__satisfying_nap(mocker):
    mocker.patch.object(time, "sleep", autospec=True)
    catactivities.cat_nap(400)
    time.sleep.assert_called_with(400)


def test__cat_nap__not_satisfying(mocker):
    mocker.patch.object(time, "sleep", autospec=True)
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(1)
    time.sleep.assert_not_called()
