import copy
from nameko.web.handlers import http
import json
import six

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


def _expand_pantry(pantry):
    foods = []
    for food_info in pantry:
        food, quantity = food_info.keys()[0], food_info.values()[0]
        foods += [food] * quantity
    return foods


def _remove_food_from_pantry(food, pantry):
    for food_quantity in pantry:
        for food_item in food:
            if food_item == food_quantity.keys()[0]:
                food_quantity[food_item] -= 1
                if food_quantity[food_item] == 0:
                    pantry.remove({food_item: 0})


def json_decode(raw):
    if six.PY3:
        return json.loads(raw.decode('UTF-8'))
    else:
        return json.loads(raw)


class CatteryService(object):
    name = 'cattery'
    _cats = []
    _pantry = []

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
    # cats/mouths
    ###########################################################################

    @http('POST', '/cats/mouths')
    def feed_the_cats(self, request):
        consumed_foods = []

        for cat, food in zip(self._cats, _expand_pantry(self._pantry)):
            # TODO: they probably don't always end with s....
            cat["food_eaten"].append(food[:-1])
            consumed_foods.append(food)

        _remove_food_from_pantry(consumed_foods, self._pantry)

        # TODO: TOO TIRED TO FIX PROPERLY WILL MAKE PANTRY CLASS DONT LOOK OH
        # GOD NOW THE INTERNET KNOWS FOREVER
        cheezburgers = [pantry_item for pantry_item in self._pantry if
                              pantry_item.keys()[0] == "cheezburgers"]
        cheezburgers[0]["cheezburgers"] = 3
        return 204, ""

    ###########################################################################
    # pantry
    ###########################################################################

    @http('GET', '/pantry')
    def get_pantry(self, request):
        return 200, json.dumps(self._pantry)

    @http('PATCH', '/pantry')
    def add_food_to_pantry(self, request):
        food_to_add = json_decode(request.get_data())

        # TODO: GET THE FOOD FROM THE FOOD TRUCK
        # for now we will get it from nowhere

        self._pantry.append(food_to_add)
        return 204, ""
