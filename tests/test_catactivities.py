import pytest
import time

from catinabox import catactivities


def test__cat_nap__satisfying_nap(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    catactivities.cat_nap(catactivities.LENGTH_OF_SATISFYING_NAP+1)
    mock_sleep.assert_called_with(catactivities.LENGTH_OF_SATISFYING_NAP+1)


def test__cat_nap__not_satisfying(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(catactivities.LENGTH_OF_SATISFYING_NAP-1)
    mock_sleep.assert_not_called()
