import urllib
from urllib.request import urlopen
import requests


class HTTPRequestHandler:
    """This class is responsible for reading the data from the given URL"""

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
    """This class is responsible for posting the data to the server"""

    def __init__(self, dict_pair, url):
        self.dict = dict_pair
        self.url = url

    def post_data_to_URL(self):
        try:
            post_request = requests.post(self.url, data=self.dict)
            #print(post_request.content)
            return post_request.status_code
        except Exception as e:
            print(e)
