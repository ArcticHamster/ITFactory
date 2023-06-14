"""1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă."""
# o variabila este un spatiu de memorie alocat unei valori ce se poate schimba

"""2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
string
int
float
bool
Observație: Valorile vor fi alese de tine după preferințe."""
# var_string, valoare, double, boolean = "string by default", 20, 3.14, True

"""3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat."""
# print(type(var_string))
# print(type(valoare))
# print(type(double))
# print(type(boolean))

"""4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
Verifică tipul acesteia."""
# double = round(double)
# print(type(double))

"""5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile. 
Rezolvă nepotrivirile de tip prin ce modalitate dorești."""
# print(f"Un text atribuit unei variabile este {var_string}")
# print(f"'Ca la {valoare} de ani' este numele piesei apartinand trupei Voltaj")
# print(f"PI este raportul dintre circumferinta si diamentrul oricarui cerc si are valoarea {float(double)+0.14}")
# print(f"Afirmatia de ma sus va fi intotdeauna {boolean!s} intr-un spatiu euclidian")

"""6. Citește de la tastatură:
numele;
prenumele.
    Afișează: 'Numele complet are x caractere'."""
# nume = input("Introdu numele:\n")
# prenume = input("Introdu prenumele:\n")
# print(f"Numele tau complet este {prenume} {nume}!")

"""7. Citește de la tastatură:
lungimea;
lățimea.
   Afișează: 'Aria dreptunghiului este x'.


8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
afișează de câte ori apare cuvântul 'the';


9. Același string:
Afișează de câte ori apare cuvântul 'the';
Printează rezultatul."""
# x = 'Coral is either the stupidest animal or the smartest rock'
# print(f"Sintaxa 'the' apare de {x.count('the')} ori")

"""10. Același string:
Folosește un assert ca să verifici dacă acest string conține doar numere."""
# assert x.isdigit(), f'Stringul nu contine doar numere'

"""11. Exercițiu:
citește de la tastatură un string de dimensiune impară;
afișează caracterul din mijloc."""
# inp_string = input("Introdu un string impar, minim 3 caractere:\n")
# # mai intai eliminam stringurile neconforme: mai mici de 3 sau pare:
# if len(inp_string) < 3:
#     print("Ai introdus mai putin de 3 caractere!")
# elif (len(inp_string) % 2) == 0:
#     print("Numarul caracterelor introduse este par, te rog introdu un string impar!")
# # daca totul e ok atunci printam rezultat
# else:
#     print(f"Caracterul din mijloc este: {inp_string[len(inp_string) // 2]}")    # parantezele patrate se folosesc pentru indexarea caracterelor din string

"""12. Folosind o singură linie de cod :
citește un string de la tastatură (ex: 'alabala portocala');
salvează fiecare cuvânt într-o variabilă;
printează ambele variabile pentru verificare."""
# text = input("Introdu un string:\n")
# a, b = text.split()
# print(a + "si" + b)

"""13. Exercițiu:
citește un string de la tastatură (ex: alabala portocala);
salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla."""
# text = input("Introdu un string:\n")
# a = text[0]
# print(a)
# b = text.replace(a,a.upper())
# print(b[0].replace(b[0],b[0].lower()+b[1:-1]+b[-1].replace(b[-1],b[-1].lower())))

"""14.Exercițiu:
citește un user de la tastatură;
citește o parolă;
afișează: 'Parola pt user x este ***** și are x caractere';
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
eg: parola abc => ***
      parola abcd => ****"""
# user = input("user: ")
# parola = input("parola: ")
# print(f"parola este {'*' * len(parola)} si are {len(parola)} caractere")


"""Partea 2 - Operatori, condiționale

Exerciții - studiu în workshopul de weekend

Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe. 
X este un int.

1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
# daca se indeplineste o conditie atunci se executa un cod, daca nu se executa un altul
2. Verifică și afișează dacă x este număr natural sau nu.
# adica daca este un numar intreg pozitiv"""
# x = int(input('Introdu un numar:\n'))
# if x >= 0:
#     print(f'{x} este numar natural')
# else:
#     print(f'{x} nu este numar natural')

"""
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru."""
# if x > 0:
#     print(f'{x} este numar pozitiv')
# elif x < 0:
#     print(f'{x} este numar negativ')
# else:
#     print(f'{x} este numar neutru')

"""
4. Verifică și afișează dacă x este între -2 și 13."""
# if x > -2 and x < 13:
#     print(f'{x} este cuprins intre -2 si 13')
# else:
#     print(f'{x} NU este cuprins intre -2 si 13')

