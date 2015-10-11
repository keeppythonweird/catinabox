from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 7
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 35


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = 0.5
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 0.25


def test__cat_years_to_hooman_years__0__returns_0():
    hooman_age = catmath.cat_years_to_hooman_years(0)
    assert hooman_age == 0