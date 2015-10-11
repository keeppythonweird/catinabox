# import pytest

from catinabox import safecatmath
from catinabox.safecatmath import InvalidAge


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
    import pytest
    with pytest.raises(InvalidAge):
        safecatmath.cat_years_to_hooman_years(-1)


def test__cat_years_to_hooman_years__older_than_1000__raises():
    import pytest
    with pytest.raises(InvalidAge):
        safecatmath.cat_years_to_hooman_years(1001)


def test__cat_years_to_hooman_years__string__raises():
    import pytest
    with pytest.raises(InvalidAge):
        safecatmath.cat_years_to_hooman_years("six")
