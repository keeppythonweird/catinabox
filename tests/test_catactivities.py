import pytest
import time

from catinabox import catactivities


def test__cat_nap__satisfying_nap(mocker):
    cat_nap_length = 1000
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    catactivities.cat_nap(cat_nap_length)
    mock_sleep.assert_called_with(cat_nap_length)


def test__cat_nap__not_satisfying(mocker):
    cat_nap_length = 30
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(cat_nap_length)