"""5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5."""
# x = float(input('Introdu primul numar:\n'))
# y = float(input('Introdu al doilea numar:\n'))
# if x - y < 5:
#     print(f'Diferenta celor doua numere este mai mica decat 5')
# else:
#     print(f'Diferenta celor doua numere este mai mare sau egala cu 5')

# 5 - varianta 2-------------------------------------------------------------
# while True:
#     x = input("Introdu valoarea lui x: ")
#     y = input("Introdu valoarea lui y: ")
#     try:
#         x = float(x)
#         y = float(y)
#     except:
#         print("Mai incearca!")
#         continue
#     if x - y < 5:
#         print(f"Diferenta dintre {x} si {y} este mai mica 5, mai exact {x-y}")
#         break
#     else:
#         print(f"Diferenta dintre {x} si {y} nu este mai mica de 5, este {x-y}")
#         break
#
#
# print("-"*70)

"""6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’."""
# if not x >= 5 and x <= 27:
#     print(f'{x} NU este cuprins intre 5 si 27')
# else:
#     print(f'{x} este cuprins intre 5 si 27')

"""7. x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare."""

"""
8. x, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare."""

# while True:
#     x = int(input('Introdu latura pozitiva x:\n'))
#     if x > 0:
#         break
# while True:
#     y = int(input('Introdu latura pozitiva y:\n'))
#     if y > 0:
#         break
# while True:
#     z = int(input('Introdu latura pozitiva z:\n'))
#     if z > 0:
#         break
#
# if x == y and y == z:
#     print(f'Triunghiul este echilateral')
# elif x == y or x == z or y == z:
#     print(f'Triunghiul este isoscel')
# else:
#     print(f'Triunghiul este oarecare')

"""
9. Citește o literă de la tastatură.
    Verifică și afișează dacă este vocală sau nu.

10.Transformă și printează notele din sistem românesc în  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F

11.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)"""
# exercitiul nu este rezolvat corect, ramane tema!
# while True:
#     x = input("Introdu un numar de minim 4 cifre:\n")
#     if x.isdigit():
#         if int(x) > 0:
#             break
#     elif not x.isdigit() or int(x) < 0:
#         print(f'Nu ai introdus un numar!')
#
# if len(str(x)) >= 4:
#     print(f'Numarul {x} are {len(str(x))} cifre si indeplineste conditia')
# else:
#     print(f'Numarul {x} NU are minim 4 cifre si NU indeplineste conditia')


"""12.Verifică dacă x are exact 6 cifre.

13.Verifică dacă x este număr par sau impar (x e int)."""
# if x % 2  == 0:
#     print('E numar par')
# else:
#     print('E numar impar)
"""14.      x, y, z (int)
Afișează care este cel mai mare dintre ele?
15. 
X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.

16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
Citește de la tastatură un int x
Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'

17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
"""
# str = 'Coral is either the stupidest animal or the smartest rock'
# str1  = str[:5] + str[-5:]
# print(str1)

"""
18. Același string. 
Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)"""
# word = 'rock'
# index = str.find(word)
# print(index)

"""Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
output: 'Coral is either the stupidest animal or the smartest' """
# str2 = str[0:len(str)-len(word)]
# print(str2)

"""19. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
Ai ghicit. Felicitări! Ai ales x si zarul a fost y."""

import random
# dice_roll = random.randint(0,20)
# user_guess = int(input("Introdu un numar de la 0 la 20:\n"))
# if user_guess < dice_roll and user_guess =< 20:
#     print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {user_guess} dar a fost {dice_roll}.")
# elif user_guess > dice_roll and user_guess =< 20:
#     print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {user_guess} dar a fost {dice_roll}.")
# elif user_guess == dice_roll:
#     print(f"Ai ghicit. Felicitări! Ai ales {user_guess} si zarul a fost {dice_roll}")
# # elif user_guess > 20:
# else:
#     print(f"Numarul {user_guess} nu este valid.")
print("Ready for a round of Dice? Yes/No ")
while True:
    choice_check = input("")
    if choice_check.lower() != "no":
        print(choice_check)
        roll_dice = random.randint(1, 6)
        # print(roll_dice)
        user_guess = int(input("Guess the computer's roll: "))
        if user_guess == roll_dice:
            print("Congrats! You guessed it!")
        else:
            print(f"Such shame! Much sad! The roll was {roll_dice}")
    else:
        print("Byeeee!")
        break
    print("Wanna play again? Yes/No")

print("-"*70)

"""20.  Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat

21. Având stringul '0123456789'
Afișează doar numerele pare 
Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)
"""
# str = '0123456789'
#
# print(str[::2])
# print(str[1::2])
# print(f'Numerele pare sunt: {l[::2]}')
# print(f'Numerele impare sunt: {l[1::2]}')

