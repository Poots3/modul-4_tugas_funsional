#PERCOBAAN 3 

def title_decorator(func):
    def wrapper():
        result = func()
        make_title = result.title()
        print(make_title + " - Data is converted to title case")
        return make_title
    return wrapper

def split_string_decorator(func):
    def wrapper():
        result = func()
        splitted_string = result.split()
        print(str(splitted_string) + " - Then Data is splitted")
        return splitted_string
    return wrapper

@split_string_decorator
@title_decorator
def say_hi():
    return 'hello there'

say_hi()