"""
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
"""

from abc import ABC, abstractmethod
class FormaGeometrica(ABC):

    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai prbabil am colturi')

class Patrat(FormaGeometrica):

    def __init__(self,latura):
        self.__latura = latura
    @property
    def latura(self):           # getter - expune valoarea privata
        return self.__latura

    @latura.setter
    def latura(self,noua_latura):   #setter
        if noua_latura > 0:
            self.__latura = noua_latura
        else:
            print('Latura trebuie sa fe un numar pozitiv')


    @latura.deleter
    def latura(self):
        print('Patratul trebuie sa aiba parametrul latura')

    def aria(self):
        return print(f'Aria patratului este: {self.__latura ** 2}')

p = Patrat(8)
p.descrie()
p.aria()
del p.latura




