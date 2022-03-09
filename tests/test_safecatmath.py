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
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(-8)


def test__cat_years_to_hooman_years__older_than_1000__raises():
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(1200)


def test__cat_years_to_hooman_years__string__raises():
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years('Hello')


def test__cat_years_to_hooman_years__nan__raises():
    hooman_age = float('nan') # nan
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(hooman_age)


def test__cat_years_to_hooman_years__collection_type__raises():
    hooman_age = [4, 5]
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(hooman_age)
