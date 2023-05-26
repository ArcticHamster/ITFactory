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

    pi = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai prbabil am colturi')

"""
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
"""

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
    def latura(self):   #deleter
        print('Patratul trebuie sa aiba parametrul latura')

    def aria(self):
        return print(f'Aria patratului este: {self.__latura ** 2}')


# p = Patrat(8)
# p1 = Patrat(11)
# p.descrie()
# p.aria()
# p1.latura = -12
# p1.aria()
# del p.latura

"""
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)
"""
class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        print(f'Aria cercului este {Cerc.pi * self.raza ** 2}')

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self,raza_new):
        if raza_new > 0:
            self.__raza = raza_new
        else:
            print('Raza trebuie sa ie un numar pozitiv')

    @raza.deleter
    def raza(self):
        print('Raza este obligatorie')

    def descrie(self):
        print("nu am colturi")

c1 = Cerc(13)
c1.descrie()
c1.aria()
c1.raza = 15
c1.aria()






