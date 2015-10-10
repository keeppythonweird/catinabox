MAX_CAT_AGE = 1000
NUM_HOOMAN_YEARS_IN_CAT_YEAR = 5


class InvalidAge(Exception):
    """The specified cat age is not an expected value."""
    def __init__(self, cat_age):
        super(InvalidAge, self).__init__(
            "Cat age {!r} was provided, but cat age should be an int between "
            "0 and {!r} inclusive.".format(cat_age, MAX_CAT_AGE)
        )
        self.cat_age = cat_age


def cat_years_to_hooman_years(age_in_cat_years):
    """Converts the cat's age to the equivalent in hooman years.

    If the input is not an int or a float, or the age is not considered
    valid, an exception will be raised.

    :param age_in_cat_years: A float: cat's age in years
    :return: The age of the cat relative to a human, assuming 100 years is
             a long human lifespan.
    """
    if (not (isinstance(age_in_cat_years, int) or
             isinstance(age_in_cat_years, float))):
        raise InvalidAge(age_in_cat_years)

    if (age_in_cat_years < 0 or age_in_cat_years > MAX_CAT_AGE):
        raise InvalidAge(age_in_cat_years)

    return age_in_cat_years * NUM_HOOMAN_YEARS_IN_CAT_YEAR
