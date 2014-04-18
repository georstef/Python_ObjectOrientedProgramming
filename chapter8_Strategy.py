import random

class FirstStrategy:
    def get_value(self, l):
        return l[0]

class LastStrategy:
    def get_value(self, l):
        return l[-1]

class RandomStrategy:
    def get_value(self, l):
        return l[random.randrange(len(l))]

if __name__ == '__main__':
    myl = ['first',2,3,4,5,6,7,8,'last']
    ans = input('give number (1, 2, 3):')
    if ans == '1':
        myc = FirstStrategy()
    elif ans == '2':
        myc = LastStrategy()
    else:
        myc = RandomStrategy()

    print(type(myc))

    #strategy pattern is like duck typing
    #myc doesn't know which class is but it has a get_value() method
    print(myc.get_value(myl)); 
