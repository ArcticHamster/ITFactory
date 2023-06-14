"""
Python:
modul = un fisier cu extensia .py (adica un cod care il putem rula cu Python)
    => putem folosi codul in alte fisiere folosind import

Import: folosirea unui cod dintr-un loc extern in fisierul nosreu curent. Optiuni:

from modul import ceva => importam doar <ceva> care poate fi o variabila, o functie, o clasa
from module import * => importam to ce e in modul
import modul => importa tot din interiorul fisierului
"""
import my_module
# trebuie sa folosim notatia cu punct ca sa accessam elementele

print(my_module.a)


"""
Alias import
ultimul import va fi cel luat in considerare daca functiile se numesc la fel
daca nu dorim asta, putem importa un element sub alt nume folosind alias import
(uneori se foloseste ca sa scurtam unele nume, sau sa evitam conflicte de cod

Putem aliasa si numele de modul:
import my_module as mm
"""
from my_module import my_func as my_func1
from my_other_module import my_func as my_func2
