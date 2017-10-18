import random
import requests
import time


NAME_GENERATOR_API_ENDPOINT = "http://namey.muffinlabs.com/name.json"
# ignoring leap years for now
SECONDS_IN_YEAR = 365 * 24 * 60 * 60
MAX_YEARS_OLD = 30


class CouldNotGetNameError(Exception):
    def __init__(self, e):
        super(CouldNotGetNameError, self).__init__(
            "Unable to connect to {}: {}".format(
                NAME_GENERATOR_API_ENDPOINT, str(e)
            )
        )


def get_random_cat_name():
    try:
        result = requests.get(NAME_GENERATOR_API_ENDPOINT)
        name = result.json()[0]
        return name
    except requests.exceptions.RequestException as e:
        raise CouldNotGetNameError(e)


def make_cat_birthday():
    current_time = int(time.time())

    birthday = random.randint(
        current_time - (SECONDS_IN_YEAR * MAX_YEARS_OLD),
        current_time)

    birthday_datetime = time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime(birthday))
    return birthday_datetime


def cat_generator():
    while True:
        yield {"name": get_random_cat_name(),
               "birthday": make_cat_birthday()}
