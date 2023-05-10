"""
Adapter,
Bridge,
Composite = folosit pentru a creea o erarhie de obiecte care au atribute si functionalitati comune dar au si
relatie copil-parinte intre ele. Cele mai de la baza obiecte se numesc leaf
Decorator,
Facade,
Flyweight,
Private Class Data si
Proxy = folosit atunci cand vrem sa avem un wrapper pentr uun anumiserviciu care sa faca pre-procesari si
post-procesari necesare pentru utilizarea serviciului

"""

class Folder:

    def __init__(self, name):
        self.name = name
        self.objects = []

    @property
    def size(self):
        total_size = 0
        for obj in self.objects:
            total_size += obj.size
        return total_size

class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size

root = Folder('root')
a = Folder('a')
b = Folder('b')

f1 = File('ceva.txt', 180)
f2 = File('altceva.csv', 90)