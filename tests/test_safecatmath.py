import pytest
from catinabox import safecatmath


@pytest.mark.parametrize(('tc', 'expct'), [
    (7, 35),
    (5, 25),
    (4, 20),
    (10, 50)
])
def test__cat_years_to_hooman_years__middle_age__succeeds(tc, expct):
    assert safecatmath.cat_years_to_hooman_years(tc) == expct


@pytest.mark.parametrize(('tc', 'expct'), [
    (.1, .5),
    (.5, 2.5),
    (.2, 1),
    (.9, 4.5)
])
def test__cat_years_to_hooman_years__less_than_one_year__succeeds(tc, expct):
    assert safecatmath.cat_years_to_hooman_years(tc) == expct


@pytest.mark.parametrize(('tc', 'expct'), [
    (0, 0)
])
def test__cat_years_to_hooman_years__0__returns_0(tc, expct):
    assert safecatmath.cat_years_to_hooman_years(tc) == expct


@pytest.mark.parametrize(('tc', 'expct'), [
    (-10, safecatmath.InvalidAge),
    (-15, safecatmath.InvalidAge),
    (-7, safecatmath.InvalidAge)
])
def test__cat_years_to_hooman_years__less_0__raises(tc, expct):
    with pytest.raises(expct):
        safecatmath.cat_years_to_hooman_years(tc)


@pytest.mark.parametrize(('tc', 'expct'), [
    (2225.2, safecatmath.InvalidAge),
    (50000, safecatmath.InvalidAge),
    (1000.000001, safecatmath.InvalidAge)
])
def test__cat_years_to_hooman_years__older_than_1000__raises(tc, expct):
    with pytest.raises(expct):
        safecatmath.cat_years_to_hooman_years(tc)


@pytest.mark.parametrize(('tc', 'expct'), [
    ("105", safecatmath.InvalidAge),
    ("7", safecatmath.InvalidAge),
    ("5555555", safecatmath.InvalidAge)
])
def test__cat_years_to_hooman_years__string__raises(tc, expct):
    with pytest.raises(expct):
        safecatmath.cat_years_to_hooman_years(tc)


@pytest.mark.parametrize(('tc', 'expct'), [
    (float('nan'), safecatmath.InvalidAge),
])
def test__cat_years_to_hooman_years__nan__raises(tc, expct):
    with pytest.raises(expct):
        safecatmath.cat_years_to_hooman_years(tc)
