"""
In python class is a blueprint for creating objects. Classes encapsulate 
data and behaviors that belong together ( attributes and methods ).
"""

# define class

class Car:
    
    def __init__(self, make, model, year): #  constructor ( set class attributes )
        self.make = make
        self.model = model
        self.year = year
        
    # define class methods details and start engine
    def details(self):
        print(f"Car make is {self.make}")
        print(f"Car model is {self.model}")
        print(f"Car year is {self.year}")
    
    def start_engine(self):
        print(f"Car ({self.make}, {self.model}) engine started")
        
        
#create object
car1 = Car("Ford", "Mustang", 2020)
car1.details()
car1.start_engine()