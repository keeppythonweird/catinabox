from .util import http_jsonify


class FoodTruckService(object):

    name = 'foodtruck'
    _inventory = {}

    @http_jsonify('GET', '/')
    def index(self, request):
        return 200, 'Welcome to the food truck!'
