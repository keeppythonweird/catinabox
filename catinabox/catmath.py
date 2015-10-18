NUM_HOOMAN_YEARS_IN_CAT_YEAR = 5


def cat_years_to_hooman_years(age_in_cat_years):
    """Converts the cat's age to the equivalent in hooman years.

    :param age_in_cat_years: A float: cat's age in years
    :return: The age of the cat relative to a human, assuming 100 years is
             a long human lifespan.
    """
    return age_in_cat_years * NUM_HOOMAN_YEARS_IN_CAT_YEAR
