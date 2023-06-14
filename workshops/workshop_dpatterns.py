"""
Generators

Implementați un generator pentru loteria 6/49 și noroc:
Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv
Ultima apelare va da un singur număr de “noroc” format din 7 cifre

"""
import random


def loto():
    lista_numere = []
    for i in range(6):
        nr = random.randint(1,49)
        while nr in lista_numere:
            nr = random.randint(1,49)
        lista_numere.append(nr)
        yield nr

for nr in loto():
    print(nr)

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

def logger(functie):
    def wrapper(*args,**kwargs):
        print(f'Date intrare args {args}')
        print(f'Date intrare kwargs {kwargs}')
        request_logger = functie(*args, **kwargs)
        print(f'Date de iesire {request_logger}')
        return request_logger
    return wrapper

@logger
def mesaj(msg):
    print(f'Acesta este un mesaj: {msg}')

mesaj('am ajuns')