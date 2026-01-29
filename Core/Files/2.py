#IF Else
height = float(input('Enter Your height: '))
age = float(input('Enter Your age: '))
if height < 5:
    print("You can't Ride")
elif height >6.5: print("You also can't ride")
else: print('You can ride')

if height >=5 and height<=6.5:
    if age>18:
        print('Go Ride')
    else: print ('Get Out')

#For Loop
for x in range(0,10,2): ### for variable_name in range(start, stop, increament by) 
    print(x)

#While Loop
    ### while condition == true:
    ###     Body
    ###     break     (manualy stops the while loop)
con = True
while con:
    password = input('Passwords: ')
    if password == 'stop':
        break
