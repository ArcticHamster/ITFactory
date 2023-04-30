"""
Putem controla iteratiile folosind 2 cuvinte cheie:
- break (rupe)
- continue (continua)
"""

print('Inainte de FOR')
for nr in range(1, 10):
    if nr == 5:
        break
    print(f'Numarul curent este {nr}')
print('Dupa FOR')

print('_' * 50)

for nr in range(10):
    if nr % 2 ==1:
        continue
    print(f'\tNumar par: {nr}')

print('_' * 50)

