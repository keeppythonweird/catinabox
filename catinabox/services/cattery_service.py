import copy
from nameko.web.handlers import http
import json
import six

from catinabox import pantry


CAT_SITTING_ON_FENCE = '''
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
NEW_CAT_TEMPLATE = {"food_eaten": []}


def json_decode(raw):
    if six.PY3:
        return json.loads(raw.decode('UTF-8'))
    else:
        return json.loads(raw)


class CatteryService(object):
    name = 'cattery'
    _cats = []
    _pantry = pantry.Pantry()

    @http('GET', '/')
    def index(self, request):
        return 200, CAT_SITTING_ON_FENCE

    ###########################################################################
    # cats
    ###########################################################################

    @http('GET', '/cats')
    def get_cats(self, request):
        return 200, json.dumps(self._cats)

    @http('POST', '/cats')
    def create_cat(self, request):
        cat_to_add = json_decode(request.get_data())
        new_cat = copy.deepcopy(NEW_CAT_TEMPLATE)
        new_cat.update(cat_to_add)
        self._cats.append(new_cat)
        return 201, ""
        # return 201, json.dumps(cat_to_add)

    @http('DELETE', '/cats')
    def delete_cat(self, request):
        cat_to_delete = json_decode(request.get_data())
        cats = [cat for cat in self._cats
                if cat["name"] == cat_to_delete["name"]]
        if len(cats) == 0:
            return 404, json.dumps(cat_to_delete)
        # TODO: there must only be one
        self._cats.remove(cats[0])
        return 204, ""

    ###########################################################################
    # cats/dishes
    ###########################################################################

    @http('POST', '/cats/dishes')
    def feed_the_cats(self, request):
        foods_to_feed = self._pantry.retrieve_food(len(self._cats))

        for cat, food in zip(self._cats, foods_to_feed):
            cat["food_eaten"].append(food)

        return 204, ""

    ###########################################################################
    # pantry
    ###########################################################################

    @http('GET', '/pantry')
    def get_pantry(self, request):
        return 200, json.dumps(self._pantry.list_food())

    @http('PATCH', '/pantry')
    def add_food_to_pantry(self, request):
        food_to_add = json_decode(request.get_data())

        # TODO: GET THE FOOD FROM THE FOOD TRUCK
        # for now we will get it from nowhere

        for food_type, quantity in food_to_add:
            self._pantry.add_food(food_type=food_type, quantity=quantity)

        return 204, ""
