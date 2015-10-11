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
    catactivities.cat_nap(300)
    sleep.assert_called_with(300)


@mock.patch.object(time, "sleep", autospec=True)
def test__cat_nap__not_satisfying(sleep):
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(15)
    assert sleep.call_count == 0
