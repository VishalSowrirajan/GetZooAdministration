import urllib
from urllib.request import urlopen
import requests


class HTTPRequestHandler:
    """This class is responsible for reading the file from the given URL"""

    def __init__(self, path):
        self.path = path

    def response(self):
        try:
            page = urlopen(self.path)
            file_content = page.read()
            return file_content
        except urllib.error.URLError as e:
            print(e.reason)


class HTTPPostHandler:
    """This class is responsible for posting the result to the server"""
    def __init__(self, data, url):
        self.data = data
        self.url = url

    def post_data_to_URL(self):
        try:
            post_request = requests.post(self.url, data={'result': self.data})
            return 'The status code for the post request is: {}'.format(post_request.status_code)
        except Exception as e:
            print(e)