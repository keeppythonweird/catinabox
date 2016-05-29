NUM_HOOMAN_YEARS_IN_CAT_YEAR = 5


def cat_years_to_hooman_years(age_in_cat_years):
    """Converts the cat's age to the equivalent in hooman years.

    :param age_in_cat_years: A float: cat's age in years
    :return: The age of the cat relative to a human, assuming 100 years is
             a long human lifespan.
    """
    return age_in_cat_years * NUM_HOOMAN_YEARS_IN_CAT_YEAR


def is_cat_leap_year(year):
    """Returns True iff. year is a cat leap year.

    Args:
        year (int): a cat year (which is basically the same as a human year)

    Returns:
        bool: True iff. the cat year is a leap cat year.

    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
