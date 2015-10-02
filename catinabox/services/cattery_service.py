import copy
from nameko.web.handlers import http
import json
import six

from catinabox import pantry, cattery


CAT_SITTING_ON_FENCE = r'''
             *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *
          |\___/|
          )     (             .              '
         =\     /=
           )===(       *
          /     \
          |     |
         /       \
         \       /
  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  jgs|  |  |  |  |  |  |  |  |  |  |  |  |  |
'''


def json_decode(raw):
    if six.PY3:
        return json.loads(raw.decode('UTF-8'))
    else:
        return json.loads(raw)


class CatteryService(object):
    name = 'cattery'
    _cats = cattery.Cattery()
    _pantry = pantry.Pantry()

    @http('GET', '/')
    def index(self, request):
        return 200, CAT_SITTING_ON_FENCE

    ###########################################################################
    # cats
    ###########################################################################

    @http('GET', '/cats')
    def get_cats(self, request):
        """Retrieve list of all cats in the cattery.

        :param request: n/a
        :return: A list of dictionaries, each specifying
                 the name of the cat and a list of the foods that have been
                 fed to the cat, e.g.:
                 [
                   {"name": <name of cat>, "food_eaten": [<food item>]
                 ]
        """
        return 200, json.dumps(self._cats.cats)

    @http('POST', '/cats')
    def create_cat(self, request):
        """Add a cat with the specified name.

        :param request: Expected format {"name": <name of cat>}
        :return: No body
        """
        cat_to_add = json_decode(request.get_data())
        self._cats.add_cats([cat_to_add["name"]])
        return 201, ""

    @http('DELETE', '/cats')
    def delete_cat(self, request):
        """Remove the specified cat from the cattery.

        :param request: Expected format {"name": <name of cat>}
        :return: No body
        """
        cat_to_delete = json_decode(request.get_data())
        try:
            self._cats.remove_cat(cat_to_delete["name"])
        except cattery.CatNotFound:
            return 404, json.dumps(cat_to_delete)
        return 204, ""

    ###########################################################################
    # cats/dishes
    ###########################################################################

    @http('POST', '/cats/dishes')
    def feed_the_cats(self, request):
        """Feed all cats from the pantry.

        :param request: n/a
        :return: No body
        """

        # TODO: should raise an exception if there isn't enough food

        foods_to_feed = self._pantry.retrieve_food(self._cats.num_cats)
        self._cats.feed_cats(foods_to_feed)
        return 204, ""

    ###########################################################################
    # pantry
    ###########################################################################

    @http('GET', '/pantry')
    def get_pantry(self, request):
        """Return a list of all foods in the pantry.

        These are foods available to be fed to the cats in the cattery.

        :param request: n/a
        :return: A list, where each entry is the name of a food item in the
                 pantry, one entry per consumable item. e.g.:
                 ["burger", "pickle", "cheezburger", "cheezburger"]
        """
        return 200, json.dumps(self._pantry.list_food())

    @http('PATCH', '/pantry')
    def add_food_to_pantry(self, request):
        """Retrieve food from food truck and add to the pantry.

        :param request: Food to add to the pantry. A list of tuples, specifying
                        the type of food and the count to add to the pantry,
                        e.g.:
                        [
                          ("cheezburger", 5),
                          ("pickle", 7)
                        ]
        :return: No body
        """
        food_to_add = json_decode(request.get_data())

        # TODO: GET THE FOOD FROM THE FOOD TRUCK
        # for now we will get it from nowhere

        for food_type, quantity in food_to_add:
            self._pantry.add_food(food_type=food_type, quantity=quantity)

        return 204, ""
