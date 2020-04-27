class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('EATING')

mya = Animal()
mya.whoAmI()
mya.eat()

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    def eat(self):
        print('Dog eating')

mydog = Dog()
mydog.eat()
