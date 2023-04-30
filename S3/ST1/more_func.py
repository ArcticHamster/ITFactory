students = ['Octav', 'Gabriel', 'Bogdan', 'Liviu', 'Eugen', 'Roxana']

def say_hello(student_name):
    print(f'Hello, my name is {student_name} and I am learning Python')

for student in students:
    say_hello(student)

def sort2(x, y):
    if x > y:
        return x, y
    else:
        return y, x

sort_result = sort2(12, 5)
print(sort_result)
print(type(sort_result)) # va fi tupla, deoarece Python face packing cand returneaza mai multe valori

nr1, nr2 = sort2(100, 10) # daca stime xact numarulde valori returnate, atunci facem unpacking
print(f"Numarul 1 este {nr1} si numarul 2 este {nr2}")