# 1. Arrays / Lists
# Lists in Python are like arrays. You can store multiple values in a single variable.

numbers = [1, 2, 3, 4, 5]

print("Accessing elements:")
print(numbers[0])   # First element -> 1
print(numbers[-1])  # Last element -> 5

print("\nUpdating elements:")
numbers[2] = 10  # Update 3rd element (index 2)
print(numbers)   # Output: [1, 2, 10, 4, 5]

print("\nLooping through list:")
for num in numbers:
    print(num)

# 2. Strings
# Strings are sequences of characters and can be treated like lists.

text = "Python"
print("\nString examples:")
print(text[0])    # First character -> P
print(text[1:4])  # Slice -> 'yth'

print("\nReverse string:")
print(text[::-1])  # Output: nohtyP

# Check palindrome (word that reads the same forward and backward)
while True:
    word = 'a'
    # word = input("Enter a word: ")

    print(word)
    if word == word[::-1]:
        print('The word {wor} is a palindrome'.format(wor=word))
        break
    else:
        print(f'The word {word} is not a palindrome')

# Check Palindrone with special char
import re
s = "A man, a plan, a canal: Panama"
def palin(s):
    s = re.sub(r'[a-zA-Z0-9]','',s).lower()
    if s == s[::-1]:
        return True
    else: return False
    
print(palin(s))

# 3. Star Patterns
# Patterns help in understanding loops and nested loops.

print("\nSquare pattern (3x3):")
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

print("\nRight Triangle pattern:")
n = 4
for i in range(1, n+1):
    print("* " * i)

print("\nPyramid pattern:")
n = 4
for i in range(1, n+1):
    print(" "*(n-i) + "* "*i)
