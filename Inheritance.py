#inheritance concept



#Base class
class Animal():
    
    #Constructor
    def __init__(self):
        print("ANIMAL CREATED")
    
    def who_am_i(self):
        print("I am an animal")

    def Eat(self):
        print("I am eating")

#using inheritance
class Dog(Animal): #Derived class

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
        

#Making objects

my_object=Animal()

my_object.Eat()

my_object=Dog()

my_object.Eat()