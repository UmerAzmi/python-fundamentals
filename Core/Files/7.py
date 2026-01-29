#Overridding Methods
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def coorinate(self):
        return (self.x,self.y)

    def __add__(self,other):
        return point(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        return point(self.x - other.x, self.y - other.y)
    def __mul__(self,other):
        return self.x * other.x + self.y * other.y
    def __truediv__(self,other):
        return self.x / other.x + self.y / other.y
    def __floordiv__(self,other):
        return self.x // other.x + self.y // other.y
    def __mod__(self,other):
        return self.x % other.x + self.y % other.y
    def __str__(self):
        return f'Point({self.x},{self.y})' # "Point("+str(self.x)+','+str(self.y)+')'

    def move(self,x,y):
        self.x += x
        self.y += y

    def length(self):
        return (self.x**2 + self.y**2)**0.5

    """
        import math
        math.sqrt(self.x**2 + self.y**2)
    """

    def __gt__(self,other):
        return self.length() > other.length()
    def __ge__(self,other):
        return self.length() >= other.length()
    def __le__(self,other):
        return self.length() <= other.length()
    def __lt__(self,other):
        return self.length() < other.length()
    def __eq__(self,other):
        return self.length() == other.length()
    def __ne__(self,other):
        return self.length() != other.length()


p1 = point(1,2)
p2 = point(3,4)
print('P1:',p1,'\nP2:',p2)
p3=p1 + p2
p4=p1 - p2
print('Addition:',p3)
print('Subtract: ',p4)
print('Multiply:',p1 * p2)
print('Divide:',p1 / p2)
print('Int Divide:',p1 // p2)
print('Modulus:',p1 % p2)
p1.move(1,2)
print('New P1:',p1)
p2.move(-1,-2)
print('New P2:',p2)
print('Greater than:',p1 > p2)
print('Greater than Equal to:',p1 >= p2)
print('Less than:',p1 < p2)
print('Less than Equal to:',p1 <= p2)
print('Equal to:',p1 == p2)
print('Not Equal to:',p1 != p2)

print(p2.coorinate())