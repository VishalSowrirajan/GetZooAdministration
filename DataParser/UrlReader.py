import urllib
from urllib.request import urlopen


class UrlReader:
    """This class is responsible for reading the file from the given URL"""

    def __init__(self, path):
        self.path = path

    def readFile(self):
        try:
            page = urlopen(self.path)
            file_content = page.read()
            return file_content
        except urllib.error.URLError as e:
            print(e.reason)
