#Classes in Python
#Exercise 9
# --- Q -->>> 9-1
class Restaurant():
    def __init__(self, restaurant_name, dish):
        self.restaurant_name = restaurant_name
        self.dish = dish 
    def describe_restaurant(self):
        print('Restaurant Name: '+self.restaurant_name)
        print('Dish: '+self.dish)
    def open_restaurant(self):
        print('The Restaurant is Open for Visit.')
        
        
restaurant1 = Restaurant('Khyber Charsi','Tikka')
print(restaurant1.restaurant_name)
print(restaurant1.dish)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()


# --- Q ->>> 9-3
class user():
    def __init__(self,name,age,weight):
        self.name = name
        self.weigth = weight
        self.age = age
    def describe_user(self):
        print('Name: '+self.name+'\nAge: '+self.age+'\nWeight: '+self.weigth)
    def greet_user(self):
        print('Hello, '+self.name+' Welcome to the show.')
        
user1 = user('Eisha',20,45)
user1.describe_user()
user1.greet_user()
user2 = user('Sana','Tahir',33,77)
user2.describe_user()
user2.greet_user()


# --- Q ->>> 9-4
class Restaurant():
    def __init__(self, restaurant_name, dish):
        self.restaurant_name = restaurant_name
        self.dish = dish
        self.numbers_served = 0
    def describe_restaurant(self):
        print('Restaurant Name: '+self.restaurant_name)
        print('Dish: '+self.dish)
    def open_restaurant(self):
        print('The Restaurant is Open for Visit.')
    def set_customers_served(self,customers_served):
        self.number_served = customers_served
    def increment_customers_served(self,customers_served):
        self.number_served += customers_served

restaurant = Restaurant('Cheezious','Pizza')
print('Customers served by cheezious: '+ str(restaurant.number_served))
restaurant.set_customers_served(122)
print('Customers served: '+ str(restaurant.number_served))
restaurant.increment_customers_served(20)
print('Customers served: '+ str(restaurant.number_served))


# ---- Q -->>>> 9-6
class Restaurant():
    def __init__(self, restaurant_name, dish):
        self.restaurant_name = restaurant_name
        self.dish = dish
        self.numbers_served = 0
    def describe_restaurant(self):
        print('Restaurant Name: '+self.restaurant_name)
        print('Dish: '+self.dish)
    def open_restaurant(self):
        print('The Restaurant is Open for Visit.')
    def set_customers_served(self,customers_served):
        self.number_served = customers_served
    def increment_customers_served(self,customers_served):
        self.number_served += customers_served

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine,flavors=['Strawberry','BlueBerry','Mango']):
        super().__init__(name, cuisine)
        self.flavors = flavors
    def display_flavors(self):
        print('Ice Cream Flavors: '+str(self.flavors))
        
iceStand = IceCreamStand('Walls','Dont really Know')
iceStand.display_flavors()


# --- Q ->>> 9-9
#using class car from book
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
 
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
 
    def increment_odometer(self, miles):
        self.odometer_reading += miles


#using battery car from book
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.") 
    
    def upgrade_capacity(self):
        if self.battery_size==70:
            self.battery_size = 85
            
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
 
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
 
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        
car1 = ElectricCar('BMW','A5','1999')
car1.battery.get_range()
car1.battery.upgrade_capacity()
car1.battery.get_range()
