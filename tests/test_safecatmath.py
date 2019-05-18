import pytest

from catinabox import safecatmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    hooman_age = safecatmath.cat_years_to_hooman_years(7)
    assert hooman_age == 35


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    hooman_age = safecatmath.cat_years_to_hooman_years(0.1)
    assert hooman_age == 0.5


def test__cat_years_to_hooman_years__0__returns_0():
    hooman_age = safecatmath.cat_years_to_hooman_years(0)
    assert hooman_age == 0


def test__cat_years_to_hooman_years__less_0__raises():
    hooman_age = -5
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(hooman_age)


def test__cat_years_to_hooman_years__older_than_1000__raises():
    hooman_age = 2000
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(hooman_age)


def test__cat_years_to_hooman_years__string__raises():
    hooman_age = 'this is my age'
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(hooman_age)


def test__cat_years_to_hooman_years__nan__raises():
    hooman_age = float('nan')
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(hooman_age)
