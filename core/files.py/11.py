#Generator
def my_gen():
    yield 'Hi'
    def anoher():
        variable = 'Umer Azmi'
        return f"2: {variable}"
    yield anoher()
    yield 'My King'

gen = my_gen()
print(next(gen))
print(next(gen))
print(next(gen),'\n')

def count_up_to(a):
    i=1
    while i <= a:
        yield i
        i += 1
for num in count_up_to(5):
    print(num)


square = [x**x for x in range(10)]
print('\n',square)
square_gen = (x**x for x in range(10))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))

gen = (x for x in range(3))
print(f'\n{next(gen)}')  # 0
print(next(gen))  # 1
print(next(gen))  # 2
# print(next(gen))

#Exception Handling
class NegativeNumberError(Exception):  # Custom Error
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Can't take square root of negative number")  # Manually raise
    return x ** 0.5

try:
    print(square_root(-9))
except NegativeNumberError as e:
    print("Custom Error Caught:", e)
else:
    print("Square root calculated successfully")
finally:
    print("End of operation")

print('\n')
try:
    print(square_root(2))
except (ValueError,TypeError) as e:
    print("Error Caught:",type(e).__name__, e)
else:
    print("Square root calculated successfully")
finally:
    print("End of operation")