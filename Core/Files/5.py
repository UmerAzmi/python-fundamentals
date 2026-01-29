#Modular Programming
import math
import myModule

print(math.pi)
print(myModule.myFunc(5))
print(myModule.anotherfunc(5))

#Try and Except
text = input('Username: ')
try:
    number = int(text)
    print(number)
except:
    print('Invalid Username')

#Global and local Variable
""" #Gives error due to variable is local for that function
var = 9        ## Global 
loop = True    ## Global

def func(x):
    newVar= 7
    print(loop)   
    if x == 5:
        return newVar

print(newVar)"""

#Does not change the value due to variable is local for that function and global wont be affected by it

loop = True    ## Global
def func(x):
    loop = 7
    print('\nFirst: \n',loop)
    if x == 5:
        print(7)
func(2)
print(loop,'\n')

loop = True    ## Global
def func(x):
    global loop   ##Imports that global variable for this function
    loop = 7
    print(loop)   
    if x == 5:
        print(7)
func(2)
print(loop)
