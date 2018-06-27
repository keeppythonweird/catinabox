from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    """ Tests if a middle aged hooman equates to a middle aged cat """

    hooman_age = catmath.cat_years_to_hooman_years(6)
    assert hooman_age == 30


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    """ Checks function using floating point cat and hooman years"""

    hooman_age = catmath.cat_years_to_hooman_years(0.1)
    assert hooman_age == 0.5


def test__cat_years_to_hooman_years__0__returns_0():
    """ Takes 0 as input, returns 0 as output"""
    hooman_age = catmath.cat_years_to_hooman_years(0)
    assert hooman_age == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
