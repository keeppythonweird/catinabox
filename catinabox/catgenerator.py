from numpy import random
import numpy as np
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


def get_name(NAME_GENERATOR_API_ENDPOINT):
    result = requests.get(NAME_GENERATOR_API_ENDPOINT)
    return result.json()[0]


def get_current_time():
    return int(time.time())


def get_birthday(current_time):
    np.random.seed(123)
    birthday = random.randint(
        current_time - (SECONDS_IN_YEAR * MAX_YEARS_OLD),
        current_time)
    return birthday


def to_datetime(birthday):
    birthday_datetime = time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime(birthday))
    return birthday_datetime


def cat_generator():
    while True:
        try:
            name = get_name(NAME_GENERATOR_API_ENDPOINT)
        except requests.exceptions.RequestException as e:
            raise CouldNotGetNameError(e)

        current_time = get_current_time()
        birthday = get_birthday(current_time)
        birthday_datetime = to_datetime(birthday)

        yield {"name": name,
               "birthday": birthday_datetime}
