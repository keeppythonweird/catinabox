import json
from nameko.web.handlers import http


class CatteryService(object):
    name = 'cattery'
    _cats = []

    ############################################################################
    # cats
    ############################################################################

    @http('GET', '/cats')
    def get_cats(self, request):
        return 200, json.dumps(self._cats)

    @http('POST', '/cats')
    def create_cat(self, request):
        cat_info = json.loads(request.get_data())
        self._cats.append(cat_info)
        return 200
