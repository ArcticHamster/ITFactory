"""
Set = structura de date care nu permite duplicate
este echivalenta cu o multime
Seturile nu sunt ordonate si nici indexate, putem doara dauga sau sterge elemente din ele
"""

s = {1, 2, 3, 1}
print(s)

s.add(7)
s.add(3)

s.remove(2)
print(s)

"""
Si setul poate tine aproape orice tip de date
-toate tipurile basic
-liste, dictionare, alte seturi, NU
-tuple DA

practic, setul poate avea valori imutabile
"""

set_cpmplex = {1, 2, True, ['lista', 'scurta'], 'Ana are mere'}
print(set_cpmplex)
set_gol = set()
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.intersection(b))
print(a.difference(b))
print(a.union(b))