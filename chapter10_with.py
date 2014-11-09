import random
import string

class StringJoiner(list):
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.result = '-'.join(self)
        
if __name__=='__main__':
    with StringJoiner() as j:
        for i in range(10):
            j.append(str(i))
    print(j.result)
