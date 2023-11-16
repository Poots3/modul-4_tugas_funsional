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
