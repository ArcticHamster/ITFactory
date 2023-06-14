"""
Implementați o clasă User, cu următoarele cerințe:
– constructorul va primi nume, email, parola, și data nasterii
– o metoda login, care va primi email și parola ca parametrii; dacă acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informațiile despre user DOAR DACĂ acesta este logat, folosind un decorator `@require_login`
– o metoda logout, fara params, care delogheaza userul.

Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, și după încă o logare.
"""

class User:


    def __init__(self, nume, email, parola, data_nastere):
        self._nume = nume
        self._email = email
        self.__parola = parola
        self._data_nastere = data_nastere


    # def utilizator_nou(self):
    #     self._nume = input(str('Introdu nume:\n'))
    #     self._email = input(str('Introdu email:\n'))
    #     self.__parola = input(str('Introdu parola:\n'))
    #     self._data_nastere = input(str('Introdu data nastere:\n'))
    def login(self, email, parola):
        if self._email == email and self.__parola == parola:
            print('User logat')
        else:
            print('email sau parola incorecte')

    @login
    def get_info(self):
        print(f'date utilizator: {self._nume}, {self._email}, {self._data_nastere}')



util1 = User('Laur', 'only.laur@gmail.com', 'password', '01.05.1980')
# util1.utilizator_nou()

util1.login(input(str('Introdu email:\n')), input(str('Introdu parola:\n')))
util1.get_info()