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


def json_decode(raw):
    if six.PY3:
        return json.loads(raw.decode('UTF-8'))
    else:
        return json.loads(raw)


class CatteryService(object):
    name = 'cattery'
    _cats = []

    ############################################################################
    # cats
    ############################################################################

    @http('GET', '/')
    def index(self, request):
        return 200, CAT_SITTING_ON_FENCE

    ############################################################################
    # cats
    ############################################################################

    @http('GET', '/cats')
    def get_cats(self, request):
        return 200, json.dumps(self._cats)

    @http('POST', '/cats')
    def create_cat(self, request):
        cat_info = json_decode(request.get_data())
        self._cats.append(cat_info)
        return 200, ''
