
# Partea 2- OOP _ Clase & Obiecte

"""
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria
diametru()
circumferinta()
"""

# import math
#
# class Circle:
#
#     def __init__(self, r, name, colour):
#         self.r = r
#         self.colour = colour
#         self.name = name
#
#     def get_area(self):
#         return self.r ** 2 * math.pi
#
#     def get_primeter(self):
#         return 2 * self.r * math.pi
#
#     def describe(self):
#         print(f"{self.name} are raza {self.r}, aria {round(self.get_area(),2)}, perimetrul {round(self.get_primeter(),2)} si culoarea {self.colour}")


# c1 = Circle(9, "Cercul 1", "Rosu")
# print(f"sunt cerc cu raza {c1.r}, am aria {round(c1.get_area(),2)} si perimetrul {round(c1.get_primeter(),2)}")

# c2 = Circle(13, "Cercul 2", "Negru")
# print(f"nu sunt cerc cu raza {c2.r}, am aria {round(c2.get_area(),2)} si perimetrul {round(c2.get_primeter(),2)}")
# c1.describe()
# c2.describe()

# class Cerc:
#
#     def __init__(self, r, colour, pi = 3.14):
#         self.r = r
#         self.colour = colour
#         self.pi = pi
#
#     def descrie_cerc(self):
#         print(f"cercul are culoarea {self.colour} si raza {self.r}")
#
#
#     def calc_aria(self):
#         return self.r ** 2 * self.pi
#
#     def calc_diam(self):
#         return self.r * 2
#
#     def calc_circumf(self):
#         return 2 * self.r * self.pi
#
# c1 = Cerc(9, "gri")
# c1.descrie_cerc()
# print(f'Aria lui este {c1.calc_aria()}')
# print(f'Diametrul este {c1.calc_diam()}')
# print(f'Circumferinta este {c1.calc_circumf()}')

"""
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pentru toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
"""


# class Angajat:
#
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         return 'Angajat:', self.nume, self.prenume, "salariu:", self.salariu
#
#     def nume_complet(self):
#         return self.nume + " " + self.prenume
#
#     def salariu_anual(self):
#         return f'Salariul anual este:', self.salariu * 12
#
#     def marire_salariu(self, procent):
#         self.salariu = self.salariu * procent/100
#         return f'marire de {procent}%, noul salariu este {self.salariu} lei'
#
#
# a = Angajat("Cosa", "Laurentiu", 1000)
# print(a.descrie())
# print(a.nume_complet())
# print(a.marire_salariu(int(input('Introdu marirea:\n'))))
# print(a.salariu_anual())

"""
4. Clasa Cont
   Atribute: iban, titular_cont, sold
   Constructor pentru toate atributele
   Metode:
afisare_sold() - Titularul x are în contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
"""

# class Cont:
#     def init(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#     def afisare_sold(self):
#         print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei")
#
#     def debitare_cont(self):
#         print("Tranzactia va fi comisionata")
#         suma = int(input('Suma ='))
#         if suma > self.sold:
#             print("Fonduri insuficiente")
#         else:
#             self.sold = self.sold - suma
#             return self.sold
#
#     def creditare_cont(self, suma):
#         self.sold = self.sold + suma
#         return self.sold
#
#     def debitare_cont_input(self, suma):
#         if suma > self.sold:
#             print("Fonduri insuficiente")
#         else:
#             self.sold = self.sold - suma
#             return self.sold
#
#
# #cont1 = Cont(1234 , "Popescu Vasile", 3000)
# cont2 = Cont(5678, "Ionescu Maria" , 500)
#
# cont2.afisare_sold()
# #cont2.debitare_cont()
# #cont1.afisare_sold()
# #cont2.afisare_sold()
# cont2.debitare_cont_input(int(input("Suma de debitare:")))

"""
TEMA PENTRU 27.05: EXERCITIU 4, REFACUT CU PASII DE LA BANCOMAT si LOGICA DIN SPATELE INTERFETEI UNUI APARAT DE CAFEA

5. Clasa Factură
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fără serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
Indiciu pentru dată: https://www.geeksforgeeks.org/get-current-date-using-
python/
"""
# VAR 1:

