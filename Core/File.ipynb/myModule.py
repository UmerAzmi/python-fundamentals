def myFunc(x):
    return x+5
def anotherfunc(x):
    return x // 5

def mydec(func):
    def wrapper():
        print('Hello ')
        func()
        print('.')
        return
    return wrapper
