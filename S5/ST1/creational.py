"""
Factory Method,
Abstract Factory,
Builder,
Singleton,
Object Pool si
Prototype

1. Singleton = design pattern care ne permite sa avem o clasa care mereu returneaza acceasi instanta unica
De obicei il folosim insituatii incare nu ne ne intereseaza obiectul in sine, ci doar anumite functionalitati
(metode) ale acestuia

Exemplu: un Logger pentru un proiect - adica o clasa care scrie informatii despre felul in care ruleaza un sistem
in timp real in fisiere cu extensia.log
"""

class Car:
    def __init__(self):
        pass

c1 = Car()
c2 = Car()

print(id(c1))
print(id(c2))

"""
c1 si c2 sunt obiecte diferite, adica au ID-uri diferite si se afla in locatii de memorie diferite
"""

class SingletonLogger:
    __instance = None   # atributul de clsa __instance va actiona ca un obiect fals

    """
    Functia init nu este un constructor, ci este un initializator
    inainte este apelata de fapt functia __new__ care creeaza un obict in realitate
    """

    def __new__(cls,*args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

print("_" *50)

s1 = SingletonLogger()
s2 = SingletonLogger()
print(id(s1))
print(id(s2))
print(s1 == s2)
s1.logger_level = "Debug"
print(s2.logger_level)

print("_" *50)
