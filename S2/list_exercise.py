l = [1, 2, 3, 10]
print(type(l)) # <class 'list'>
print(l[0]) # primul element din lista, adica nr 1
print(l[3]) # al patrulea element din lista, adica 10
print(f'Lista mea are {len(l)} elemente')
print(f"deci indexul ultimului element va fi {len(l)-1}")
# sau
print(f"Ultimul element este {l[-1]}")
# accesarea unui element din afara listei duce la eroare

"""listele sunt mutabile, adica le putem modifica prin schimbarea elementelor existente
sau adaugarea unora noi, sau stergerea celor deja existente"""

print('_' * 50)
l[2] = 7 # schimb valoarea celui de-al treilea element
print(l)
l.append(15) # adugam un element nou la finalul listei
print(l)
l.insert(3,100) # inseram un element inaintea indexului dorit de noi
print(l)

l.pop() # va sterge ultimul element daca nu are nici un argument
print(l)
l.pop(0) # va sterge elementul de la indexul mentionat daca are argument

print('_' * 50)
list_strings = ['Adela', 'este', 'la', 'curs']
print(list_strings[1][0]) # va printa litera cu index 0 din stringul cu index 1, adica e
