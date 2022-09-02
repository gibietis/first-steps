#The goal of this exercise is to discern is-a from has-a. Above every class you'll have to determine if it's a is-a or has-a

#Animal is-a object
class Animal(object):
    pass

#Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ##??
        self.name = name

# Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ##??
        self.name = name

# Person is-a object
class Person(object):
    def __init__(self, name):
    #Person has-a name
        self.name = name
    ## Person has-a pet
        self.pet = None

# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ##??
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary
    
# Fish is-a object
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

# Halibut is-a Fish
class Halibut(Fish):
    pass

#Rover is-a Dog
rover = Dog("Rover")

#Satan is-a Cat
satan = Cat("Satan")

#Mary is-a Person
mary = Person("Mary")

#Mary has-a pet of satan kind
mary.pet = satan

#Frank is-a employee
frank = Employee("Frank", 120000)

#Frank has-a pet of kind rover
frank.pet = rover

# Flipper is-a fish
flipper = Fish()

# crouse is-a salmon
crouse = Salmon()

# harry is-a halibut
harry = Halibut()