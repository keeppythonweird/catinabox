from catinabox import catmath
import random


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = random.randint(1, 20)
    human_age = catmath.cat_years_to_hooman_years(cat_age)
    assert human_age == cat_age*catmath.NUM_HOOMAN_YEARS_IN_CAT_YEAR


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = random.randint(1, 9)/10
    human_age = catmath.cat_years_to_hooman_years(cat_age)
    assert human_age == cat_age*catmath.NUM_HOOMAN_YEARS_IN_CAT_YEAR


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0
