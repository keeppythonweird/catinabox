from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 6
    age = catmath.cat_years_to_hooman_years(cat_age)
    assert age == 30


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = 0.4
    age = catmath.cat_years_to_hooman_years(cat_age)
    assert age == 2


def test__cat_years_to_hooman_years__0__returns_0():
    cat_age = 0
    age = catmath.cat_years_to_hooman_years(cat_age)
    assert age == 0
