"""
Parametri unei functii:
 - sunt pozitionali (adica ordinea data la definire coincide cu ordinea la apelare

 def f(a, b, c, d)
    pass

f(1, 2, 5, 7) => a=1, b=2, c=5, d=7

- nu este obligatoriu ca o finctie sa aiba parametri
def g()
    pass

- parametri fara valoare (pozitionali) sunt obligatorii
adica nu pot apela functia de mai sus fara sa ii dau 4 parametri

- exista si parametri care NU sunt pozitionali, se numesc named parameters
acestia au deja o valoare predefinita si se pot pasa folosind numele lor
"""

def my_funct(a, b, c=7, d=100):
    print(f'a={a}, b={b}, c={c}, d={d}')
"""
a si b sunt OBLIGATORII, adica trebuie sa existe MEREU cand apleam functia
c si d sunt optionali, adica daca nu le dam valoare la apelare, vor lua valoarea definita odata cu functia
"""
my_funct(1, 2)
