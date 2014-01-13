class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)
        # Add e-mail logic here

class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value in their name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
# --------------------------------------------------
class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self):
        print("If this were a real system we would send an order to {}".format(self.name))

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        #super(Friend, self).__init__(name, email) it's the same
        self.phone = phone

# --------------------------------------------------
# solution for diamond problem
# 2 classes that are reunited in another class
# with this solution there is a problem with the PHONE parameter
# to review later on
class Contact2(object):
    all_contacts = ContactList()

    def __init__(self, name='', email='', **kwargs):
        super(Contact2, self).__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class AddressHolder(object):
    def __init__(self, street='', city='', state='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend2(Contact2, AddressHolder):
    def __init__(self, phone, **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

class EmailableContact(Contact, MailSender):
    pass

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest
