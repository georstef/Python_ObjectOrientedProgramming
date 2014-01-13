def get_valid_input(input_string, valid_options):
    response = ''
    while response.lower() not in valid_options:
        response = input(input_string)
    return response

class Property:
    def __init__(self, square_feet='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet

    def display(self):
        print('PROPERTY')
        print('Square Feet:', self.square_feet)

    @staticmethod
    def prompt_init():
        return dict(square_feet=input('Enter square feet:'))

##    prompt_init = staticmethod(prompt_init)
    
class Apartment(Property):
    valid_balconies = ('yes', 'no', 'solarium')

    def __init__(self, balcony='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony

    def display(self):
        super().display()
        print('APARTMENT')
        print('Balcony:', self.balcony)
        
    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        
        balcony = get_valid_input('Enter Balcony type:', Apartment.valid_balconies)
                            
        parent_init.update({'balcony': balcony})
        return parent_init

##    prompt_init = staticmethod(prompt_init)
    
class House(Property):
    valid_garage = ('yes', 'no')

    def __init__(self, garage='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage

    def display(self):
        super().display()
        print('HOUSE')
        print('Garage:', self.garage)
        
    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        
        garage = get_valid_input('Enter Garage:', House.valid_garage)
                            
        parent_init.update({'garage': garage})
        return parent_init

##    prompt_init = staticmethod(prompt_init)

class Purchase:
    def __init__(self, price='', **kwargs):
        super().__init__(**kwargs)
        self.price = price

    def display(self):
        super().display()
        print('PURCHASE')
        print('Price:', self.price)

    @staticmethod
    def prompt_init():
        return dict(price=input('Enter Price: '))

##    prompt_init = staticmethod(prompt_init)
    
class Rental:
    def __init__(self, rental='', **kwargs):
        super().__init__(**kwargs)
        self.rental = rental

    def display(self):
        super().display()
        print('RENTAL')
        print('Rental:', self.rental)

    @staticmethod
    def prompt_init():
        return dict(rental=input('Enter Rental: '))

##    prompt_init = staticmethod(prompt_init)

class HouseRental(Rental, House): ## η σειρά είναι σημαντική για το display
    @staticmethod
    def prompt_init():
        init = House.prompt_init() ##gemisei to class House
        init.update(Rental.prompt_init()) ##prosthetei apo to class Rental
        return init

class ApartmentRental(Rental, Apartment): ## η σειρά είναι σημαντική για το display
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init() ##gemisei to class Apartment
        init.update(Rental.prompt_init()) ##prosthetei apo to class Rental
        return init

class HousePurchase(Purchase, House): ## η σειρά είναι σημαντική για το display
    @staticmethod
    def prompt_init():
        init = House.prompt_init() ##gemisei to class House
        init.update(Purchase.prompt_init()) ##prosthetei apo to class Rental
        return init

class ApartmentPurchase(Purchase, Apartment): ## η σειρά είναι σημαντική για το display
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init() ##gemisei to class Apartment
        init.update(Purchase.prompt_init()) ##prosthetei apo to class Rental
        return init

class Agent:
    type_map = {
        ("h", "r"): HouseRental,
        ("h", "p"): HousePurchase,
        ("a", "r"): ApartmentRental,
        ("a", "p"): ApartmentPurchase
        }
    
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for p in self.property_list:
            p.display()

    def add_property(self):
        property_type = get_valid_input('Property:', ('h', 'a'))
        payment_type = get_valid_input('Payment:', ('r', 'p'))

        PropertyClass = Agent.type_map[property_type, payment_type]

        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
