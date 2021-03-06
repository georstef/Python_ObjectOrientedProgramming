from threading import Timer
import datetime
from urllib.request import urlopen
import pickle

class UpdatedURL:
    def __init__(self, url):
        self.url = url
        self.contents = ''
        self.last_updated = None
        self.update()

    def update(self):
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self):
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()

    def __getstate__(self):
        # returns all of the objects attributes (that are in __dict__)
        # except the timer which is deleted
        new_state = self.__dict__.copy()
        if 'timer' in new_state:
            del new_state['timer']
        return new_state

    def __setstate__(self, data):
        # when unpickling the timer will not exist
        # so we recreate the __dict__ with the data
        # and call schedule() to recreate the timer
        self.__dict__ = data
        self.schedule()
        
if __name__==('__main__'):
    update_url = UpdatedURL("http://www.google.com")
    #print(update_url.contents)

    #cannot pickle timer so we have created a __getstate__
    #when unpickling the timer will not exist so we have created __setstate__
    p = pickle.dumps(update_url)
    print(p)
