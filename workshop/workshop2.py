"""
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.

1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o.
Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială."""

# l = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(l)
# li = l[::-1]
# print(li)
# li.reverse()
# print(li)
"""Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări. Ambele variante își găsesc utilitatea în funcție de ce ne dorim în acel moment. 

2. De câte ori apare ‘do’?"""
# print(li.count('do'))

"""3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
   Găsește 2 variante să le unești într-o singură listă. """
# l1 = [3, 1, 0, 2]
# l2 = [6, 5, 4]
# l1.append(l2)
# l3 = l1 + l2
# print(str(l3))

# sau:

# for i in l2:
#     l1.append(i)

"""4.Sortează și afișează lista generată la exercițiul anterior.
Sortează numărul 0 folosind o funcție.
Afișaza iar lista."""
# l1.sort()
# print(l1)

"""5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
Lista este goală.
Lista nu este goală."""



"""6. Folosește o funcție care să șteargă lista de la exercițiul 3."""
# del l1[:]
# print(l1)

"""7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.

8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)"""
# dict1 = {
#     'Ana' : 8,
#     'Gigel' : 10,
#     'Dorel' : 5
# }
# l = dict1.keys()
# print(l[])

# sau:

# chei = tuple(dict1.keys())
# for i in chei:
#     print(f'{i} a luat nota {dict1.get(i)}')
# print(chei[0])
# print('_' * 50)
"""9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie"""
# print(f'Ana a luat nota {dict1.get("Ana")}')
# print(f'Gigel a luat nota {dict1.get("Gigel")}')
# print(f'Dorel a luat nota {dict1.get("Dorel")}')
#varianta 2 :
# x = [key for key in dict1]
# print(x)
"""10. Dorel a făcut contestație și a primit 6
Modifică nota lui Dorel în 6
Printează nota după modificare"""
# dict1['Dorel'] = 6
# print(f'Dorel are acum nota {dict1["Dorel"]}, el a facut contestatie')

"""11. Gigel se transferă din clasă
Căuta o funcție care să îl șteargă
Vine un coleg nou. Adaugă Ionică, cu nota 9
Printează noii elevi"""

# del dict1["Dorel"]
# dict1['Ionica'] = 9
# print(dict1)


"""12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
Efectuează schimbarea 
Șterge jucătorul scos din listă
Adaugă jucătorul intrat
Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
Afișază ‘mai ai z schimbări’

Testează codul cu diferite valori

Google search hint
“how to check if item is în list python”

13.Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
Adaugă în zilele_sapt ‘luni’
Afișează zile_sapt

14.Folosește un if și verifică dacă:
Weekend este un subset al zilelor din săptămânii.
Weekend nu este un subset al zilelor din săptămânii."""

# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

# var 1
# if zile_sapt.intersection(weekend) == weekend:
#     print('Weekend este un subset al zilelor din săptămânii')
# else:
#     print('Weekend nu este un subset al zilelor din săptămânii')

# if weekend.issubset(zile_sapt):
#     print('Weekend este un subset al zilelor din săptămânii')
# else:
#     print('Weekend nu este un subset al zilelor din săptămânii')

"""15. Afișează diferențele dintre aceste 2 seturi.

16. Afișează intersecția elementelor din aceste 2 seturi.

Partea 2 - Cicluri repetitive

Exerciții - studiu în workshopul de weekend

1.Având lista:"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

"""Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while."""
# cazul for each:
# for i in masini:
#     print(f'Masina mea preferata este {i}')

# cazul while:
# masina  = 0
# while masina < len(masini):
#     print (f'Masina mea preferata este: {masini[masina]}')
#     masina += 1

# cazul for:
# l = len(masini)
# for i in range(l):
#     print(f'Masina mea preferata este: {masini[i]}')

"""2. Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista."""
#   var 1:
# res = []
# l = len(masini)
# res.append(masini[0])
# for i in range(1, l-1, 1):
#     x = masini[i].upper()
#     res.append(x)
# res.append(masini[l-1])
#
# print(res)

#   var 2:
# for i in range(1, len(masini)-1):
#     masini[i] = masini[i].upper()
# print(masini)

"""3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘"""

# for car in masini:
#     if car == 'Mercedes'
#         print('Am gasit masina dvs')
#     break
# else:
#     print(f"am gasit masina {car}, mai cautam")

"""4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.


5. Modernizează parcul de mașini:

Crează o listă goală, masini_vechi.
Iterează prin mașini.
Când găsesti Lăstun sau Trabant:
Salvează aceste mașini în masini_vechi.
Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
Printează Modele vechi: x.
Modele noi: x."""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for car in range(len(masini)):
#     if masini[car] == 'Lastun' or masini[car] == 'Trabant':
#         masini_vechi.append(masini[car])
#         masini[car] = 'Tesla'
#
# print(f'Modele vechi:', masini_vechi)
# print(f'Modele noi:', masini)

"""6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.

Prezintă doar mașinile care se încadrează în acest buget.
Iterează prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
Iterează prin listă.

7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count).

8. Aceeași listă:
Iterează prin ea
Calculează și afișează suma numerelor (nu ai voie să folosești sum).

9. Aceeași listă:
Iterează prin ea.
Afișază cel mai mare număr (nu ai voie să folosești max)."""

# numere = [12, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# # de gasit o alta varianta mai simpla
# for nr in numere:
#     if nr > range(len(numere)):
#         maxim = numere[nr]
# print(maxim)

"""10. Aceeași listă:
Iterează prin ea.
Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
Afișază noua listă."""

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# negative = []
# for nr in numere:
#     if nr > 0:
#         nr = -nr
#     negative.append(nr)
# print(negative)


"""11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere 
Populează corect celelalte liste
Afișează cele 4 liste la final


12. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4


# Tema pentru acasa:
13. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!"""

# Varianta 1:
# import random
# numar_secret = random.randint(1,30)
# numar_ghicit = int(input("Introdu un numar de la 1 la 30:\n"))
#
# while numar_ghicit < numar_secret :
#     print(f"Nr secret e mai mare: {numar_secret}")
#     break
# while numar_ghicit > numar_secret:
#     print(f"Nr secret e mai mic: {numar_secret}")
#     break
# while numar_ghicit == numar_secret:
#     print("Felicitări! Ai ghicit!")
#     break

#Varianta 2

# import random
# numar_secret = random.randint(1,30)
# numar_ghicit = None
#
# while True:
#     numar_ghicit = int(input("Introdu un numar de la 1 la 30:\n"))
#     if numar_secret > numar_ghicit:
#         print(f"Nr secret e mai mare: {numar_secret}")
#
#     elif numar_secret < numar_ghicit:
#         print(f"Nr secret e mai mic: {numar_secret}")
#     else:
#         print("Felicitări! Ai ghicit!")
#         break

# de adaugat daca numarul e mai mare de 30

"""14. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777"""

# numar = int(input("introdu numar:\n"))
#
# for i in range(numar+1):
#     print(str(i)*i)
# print()

"""Ex:3
1
22
333

Tema pentru acasa
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)"""

# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# for grup in tastatura_telefon:
#     for cifra in grup:
#         print(f"Cifra curenta este: {cifra}")


"""Exerciții Recomandate - studiu individual                                        .

1. Revizualizează sesiunile din această săptămână și ia notițe în caz că ți-a scăpat ceva.

2. Vizualizează din cursul  ‘Primii pași în Programare’ de la sectiunile de mai jos:
Structuri de date 
Flow Control
"""