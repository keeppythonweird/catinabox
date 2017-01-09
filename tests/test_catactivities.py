import pytest
import time

from catinabox import catactivities


def test__cat_nap__satisfying_nap(mocker):
    mocker.patch.object(time, "sleep", autospec=True)
    catactivities.cat_nap(400)


def test__cat_nap__not_satisfying(mocker):
    mocker.patch.object(time, "sleep", autospec=True)
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(200)