# from datetime import datetime

# print(datetime.today())

# class Factura:
#     serie = 'A0001'
#
#     def __init__(self, numar):
#         self.numar = numar
#         self.date = None
#         self.total_produs = None
#         self.pret_buc = None
#         self.cantitate = None
#         self.lista_produse = {}
#         self.nume_produs = None
#         self.total_plata = None
#
#     def adauga_produs(self, nume_produs, cantitate, pret_buc):
#         self.lista_produse[nume_produs] = list()
#         self.lista_produse[nume_produs].append(cantitate)
#         self.lista_produse[nume_produs].append(pret_buc)
#         self.lista_produse[nume_produs].append(self.get_total_produs(nume_produs))
#
#     def get_total_produs(self, nume_produs):
#         return self.lista_produse[nume_produs][0] * self.lista_produse[nume_produs][1]
#
#     def schimba_cantitatea(self, nume_produs, cantitate):
#         self.lista_produse[nume_produs][0] = cantitate
#         self.lista_produse[nume_produs][2] = self.get_total_produs(nume_produs)
#
#     def schimba_pretul(self, nume_produs, pret):
#         self.lista_produse[nume_produs][1] = pret
#         self.lista_produse[nume_produs][2] = self.get_total_produs(nume_produs)
#
#     def sterge_produsul(self, nume_produs):
#         del self.lista_produse[nume_produs]
#
#     def schimba_numele_produsului(self, nume_produs, nume_nou):
#         self.lista_produse[nume_nou] = self.lista_produse[nume_produs]
#         self.sterge_produsul(nume_produs)
#
#     def get_date(self):
#         self.date = datetime.today()
#         return self.date
#
#     def genereaza_factura(self):
#         self.total_plata = 0
#         print(f"Factura seria {self.serie} numar {self.numar}")
#         print(f"Data: {self.get_date()}")
#         col1, col2, col3, col4 = "Produs", 'Cantitate', 'Pret bucata', 'Total produs'
#         col_size = 20
#
#         print(f"{col1:^{col_size}}|{col2:^{col_size}}|{col3:^{col_size}}|{col4:^{col_size}}|")
#         for produs in self.lista_produse.keys():
#             print(f"{str(produs):^{col_size}}", end="|")
#             for coloana in self.lista_produse[produs]:
#                 print(f"{str(coloana):^{col_size}}", end="|")
#             print()
#         for produs in self.lista_produse.keys():
#             self.total_plata += self.lista_produse[produs][2]
#         print('-' * 4 * col_size)
#         print(f"Total de plata: {self.total_plata}")
#         print('-' * 4 * col_size)
#
#
# f1 = Factura(1)
# f1.adauga_produs('Telefon', 7, 700)
# f1.adauga_produs('TV', 1, 2000)
# f1.adauga_produs('Frigider', 2, 1500)
# f1.genereaza_factura()
# f1.schimba_cantitatea('TV', 5)
# f1.genereaza_factura()
# f1.schimba_pretul('Telefon', 1000)
# f1.genereaza_factura()
# f1.schimba_numele_produsului('Telefon', 'Congelator')
# f1.genereaza_factura()
# f1.sterge_produsul('TV')
# f1.genereaza_factura()


# VAR 2:
# from datetime import datetime
#
# class Factura:
#
#     serie = 'X'
#
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def totalp(self,*args):
#
#         return self.cantitate * self.pret_buc
#
#     def schimba_cantitatea(self,cantitate):
#
#         self.cantitate = cantitate
#
#
#     def print_fact(self):
#         print(f'| nr |  Produs  | cant | preț/buc |  Total |')
#         print(f'|{self.numar:^4}|{self.nume_produs:^10}|{self.cantitate:^6}|{self.pret_buc:^10}|{self.totalp():^8}|')
#
# f1 = Factura(1, 'Banane', 6, 15)
# f1.print_fact()
# f1.schimba_cantitatea(4)
# f1.print_fact()
# f2 = Factura(2, 'Caise', 2, 18)
# f2.print_fact()