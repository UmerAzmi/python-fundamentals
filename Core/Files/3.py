#List []
fruits = ['apple','mango',4]  #""" FRUITS VARIABLE """
print('Lists:\n','1:-',fruits[0],' 2:-',fruits[1],' 3:-',fruits[2])

fruits.insert(2,'strawberry')
print(fruits)

fruits[3] = 'blueberry'
print(fruits)


fruits.remove('blueberry')
print(fruits)

fruits.extend(['blackberry','blueberry','watermelon'])
print(fruits,'\nIteration by Items')

#List Comprehension
li=[1,2,3,4,5,6,7,8,9]
def func(x):
    return x**x

print('\nList: ',[func(x) for x in li if x%2==0],'\n')

#Tuple ()
vegetable = ('potato','tomato')


#Iteration by items
for fruit in fruits:
    print(fruit)

print('\nIteration By Item in Fruits:')
for fruit in fruits:
    if fruit == 'blueberry':
        print('OMG')
    else: print('NMG')

print('\nIteration By Items in Range:')
for x in fruits:
    if x[-1] == 'y':
        print('kallu')
    else: print('NO')

#String Methods
text = '  Umer Azmi.47 '  #""" TEXT VARIABLE """
print("\nString method:\n",text.strip())  ##removes all the empty spaces or gaps
print(len(text))     ##Return the length of the select variable 
print(text.upper())  ##Uppercase
print(text.lower())  ##Lowercase
print(text.split())  ##Splits the string into a list

""" .find(), .count()"""
print('Finds z on: ',text.find('z'))
print('Count of m: ',text.count('m'))

#Slice Operator
print('\nSlice Operations:\n',fruits[2:4])
print(text[2:6])
print(text[:6])
print(text[2:])
print(text[2::2])
