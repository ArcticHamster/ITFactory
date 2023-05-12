"""
tema ex 8 de la functii:
8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.

Pentru toate exercițiile. Apelați funcția de cel puțin 2 ori cu valori diferite pentru a testa.
Dacă funcția are return, printează răspunsul.
"""


def suma(a,b):
    return(a+b)

result = suma(2,5)
print(result)
print('_' *20)
def par(x):
    return bool(x % 2 == 0)
check = par(7)
print(check)
print('_' *20)

# def char(name):
#     return len(name) - name.count(" ")
#
# numele = char(str(input("introdu numele complet:\n")))
# print(numele)

def dr_area (l1, l2):
    return l1 * l2

dr1 = dr_area(3,5)
print(dr1)
print('_' *20)

def func(text):
    return text.count(char)

char = "x"
text1 = func("0 e singura valoare care e convertita la False")
print(bool(text1))
print('_' *20)

def upp_low (string):
    print(f'numarul de char upper este: {sum(1 for i in string if i.isupper())}')
    print(f'numarul de char lower este: {sum(1 for i in string if i.islower())}')

upp_low("Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ")
print('_' *20)

def poz (list):
    list_poz = []
    for number in list:
        if number >= 0:
            list_poz.append(number)
    return list_poz

lista1 = poz([1, 5, -1, 4, -8])
lista2 = poz([0, -7, -33, 81, 46, -11, 9])
print(lista1)
print(lista2)


