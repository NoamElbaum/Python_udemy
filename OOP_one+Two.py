class Sample():
    pass

x = Sample()
print(type(x))

class Dog():

    species = 'mammal'

    def __init__(self, bread, name):
        self.bread = bread
        self.name = name

mydog = Dog('Lab', 'Sammy')
other_dog = Dog(bread='haskie', name='rockie')
print(type(mydog))
print(mydog.bread)
print(other_dog.bread)
print(mydog.species)

class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


defaultc = Circle()
myc = Circle(8)
print(myc.radius)
print(defaultc.radius)
print(myc.area())
myc.radius = 2
print(myc.area())
myc.set_radius(10)
print(myc.area())