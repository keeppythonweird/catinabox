import requests
import shlex
import subprocess


class HttpBaseClient(object):

    def __init__(self, base_url):
        self._base_url = base_url

    def get(self, *args, **kwargs):
        return requests.get("{base_url}/{url_parts}".format(
            base_url=self._base_url, url_parts="/".join(args)
        ), **kwargs)

    def post(self, *args, **kwargs):
        return requests.post("{base_url}/{url_parts}".format(
            base_url=self._base_url, url_parts="/".join(args)
        ), **kwargs)

    def patch(self, *args, **kwargs):
        return requests.patch("{base_url}/{url_parts}".format(
            base_url=self._base_url, url_parts="/".join(args)
        ), **kwargs)

    def delete(self, *args, **kwargs):
        return requests.delete("{base_url}/{url_parts}".format(
            base_url=self._base_url, url_parts="/".join(args)
        ), **kwargs)


def start_service(service_path):
    cmd = 'nameko run {}'.format(service_path)
    return subprocess.Popen(shlex.split(cmd))
