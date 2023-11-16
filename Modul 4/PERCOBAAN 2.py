#PERCOBAAN 2
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())