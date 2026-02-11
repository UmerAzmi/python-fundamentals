# Practice Tasks

print("Reverse a list")
nums = [10, 20, 30, 40]
print("Original:", nums)
print("Reversed:", nums[::-1])

n = 6

# Increasing/Right Angled
print('\nIncreasing/Right Angled')
for i in range(1, n):
    print('* ' * i)

# Inversed/Right Angled
print('\nInversed/Right Angled')
for i in range(n, 1, -1):
    print('* ' * i)

# Increasing/left Angled
print('\nIncreasing/left Angled')
for i in range(1, n):
    print(' ' * (n - i) + '*' * i)

# Diamond Pattern
print('\nDiamond Pattern')
for i in range(1, n):
    print(' ' * (n - i) + '* ' * i)
for i in range(n, 0, -1):
    print(' ' * (n - i) + '* ' * i)

# Pyramid Patterrn)
print('\nPyramid Patterrn')
for i in range(1,n):
    print(' '*(n-i)+'*'*(2*i-1))

# Hollow Triangle:
print('\nHollow Triangle')
for i in range(1,n+1):
    print(' '*(n-i), end='')
    if i==1:
        print('*')
    elif i==n:
        print('* '*i)
    else:
        print('*'+' '*(2*i-3)+'*')

# Number Pyramid
print('\nNumber Pyramid')
for i in range(1,n):
    print(' '*(n-i),end='')
    for j in range(1,i+1):
        print(j,end='')
    for j in range(i-1,0,-1):
        print(j,end='')
    print()



# Find max/min element
print('\nFind max/min element')
nums = [1,5,3,7,9,5,9,2]

min_num = nums[0]
max_num = nums[0]

for i in nums:
    if i < min_num:
        min_num = i
    if i > max_num:
        max_num = i
print(f'Minimum: {min_num} \nMaximum: {max_num}')
# Directly using the min and max function
print(f'\nMinimum: {min(nums)} \nMaximum: {max(nums)}')

# Second Largest Element
print('\nSecond Largest Element')
first = second = float('-inf')
for n in nums:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n
print(f'Largest Element: {first} \nSecond Largest Element: {second}')

# Remove Duplicates
unique=[]
for num in nums:
    if num not in unique:
        unique.append(num)
print(f'\nNums: {nums}\nUnique list: ',unique)

  # Sets also only takes unique elements
unique = set(unique)
sorted(unique)
print('Unique Sorted list: ',unique)

# Rotate/ Shifting Array
k = 3
k = k % len(nums)
print(f'Rotated List: {nums[-k:]+nums[:-k]}')
