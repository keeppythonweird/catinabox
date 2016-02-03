from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 8
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == cat_age * catmath.NUM_HOOMAN_YEARS_IN_CAT_YEAR


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = 0.1
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == cat_age * catmath.NUM_HOOMAN_YEARS_IN_CAT_YEAR


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0
