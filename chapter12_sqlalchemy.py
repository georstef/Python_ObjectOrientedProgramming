'''
import sqlite3
connection = sqlite3.connect("chapter12_sqlalchemy.db")
connection.execute("CREATE TABLE IF NOT EXISTS pet (type, breed, gender, name)")
connection.execute("INSERT INTO pet VALUES('dog', 'spaniel', 'female', 'Esme')")
connection.execute("INSERT INTO pet VALUES('cat', 'persian', 'male', 'Oscar')")
results = connection.execute("SELECT breed, name from pet where type='dog'")
connection.close()
'''

import sqlalchemy as sqa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() # <-this function returns a class (not an instance)

class Pet(Base): # table
    __tablename__ = 'pet'
    petId = sqa.Column(sqa.Integer, primary_key = True)
    petType = sqa.Column(sqa.String(16))
    petBreed = sqa.Column(sqa.String(32))
    petGender = sqa.Column(sqa.Enum("male", "female"))
    petName = sqa.Column(sqa.String(64))

    def __init__(self, petId, petType, petBreed, petGender, petName):
        self.petId = petId
        self.petType = petType
        self.petBreed = petBreed
        self.petGender = petGender
        self.petName = petName

class Owner(Base): # table
    __tablename__ = 'owner'
    ownerId = sqa.Column(sqa.Integer, primary_key = True)
    petId = sqa.Column(sqa.Integer)
    ownerName = sqa.Column(sqa.String(64))
    
    def __init__(self, ownerId, petID, ownerName):
        self.ownerId = ownerId 
        self.petID = petID
        self.ownerName = ownerName

if __name__=='__main__':
    #connection to a database
    engine = sqa.create_engine('sqlite:///chapter12_sqlalchemy.db')
    #ensures that all the tables associated with the Base class exist
    Base.metadata.create_all(engine)

    #create Session just one time, somewhere in the application’s global scope
    Session = sqa.orm.sessionmaker(bind=engine)
    session = Session()

    # can run only 1 time
    # once we have that values into the tables
    # we must change the IDs
    '''
    pet = Pet(1, 'dog', 'spaniel', 'female', 'Esme')
    owner = Owner(1,1,'John')
    session.add(pet)
    session.add(owner)
    session.commit()
    '''
    #select * from Pet where petName='Esme' (if more than one item then error)
    #returns a Pet object
    qry1 = session.query(Pet).filter_by(petName='Esme').one()
    print(qry1.petId, qry1.petType, qry1.petBreed,
          qry1.petGender, qry1.petName)

    # query .all()
    # returns tuples of Owner objects
    qry2 = session.query(Owner).filter_by(ownerId=1).all()
    print(qry2[0].ownerId, qry2[0].ownerName)

    #.filter is not like .filter_by
    #qry = session.query(Pet).filter(Pet.petName=="Esme")
    qry = session.query(Pet, Owner).join((Owner, Pet.petId==Owner.petId)).filter(Pet.petName=="Esme")
    print(qry)
