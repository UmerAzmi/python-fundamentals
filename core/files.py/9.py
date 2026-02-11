#Map Function

li = [1,2,3,4,5,6,7,8,9]
def func(x):
    return x**x
# Without Map
newlist = []
for x in li:
    newlist.append(func(x))
print('\nMap Function:\nWithout Map:',newlist)

# With Map
print('With Map:',list(map(func,li)))

#Filter Function
def isodd(x):
    return x%2!=0

a= list(filter(isodd,li))
b= list(map(func,a))
print('\nFilter Function:\nA:',a)
print('B:',b)

#Lambda Functions (Anonymous)
print('\nNormal Functions:',isodd(5))
isOdd = lambda x:x%2!=0
print('Lambda Function:',isOdd(5))

print('Map with Lambda function:',list(map(lambda x:x**x,li)))