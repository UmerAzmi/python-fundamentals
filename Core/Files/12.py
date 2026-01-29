# 12.py

# 1) Printing headers in a table

# When we want to display data in a nice, table-like format, we can use
# formatted strings (f-strings) with width specifiers.
# Example: f"{value:10}" → reserves 10 spaces for that value.

print("Example 1: Printing headers in a table\n")

# Printing the table header
print(f"{'Name':15} {'Age':5} {'City':15}")
print("-" * 40)  # separator line

# Printing some rows with fixed column widths
print(f"{'Alice':15} {25:<5} {'New York':15}")
print(f"{'Bob':15} {30:<5} {'London':15}")
print(f"{'Charlie':15} {22:<5} {'Paris':15}")

# Explanation:
# {'Name':15}   → "Name" takes up 15 spaces (left aligned by default)
# {25:<5}       → number 25 takes 5 spaces, aligned to the LEFT
# {'City':15}   → "City" takes up 15 spaces
# "-" * 40      → prints 40 dashes as a line separator


print("\n--------------------------------\n")

# 2) Ternary Expressions
# Ternary expression = shortcut for if-else in ONE line.
# Syntax: value_if_true if condition else value_if_false

print("Example 2: Ternary Expressions\n")

age = 18

# Normal if-else
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print("Normal if-else:", status)

# Using ternary expression (short form)
status = "Adult" if age >= 18 else "Minor"
print("Using ternary expression:", status)


# Another example with boolean
book = {"title": "1984", "borrowed": True}

# Normal if-else
# Python treats some values as True and some as False automatically:
# Falsy values: False, 0, "" (empty string), [] (empty list), {} (empty dict), None
# Truthy values: pretty much everything else (True, non-zero numbers, non-empty lists/strings/dicts, etc.)

if book["borrowed"]:
    status = "Borrowed"
else:
    status = "Available"

print(f"\nBook: {book['title']} → {status}")

# Ternary expression
status = "Borrowed" if book["borrowed"] else "Available"
print(f"Book (ternary): {book['title']} → {status}")

# Explanation:
# "Borrowed" if book["borrowed"] else "Available"
# → If book["borrowed"] is True → status = "Borrowed"
# → If book["borrowed"] is False → status = "Available"
