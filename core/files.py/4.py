#Function
def squareof(x):
    return x**2
number=int(input('Enter a number: '))
print('Square is: ',squareof(number))
print('Square is: ',squareof(int(input('Enter another number: '))))
print('\nMultiple Paramerters: ')
def multipleParameters(x,y='umer'):      ###y default value is umer
    print (x)
    print(y)
    if y == 'umer':
        print('Yo Umer')
    else: print('Who')
multipleParameters(4,input('Enter a name: ').strip().lower())

#Reading in Text Files

file = open('testfile.txt','r')  ### r=read w=write
print('\nReading in Text Files\n',file.read(),'\n')
file.seek(0)
f = file.readlines()
print(f)
newlist= []
for line in f:
    if line[-1] == '\n':
        newlist.append(line[:-1])
    else:
        newlist.append(line)
print(newlist)

newlist=[]
for lins in f:
    newlist.append(lins.strip())
print(newlist)

#Writing in text file
file = open('testfile1.txt','w')
file.write('Umer Azmi')
file.write('\nIm learning how to write to a file')
file.close()

with open('testfile1.txt','w+') as file:
    file.write('Umer Azmi')
    file.write('\nIm learning how to write to a file')
    file.seek(0)
    print(file.read())