"""Tuple (tupla)  = structura de date asemna toare cu o lista, cu diferenta ca este iMUTABILA,
adica odata declarata nu se mai poate schimba
"""

t = (1, 2, 3)
print(t[0])
print(f"lungimea tuplei este de {len(t)} elemente")

tupla_complexa = (1, 2, True, 1, 2, 'string', [100, 101, 102], {0, 100})
tupla_complexa[6].append(103)
print(tupla_complexa)