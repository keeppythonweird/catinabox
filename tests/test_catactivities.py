import pytest
import six
import time

from catinabox import catactivities

if six.PY2:
    import mock
else:
    from unittest import mock


@mock.patch.object(time, "sleep", autospec=True)
def test__cat_nap__satisfying_nap(sleep):
    catactivities.cat_nap(302)
    sleep.assert_called_with(302)


@mock.patch.object(time, "sleep", autospec=True)
def test__cat_nap__not_satisfying(sleep):
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(2)
