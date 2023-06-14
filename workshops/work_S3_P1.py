
# Partea 1- Funcții

"""
Pentru toate exercițiile. Apelați funcția de cel puțin 2 ori cu valori diferite pentru a testa.
Dacă funcția are return, printează răspunsul.

1.Funcție care să calculeze și să returneze suma a două numere
"""

# def suma(a, b):
#     return a + b
# result = suma(2, 5)
# print(result)
# print('_' * 20)

"""
2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
"""

# def par(x):
#     return bool(x % 2 == 0)
# check = par(7)
# print(check)
# print('_' * 20)

"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""

# def char(name):
#     return len(name) - name.count(" ")
#
# nume = char(str(input("introdu numele:\n")))
# prenume = char(str(input("introdu prenumele:\n")))
# print("numarul total de caractere: ", nume + prenume)

"""
4. Funcție care returnează aria dreptunghiului
5. Funcție care returnează aria cercului
"""
# def dr_area(l1, l2):
#     return l1 * l2
#
#
# dr1 = dr_area(3, 5)
# print(dr1)
# print('_' * 20)

"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
"""
# VAR 1:
# def func(text):
#     return text.count(char)
#
# char = "x"
# text1 = func("0 e singura valoare care e convertita la False")
# print(bool(text1))
# print('_' * 20)

# VAR 2:


# def char_find(my_string, my_char):
#     if my_char in my_string:
#         return True
#     else:
#         return False
#
#
# my_char1 = 'w'
# my_string1 = 'Functie care returneaza True daca un caracter x se gaseste intr-un string dat si False daca nu gaseste'
#
# print(f'Caracterul {my_char1} se regaseste in string: {char_find(my_string1, my_char1)}')

"""
7. Funcție fără return, primește un string și printează pe ecran:
Numărul de caractere lower case este x
Numărul de caractere upper case exte y 
"""
# VAR 1:
# def upp_low(string):
#     print(f'numarul de char upper este: {sum(1 for i in string if i.isupper())}')
#     print(f'numarul de char lower este: {sum(1 for i in string if i.islower())}')
#
#
# upp_low("Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA pe ecran")
# print('_' * 20)

# VAR 2:
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
# upperlower('Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA pe ecran')

"""
8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.
"""
# def poz(list_):
#     list_poz = []
#     for number in list_:
#         if number >= 0:
#             list_poz.append(number)
#     return list_poz
#
#
# lista1 = poz([1, 5, -1, 4, -8])
# lista2 = poz([0, -7, -33, 81, 46, -11, 9])
# print(lista1)
# print(lista2)

"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
Primul număr x este mai mare decat al doilea număr y
Al doilea număr y este mai mare decat primul număr x
Numerele sunt egale. 

10. Funcție care primește un număr și un set de numere.
Printează ‘am adaugat numărul nou în set’ + returnează True
Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
"""

"""
11. Funcție care primește o lună din an și returnează câte zile are acea lună.
"""

# def get_days_no_2(year, month):
#     if month == 2 and year % 4 == 0:
#         # here we check if month is February , if is divisible by 4
#         # a leap year occures every 4 years
#         print("Number of days is 29")
#     elif month == 2:
#         print("Number of days is 28")
#     elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#         print("Number of days is 31")
#     else:
#         print("Number of days is 30")
#
#
# get_days_no_2(2023, 4)

"""
12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.

În final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""

"""
13. Funcție care primește o listă de cifre (adică doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0, 1 :2, 2: 0, 3: 1, 4: 0, 5: 3, 6: 0, 7: 2, 8: 0, 9: 1
}
"""
# VAR 1:
# def lista(*args):
#     d = {}
#     for i in args:
#         d[i] = args.count(i)
#     return d
#
#
# print(lista(1, 3, 1, 5, 9, 7, 7, 5, 5))

# VAR 2:
# def lista2(*args):
#     d = {
#         0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0
#         }
#     for i in args:
#         if i in d:
#             d[i] += 1
#     return d
# #
# print(lista2(1, 3, 1, 5, 9, 7, 7, 5, 5))
"""
tema: sa-l facem cu for in for si un if
"""

"""
14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
"""
def mai_mare(x, y, z):
    return max(x, y, z)

print(mai_mare(1,5,3))

"""
15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)

16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""
# def common(lista_1, lista_2):
#     set1 = set(lista_1)
#     set2 = set(lista_2)
#     return set1.intersection(set2)
#
# lista = common([1, 5, -1, 4, -8, -33], [1, -7, -33, 81, 46, -11, 9])
# print(lista)

"""
17. Funcție care să aplice o reducere de preț.
Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.
"""

# def price_reduction(price, discount):
#     if discount > 100 or price < 0:
#         return 'Reducere invalida'
#     else: return price - discount/100 * price
# result = price_reduction(100,10)
# print(result)

"""
18.Funcție care să afișeze data și ora curentă din România.
(bonus: afișază și data și ora curentă din China)
"""

# VAR 1:
# from datetime import datetime # am importat clasa 'datetime' din biblioteca 'datetime', functie folosita pentru manipularea datelor si a timpului
# import pytz # pytz este o bibliotecă Python pentru lucrul cu fusurile orare.
#
# def ora_curenta_in_romania():
#     # Această linie creează un obiect timezone reprezentând fusul orar al Bucureștiului (care este fusul orar al întregii Românii)
#     tz_bucharest = pytz.timezone('Europe/Bucharest')
#     # Această linie obține data și ora curentă, conform fusului orar pe care tocmai l-am definit
#     datetime_bucharest = datetime.now(tz_bucharest)
#     # Aici, funcția returnează data și ora curentă din București
#     return datetime_bucharest

# Această linie apelează funcția ora_curenta_inromania și afișează rezultatul său.
# print(ora_curenta_in_romania())
#
# def ora_curenta_in_china():
#     tz_shanghai = pytz.timezone('Asia/Shanghai')
#     datetime_shanghai = datetime.now(tz_shanghai)
#     return datetime_shanghai
#
# print(ora_curenta_inchina())
#
# print(''* 80)

# VAR 2:
# def ora_curenta_locala():
#     datetime_locala = datetime.now()
#     return datetime_locala
#
# print(ora_curenta_locala())
# print(''* 80)

"""
19. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)
"""

# import datetime
#
# def zile_pana_la_craciun():
#     azi = datetime.date.today() # 'datetime.date.today' este o functie care returneaza data curenta
#     craciun = datetime.date(azi.year, 12, 25) #datetime.date() este o funcție care creează un obiect de tip dată. I se dau trei argumente: anul, luna și ziua.
#
#     if azi > craciun:
#         craciun = datetime.date(azi.year + 1, 12, 25)
# #Dacă data curentă (azi) este mai mare (adică mai târziu în an) decât data de Crăciun, atunci variabila craciun este setată la data de Crăciun a anului următor.
#     delta = craciun - azi
#     return delta.days
# #când folosim '.days' după un obiect timedelta, obținem numărul de zile din acel timedelta.
# print(f"Mai sunt {zile_pana_la_craciun()} zile până la Crăciun.")
# print(f'Azi este {datetime.date.today()}')