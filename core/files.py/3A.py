"""
DATA STRUCTURES IN PYTHON
--------------------------
In Python, we use different data structures to store and organize data:
1. List       → Ordered, mutable (can change), allows duplicates.
2. Tuple      → Ordered, immutable (cannot change), allows duplicates.
3. Set        → Unordered, mutable, no duplicates allowed.
4. Dictionary → Key-Value pairs, mutable, keys must be unique.
"""

# LIST []
"""
- Lists are ordered collections that can store multiple values.
- They allow duplicates and can hold mixed data types.
- We can add, remove, or update items in a list (mutable).
"""

fruits = ['mango', 'apple', 4]  # A list with strings and a number
print(f'Lists: {fruits}\n', '1:-', fruits[0], ' , 2:-', fruits[1], ' , 3:-', fruits[2])

# Common operations
fruits.append('watermelon')  # Add new item at the end
fruits.remove(4)             # Remove item by value
fruits.pop(1)                # Remove item by index (removes 'apple')
fruits.insert(0, 'Apple')    # Insert at a specific index
print("Updated List:", fruits)

# TUPLE ()
"""
- Tuples are ordered collections like lists, but they are immutable (cannot be changed).
- Useful for fixed data (like coordinates, days of the week, etc.).
"""

vegetable = ('potato', 'tomato', 2)
print(f'\nTuple: {vegetable}\n', '1:-', vegetable[0], ' , 2:-', vegetable[1], ' , 3:-', vegetable[2])

# Tuple methods
print(f'Count "tomato": {vegetable.count("tomato")}')   # How many times "tomato" appears
print(f'Index of "tomato": {vegetable.index("tomato")}') # First index where "tomato" appears


# SET {}
"""
- Sets are unordered collections of unique elements.
- No duplicates allowed.
- Used when you want to store unique items only.
"""

id = {1, 4, 2, 1, 5}  # Duplicate '1' will be removed automatically
print(f'\nSets: {id}')

# Set operations
id.add(3)       # Adds 3
id.add(1)       # Adding duplicate has no effect
id.remove(2)    # Removes 2 (error if not present)
id.discard(8)   # Removes 8 if present, no error if not
print(f'Updated Sets: {id}')