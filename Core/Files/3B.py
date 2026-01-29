# DICTIONARY {key: value}
"""
- Dictionaries store data in key-value pairs.
- Keys must be unique and immutable (like strings, numbers).
- Values can be any type (mutable).
- Very useful for structured data.
"""

students = {
    101: {'name': 'Umer', 'age': 22, 'grade': 'A', 'city': 'Mumbai'},
    102: {'name': 'Azmi', 'age': 23, 'grade': 'B', 'city': 'Mumbai'},
    103: {'name': 'Zubiya', 'age': 23, 'grade': 'A+', 'city': 'Delhi'}
}

hundred = {'name': 'Umer', 'age': 22, 'grade': 'A', 'city': 'Mumbai'}

# Accessing dictionary data
print(f'\nDictionary: {students}')
print('Name of 103:', students[103]['name'])
print('Age of 101:', students[101]['age'])
print('Single dictionary:', hundred['name'], '\n')

# Dictionary methods
print("All keys:", students.keys())
print("Values of student 102:", students[102].values())
print("Items of student 102:", students[102].items())



# collections.Counter

"""
What is Counter?
---------------
- Counter is a special dictionary in Python (from collections module).
- It helps us count how many times each element appears in a list, string, or any iterable.
- Instead of writing loops manually, Counter does the counting for us.

Think of it like a word counter or frequency table.
"""

from collections import Counter

# 1: Counting characters in a string
print("\nCounting characters in a string")

s = "supercalifragilisticexpialidocious"
count = Counter(s)   # automatically counts how many times each char appears
print("Counter:", count)  # Output looks like: Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1})

# Accessing frequency of a specific character
print("Frequency of 'e':", count['e'])   # 3
print("Frequency of 'x':", count['x'])   # 0 (if item not present → returns 0, not error)


# 2: Counting words in a list
print("\nCounting words in a list")

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print("Word Counter:", word_count)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

print("Frequency of 'apple':", word_count['apple'])   # 3
print("Frequency of 'cherry':", word_count['cherry']) # 1


# 3: Iterating over Counter
print("\nIterating over Counter")

for item, freq in count.items():
    print(f"Character '{item}' appears {freq} times.")


# 4: Most Common Elements
print("\nMost Common Elements")

# most_common(n) → returns the n most frequent elements as (item, count)
print("Most common element(s):", count.most_common(1))  # [('e', 3)]
print("Top 2 common elements:", count.most_common(2))   # [('e', 3), ('l', 1)]

