#PERCOBAAN 1
# Higher-Order Function (HOF)
def perkalian(a, b):
    return a * b

result_hof = perkalian(2, 3)
print(result_hof)

# Currying
def curry_function(a):
    def dengan(b):
        return a * b
    return dengan

result_currying = curry_function(2)(3)
print(result_currying)


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


#PERCOBAAN 4

def translasi(tx, ty):
    def transformasi(p):
        x, y = p
        return x + tx, y + ty
    return transformasi

def dilatasi(sx, sy):
    def transformasi(p):
        x, y = p
        return x * sx, y * sy
    return transformasi

def rotasi(sudut):
    import math
    def transformasi(p):
        x, y = p
        x_baru = x * math.cos(math.radians(sudut)) - y * math.sin(math.radians(sudut))
        y_baru = x * math.sin(math.radians(sudut)) + y * math.cos(math.radians(sudut))
        return x_baru, y_baru
    return transformasi

titik = (3, 5)

translasi_2_minus_1 = translasi(2, -1)
dilatasi_2_minus_1 = dilatasi(2, -1)
rotasi_30_degrees = rotasi(30)

titik_setelah_translasi = translasi_2_minus_1(titik)
titik_setelah_dilatasi = dilatasi_2_minus_1(titik)
titik_setelah_rotasi = rotasi_30_degrees(titik)

print("Koordinat setelah translasi:", titik_setelah_translasi)
print("Koordinat setelah dilatasi:", titik_setelah_dilatasi)
print("Koordinat setelah rotasi:", titik_setelah_rotasi)


#percobaan 5
def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    def calculate_m(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    M = calculate_m(p1, p2)

    C = p1[1] - M * p1[0]

    return f"y = {M:.2f}x + {C:.2f}"


print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1, 3), point(7, 7)))

print("Persamaan garis untuk NIM akhir kalian:")
print(line_equation_of(point(7, 1), point(7, 3)))

#PERCOBAAN 6
def point(x, y):
    return x, y

def line_equation_of(x1, y1, M):
    C = y1 - M * x1

    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (5,1) dan bergradien 3:")
print(line_equation_of(3, 7, 7))

