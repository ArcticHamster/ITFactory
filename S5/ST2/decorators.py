"""
Decorators = functii speciale care ne permit sa augumentam alte functii
Sintaxa de folosire:
@decorator
def nume_functie_decorata(....)

Sintaxa de implementare:
def decorator(func):
    def inner(*args. **kwargs):
        ... pre-procesare [optional]
        result = func(*args. **kwargs)
        ... port-procesare [optional]
        return result
    return inner
"""

# def print_hi_and_bye(func):
#
#     def inner_func():
#         print("hi")
#         func()
#         print("bye")
#     return inner_func()
#
# @print_hi_and_bye
# def say_hello():
#     print("Hello, I am a function")
#
# @print_hi_and_bye
# def introduce_yourself():
#     print("Hello, my name is...")
#
# say_hello()
# introduce_yourself()

"""
pentru a decora functii cu parametri avem nevoie sa stim si de existenta parametrilor in decorator
"""
def decadd(func):
    def inner(*args, **kwargs):    # aici avem nevoie de acelasi numar de parametri ca functia originala
        print("adding stuff...")
        result = func(*args, **kwargs) # aici trbuie sa apelam functia originala
        print("Done adding...")
        # si sa nu uitam sa returnam rezultatul la final
        return result
    return inner

@decadd
def add2(a, b):
    return a + b

@decadd
def add3(a, b, c):
    return a +b + c

print(add2(10, 17))
print(add3(1, 2, 4))