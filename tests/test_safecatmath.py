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


def test__cat_years_to_hooman_years__less_0__raises():
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(-10)


def test__cat_years_to_hooman_years__older_than_1000__raises():
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(2225.2)


def test__cat_years_to_hooman_years__string__raises():
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years("105")


def test__cat_years_to_hooman_years__nan__raises():
    hooman_age = float('nan')
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(hooman_age)
