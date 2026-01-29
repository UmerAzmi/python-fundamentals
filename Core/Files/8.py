#Class Variable, CLass Method and static method
class Dogs:
    dogs=[]                  #Class Variable
    def __init__(self,name,age=None):
        self.name = name
        self.age = age
        self.dogs.append(self.name)

    @classmethod                 #Decorator
    def total(cls):
        return len(cls.dogs)

    @classmethod
    def nameAge(cls,data):
        names,age = data.split('-')
        return cls(names,int(age))

    def __str__(self):
        return f"Name:{self.name}, Age:{self.age}"

    @staticmethod               #Decorator
    def dawg(name,age):
        return f"Ssup Dawg, I'm {name} and i ym {age} years old SON!!"

a,b,c,d = Dogs('A'),Dogs('B'),Dogs('C'),Dogs('D')
print('Class Variable Call:',Dogs.dogs)
print('Count:',Dogs.total())
aDogs = Dogs.nameAge("Tim-20")
print(aDogs)
print(Dogs.dawg('Umer',22))
print(Dogs.dogs)

#Public and Private Class
"""using '_'(Underscore) before a variable/class/method name to indicate that it is private."""