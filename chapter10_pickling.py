import pickle

class myc:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
    def __str__(self):
        return '{0}) {1}'.format(self.ID, self.name)

if __name__=='__main__':
    data_in = ["a list",
            "containing",
            5,
            "values including another list",
            ["inner", "list"]]

    #write
    with open("chapter10_pickling.txt", 'wb') as file:
        pickle.dump(data_in, file)

    #read
    with open("chapter10_pickling.txt", 'rb') as file:
        data_out = pickle.load(file)

    print(data_out)
    print('\n')

    #-----------------------------------------
    myc1 = myc(1, 'joe')
    myc2 = myc(2, 'bob')
    
    #write
    with open("chapter10_pickling_myc.txt", 'wb') as file:
        pickle.dump(myc1, file)
        pickle.dump(myc2, file)

    #read
    with open("chapter10_pickling_myc.txt", 'rb') as file:
        #data_myc1 = pickle.load(file)
        #data_myc2 = pickle.load(file)
        try:
          while 1:
            data_myc = pickle.load(file)
            print(data_myc)
        except (EOFError):
            pass
        
            

    #print(data_myc1)
    #print(data_myc2)
