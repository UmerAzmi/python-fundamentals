#Class and Inheritance
class dog(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.favNum= [4,7,11]

    def speak(self):
        print('Hi my name is ',self.name,', Im ',self.age,' years old and my favourite numbers are ',self.favNum)

    def change_age(self,age):
        self.age = age

    def add_weight(self,weight):
        self.weight = weight

    def talk(self):
        print('Bark!')

class cat(dog):
    def __init__(self,name,age,colour):
        super(). __init__(name,age)
        self.colour = colour
    def talk(self):
        print('Meow!')


print('Dogs:')
asim = dog('Asim',30)
sallo = dog('Sallo',20)

asim.speak()
sallo.speak()

sallo.change_age(55)
sallo.add_weight('500Kg')
print('Sallo Says:')
sallo.talk()



print('\n')
asim.speak()
sallo.speak()
print('my wieight is ',sallo.weight)

print('\nCats:')
faiya=cat('Faiya',30,'blue')
frha=cat('Frha',30,'red')

faiya.speak()
frha.speak()
faiya.talk()

# Inheritances
print('\t\n Inheritance')
class vehicle(object):
    def __init__(self,colour,price,gas):
        self.colour = colour
        self.price = price
        self.gas = gas

    def fillUpTank(self):
        self.gas = 100
    def emptyTank(self):
        self.gas = 0
    def gasLeft(self):
        return self.gas

class car(vehicle):
    def __init__(self,colour,price,gas,speed):
        super().__init__(colour,price,gas)
        self.speed = speed
    def horn(self):
        print('beep beep')

class truck(vehicle):
    def __init__(self,colour,price,gas,tires):
        super().__init__(colour,price,gas)
        self.tires = tires
    def horn(self):
        print('Honk Honk')

a = vehicle('black',800,90)
a.fillUpTank()
print(a.gasLeft())
b=car('red',900,20,1000)
b.emptyTank()
b.horn()