from urllib.request import urlopen

class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving Page...")
            self._content = urlopen(self.url).read()
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
