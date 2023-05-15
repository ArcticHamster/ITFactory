"""
tema ex 8 de la functii:
8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.

Pentru toate exercițiile. Apelați funcția de cel puțin 2 ori cu valori diferite pentru a testa.
Dacă funcția are return, printează răspunsul.
"""


def suma(a, b):
    return a + b


result = suma(2, 5)
print(result)
print('_' * 20)


def par(x):
    return bool(x % 2 == 0)


check = par(7)
print(check)
print('_' * 20)


# def char(name):
#     return len(name) - name.count(" ")
#
#
# nume = char(str(input("introdu numele:\n")))
# prenume = char(str(input("introdu prenumele:\n")))
# print("numarul total de caractere: ", nume + prenume)
#

def dr_area(l1, l2):
    return l1 * l2


dr1 = dr_area(3, 5)
print(dr1)
print('_' * 20)

# Ex 6 var1:
# def func(text):
#     return text.count(char)
#
#
# char = "x"
# text1 = func("0 e singura valoare care e convertita la False")
# print(bool(text1))
# print('_' * 20)

# Ex 6 var 2:


def char_find(my_string, my_char):
    if my_char in my_string:
        return True
    else:
        return False


my_char1 = 'w'
my_string1 = 'Functie care returneaza True daca un caracter x se gaseste intr-un string dat si False daca nu gaseste'

print(f'Caracterul {my_char1} se regaseste in string: {char_find(my_string1, my_char1)}')


def upp_low(string):
    print(f'numarul de char upper este: {sum(1 for i in string if i.isupper())}')
    print(f'numarul de char lower este: {sum(1 for i in string if i.islower())}')


upp_low("Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA pe ecran")
print('_' * 20)

# var 2:
# def upperlower(my_string):
#     upper = 0
#     lower = 0
#     for c in range(len(my_string)):
#         if my_string[c].upper() == my_string[c] and my_string[c].isalpha():
#             upper += 1
#         elif my_string[c].lower() == my_string[c] and my_string[c].isalpha():
#             lower += 1
#     print(f'Numarul de carcatere upper este: {upper}')
#     print(f'Numarul de carcatere lower este: {lower}')
#
#
# upperlower('Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA pe ecran')


def poz(list_):
    list_poz = []
    for number in list_:
        if number >= 0:
            list_poz.append(number)
    return list_poz


lista1 = poz([1, 5, -1, 4, -8])
lista2 = poz([0, -7, -33, 81, 46, -11, 9])
print(lista1)
print(lista2)


# 11. Funcție care primește o lună din an și returnează câte zile are acea lună.
def get_days_no_2(year, month):
    if month == 2 and year % 4 == 0:
        # here we check if month is February , if is divisible by 4
        # a leap year occures every 4 years
        print("Number of days is 29")
    elif month == 2:
        print("Number of days is 28")
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("Number of days is 31")
    else:
        print("Number of days is 30")


get_days_no_2(2023, 4)

"""13. Funcție care primește o listă de cifre (adică doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""


def lista(*args):
    d = {}
    for i in args:
        d[i] = args.count(i)
    return d


print(lista(1, 3, 1, 5, 9, 7, 7, 5, 5))

"""tema: sa-l facem cu for in for si un if"""

"""
16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""
def common(lista_1, lista_2):
    set1 = set(lista_1)
    set2 = set(lista_2)
    return set1.intersection(set2)

lista = common([1, 5, -1, 4, -8, -33], [1, -7, -33, 81, 46, -11, 9])
print(lista)
