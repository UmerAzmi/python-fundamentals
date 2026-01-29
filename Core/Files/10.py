import myModule
from myModule import mydec

#Decorator
def say_hello():
    print("Hello\n")
say_hello()

def my_decorator(func):
    def wrapper():
        print(f'\nGoodmorning')
        func()
        print('World')
    return wrapper

@mydec
def say_hello():
    print("Sir")

@my_decorator
def say_goodmorning():
    print("Hello")
say_hello()
say_goodmorning()

#Context Manager on file
with open("testfile.txt", "r") as f:
    content = f.read()
print(f"\n{content}\n")

#Context Manager on function
class my_context:
    def __enter__(self):
        print('My Name')
        return f'Slim Shaddy'
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('My Name again\n')

with my_context() as t:
    print(t)

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode)
        return self  # returning self so that we can use it as an object in 'with'

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        self.file.close()
        # Optional: You can return True to suppress the exception if any occurred

# Using the context manager
with FileManager("testfile1.txt", "w+") as f:
    f.file.write("Hey my G, we just used a custom context manager!\n")
    print("Writing complete.")
    f.file.seek(0)
    print("Reading full file:\n", f.file.read())
