from catinabox import catmath
cth = catmath.NUM_HOOMAN_YEARS_IN_CAT_YEAR


def test__cat_years_to_hooman_years__middle_age__succeeds():
    for i in range(7, 10):
        assert catmath.cat_years_to_hooman_years(i) == i * cth


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.5) == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
