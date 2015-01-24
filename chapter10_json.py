import json

class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    #can be a method but this is cooler
    @property 
    def full_name(self):
        return self.first + ' ' + self.last

#for encoding json
class ContactEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Contact):
            return {'is_contact': True,
                    'first': obj.first,
                    'last': obj.last,
                    'full': obj.full_name}
        #if the obj is not a Contact just call the parent
        return super().default(obj) # raises type error
        

#for decoding json    
def decode_contact(dic):
    if dic.get('is_contact'): # dic['is_contact'] if 'is_contact' in dic else None
        return Contact(dic['first'], dic['last'])
    else:
        return dic        

class ContactFake: # just for testing the errors raised in ContactEncoder
    pass


if __name__=="__main__":
  c = Contact('george' ,'s.')
  #can be done this way
  j = json.dumps(c.__dict__)
  print(j)

  #can be done with a custom encoder 
  j = json.dumps(c, cls=ContactEncoder)
  print(j)

  #decode (send the data and a function)
  f = json.loads(j, object_hook=decode_contact)
  print(f.full_name)

'''
    #1st easy example
    with open('chapter10_json.txt', 'w') as file:
        json.dump('text - line 1', file)
        #json.dump('line 2', file)
    

    with open('chapter10_json.txt', 'r') as file:
        try:
            data = json.load(file)
            print(data)
        except (EOFError):
            pass
'''
