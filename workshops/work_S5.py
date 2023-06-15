
# Design Patterns. Iterators, Generators, Decorators

"""
Singleton
Se da următoarea clasa:


class PresedinteRomania:

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

In momentul de fata, dacă încercăm să creăm mai multe obiecte din clasa aceasta, vom putea:

a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')

Scopul acestui exercițiu este sa modificăm clasa de mai sus folosind DP Singleton pentru a obține mereu același obiect:
Vom folosi functia `__new__` (adevăratul constructor din Python)
Vom tine singurul obiect pe clasa (cls), și îl vom crea doar la prima apelare a lui __new__
La orice alta apelare, vom returna obiectul deja existent

"""

# class PresedinteRomania:
#     __instance = None
#
#     def __new__(cls, *args):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
#     def __init__(self, nume):
#         self.nume = nume
#
#     def __str__(self):
#         return "Eu sunt presedintele Romaniei."
#
#     def say_hello(self):
#         return f'Salut! Ma numesc {self.nume}! {self}'
#
#
# p1 = PresedinteRomania('Gica Petrescu')
# p2 = PresedinteRomania('Gica Petrescu Jr')
# print(p1.say_hello())
# # print(id(p1))
# # print(id(p2))
# # print(f'Acelasi obiect? {p1 is p2}')

"""
Factory Pattern
Acest pattern ne permite sa creăm un obiect dintr-o clasa folosind o alta clasa (fabrica). Fabrica are posibilitatea de a crea obiecte din mai multe clase 
(de obicei aceste clase sunt siblings, adica mostenesc de la acelasi parinte).

Vom implementa următoarele clase:
English/French/Spanish Translator – clase care știu sa traduca cuvinte din română
în limba specificata
- translations va fi un dicționar cu acele cuvinte,
exemplu `{ “masina”: “car” }` – se poate hardcoda în clasa

- localize va fi o funcție care pentru un parametru de intrare,
ne va da traducerea lui în acea limba (exemplu `input(“masina”)` returneaza “car”)

TranslatorFactory – clasa care are o singura metoda
(preferabil statica sau de clasa)
numita get_translator(language) –
in functie de parametrul language, returnează un translator object.

"""
# from abc import ABC
#
#
# class AbstractTranslator(ABC):
#     def localize(self, text):
#         raise NotImplementedError
#
#
# class EnglishTranslator(AbstractTranslator):
#
#     def __init__(self):
#         self.translations = {
#             'masina': 'car',
#             'om': 'human',
#             'curs': 'course',
#             'salut!': 'hello!'
#         }
#
#     def localize(self, text):
#         if text in self.translations:
#             return self.translations[text]
#         print('Traducerea nu exista...')
#
#
# class SpanishTranslator(AbstractTranslator):
#     def __init__(self, use_inverted_exclamation_mark=True):
#         self.translations = {
#             'masina': 'coche',
#             'om': 'hombre',
#             'curs': 'clase',
#             'salut!': 'hola!'
#         }
#         if use_inverted_exclamation_mark:
#             self.translations['salut!'] = '¡hola!'
#
#     def localize(self, text):
#         if text in self.translations:
#             return self.translations[text]
#         print('Traducerea nu exista...')
#
#
# class FrenchTranslator(AbstractTranslator):
#     def __init__(self):
#         self.translations = {
#             'masina': 'voiture',
#             'om': 'homme',
#             'curs': 'course',
#             'salut!': 'bonjour!'
#         }
#
#     def localize(self, text):
#         if text in self.translations:
#             return self.translations[text]
#         print('Traducerea nu exista...')
#
#
# class TranslatorFactory:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def get_translator(language):
#         if language == 'en':
#             return EnglishTranslator()
#         elif language == 'es':
#             return SpanishTranslator()
#         elif language == 'fr':
#             return FrenchTranslator()
#         else:
#             print('Nu exista translator pentru limba ceruta!')


"""
Dupa ce facem acesta structura, in codul meu nu voi mai avea nevoie sa stiu
ce obiect de tipul translator am, deoarece ii voi cere doar clasei Factory
sa imi dea unul gata facut!
"""
# translators = []
# translators.append(TranslatorFactory.get_translator('en'))
# translators.append(TranslatorFactory.get_translator('es'))
# translators.append(TranslatorFactory.get_translator('fr'))
#
# for t in translators:
#     print(t.localize('masina'))

"""
Generators

Implementați un generator pentru loteria 6/49 și noroc:
Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv
Ultima apelare va da un singur număr de “noroc” format din 7 cifre

"""
# import random
#
# def loto():
#     lista_numere = []
#     for i in range(6):
#         nr = random.randint(1,49)
#         while nr in lista_numere:
#             nr = random.randint(1,49)
#         lista_numere.append(nr)
#         yield nr
#
# for nr in loto():
#     print(nr)

"""
Context Managers
Se da un fisier text hello.txt, care contine un text scurt. Deschideți fișierul și citiți conținutul, folosind urmatoarele 2 metode:
try - finally 
Fișierul se deschide înainte de try, folosind functia open
În interiorul try citim conținutul folosind functia read
În finally se închide fișierul
with (context manager)
Se va observa ca pentru with nu mai este nevoie sa inchidem noi manual fișierul, pentru ca context managerul face asta pentru noi.
"""
#metoda cu with:

# with open('hello.txt', 'r') as my_file:
#     print(my_file.read())


#metoda cu try-finally:

# f = open('hello.txt')
# try:
#         print(f.read())
# finally:
#     f.close()
"""
Decorators
Implementați următorii decoratori:
timeit – decorator care măsoară timpul de execuție al unei funcții 
logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții
"""

# import time
#
# def timeit(functie):
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         request_time = functie(*args, **kwargs)
#         end_time = time.time()
#         durata = end_time - start_time
#         print(durata)
#         return request_time
#     return wrapper
#
# @timeit
# def descrie_vremea(grade):
#     time.sleep(1)
#     return f'Vremea de afara este frumoasa, sunt {grade} de grade'
#
#
# print(descrie_vremea(25))