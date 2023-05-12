"""
Generatori = o modalitate simpla de a genera valori care pot fi parcurse secvential
dpdv al sintaxei, sunt functii care folosesc cuvantul cheie Yield pentrua da inapoi
o valoare codului care i-a apelat.

spre deosebire de ofunctie normala, care va vi executata de la inceput ori de cate ori este apelata,
generatorii vor continua dupa Yield

Yield = cedeaza
"""

# def func_gen():
#     print('Am intrat in generator')
#     yield 10  # functia generator va returna o valoare
#
#     print('Am intrat din NOU in functie')
#     yield 100
#
#     print("am intrat a 3-a oara in generator")
#
# gen = func_gen()
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))    # va da eroare deoarece nu ajunge la nici o intructiune Yield

"""
Generatorii sunt foarte utili deoarece pot crea valori noi la fiecare apelare,
si consum putine resurse
"""
# generator de patrate perfecte
def pp(limit = 10):
    p = 0
    while p < limit:
        yield p ** 2
        p += 1

gen_pp = pp()
print(next(gen_pp))
print(next(gen_pp))
print(next(gen_pp))
print(next(gen_pp))
print(next(gen_pp))
print("incepem FOR")

for val in gen_pp:
    print(val) # daca nu punem limita va intra in bucla infinita

# daca vrem sa o luam de la 0, trebuie sa facem un nou generator, nu avem cum sa mergem inapo