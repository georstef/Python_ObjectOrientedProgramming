#core class
class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None

    #attach the observer(s)
    def attach(self, observer):
        self.observers.append(observer)
        
    @property
    def product(self):
        return self._product
    
    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()

    #tell all the observers that something happened
    def _update_observers(self):
        for observer in self.observers:
            observer() # is like => observer.__call__()

#one observer
class ConsoleWriteObserver:
    def __init__(self, inventory):
        self.inventory = inventory
        
    def __call__(self):
        print('Unpure:', self.inventory.product)
        
#another observer
class ConsoleWritePureObserver:
    def __init__(self, inventory):
        self.inventory = inventory
        
    def __call__(self):
        print('Pure:', self.inventory.product)

if __name__=='__main__':
    i = Inventory()

    c1 = ConsoleWriteObserver(i)
    i.attach(c1)

    c2 = ConsoleWritePureObserver(i)
    i.attach(c2)

    c3 = ConsoleWriteObserver(i)
    i.attach(c3)

    i.product = 'T-Shirt'
