"""
Clasa = blueprint (retaeta) prin care putem crea obiecte
Clasa contine urmatoarele elemente importante:
- numele clasei, unic, concis, ca sa intelegem ce fel de obiecte putem crea. Se incep cu litera mare!
- constructor - o functie spceiala apelata ori de cate ori vrem sa creem un obiect
- atribute - variabile apartinand unui obiect, si care sunt descriptive pentru toate obiectele din clasa
- metode - functii care pot fi apelate pe acele obiecte

self = parametru care apare in toate metodele, si mentine o referinta catre obiectul curent
"""

"""
obiectul este o INSTANTA a unei clase, de aceea zicem ca instantiem un obiect"""

class Person: # se foloseste CamelCase (nu snake_case)
    def __init__(self, name, age, gender, nationality = 'RO'):
        # de obicei in constructor pastram valorile atributelor obiectului pe self
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality
    def say_hello(self):
        print('Hello!')
        print(f'Ma numesc {bogdan.name}, am {bogdan.age} ani si sunt {bogdan.nationality}')


bogdan = Person('Bogdan', 24, 'M')
bogdan.say_hello()

kevin = Person('Kevin', 27, 'M', 'FR')
kevin.say_hello()