"""
For (pentru) este un ciclu repetitiv care ne permite sa parcurgem colectii Python sau intervale de numere
range = functie care ne ofera un interval (o lista de indecsi)
range(start, stop, step)

"""

print(list(range(5))) # va afisa 0, 1, 2, 3, 4
print(list(range(1, 6)))    # va afisa 1...5
print(list(range(2, 10, 2))) # va afisa 2, 4, 6, 8
print(list(range(5, 0, -1)))    # va fisa 5, 4, 3, 2, 1

"""
Sintaxa lui for

for <var> in <colectie>:
    fa ceva cu <var>
"""

numbers = range(1, 10, 2)
print('Incepe bucla FOR')
for number in numbers:
    print(f'Am ajuns la numarul {number}')
    print ('Mergem la urmatorul')
print('Am terminat cu bucla FOR')

"""
Cu FOR putem itera peste orice colectie Python (list, dict, set, tuple)
"""

cars = {
    'vW Polo': 12000,
    'Mercedes Benz': 30000,
    'Jeep Compass': 23000
}
print(f'Masina Pret')
for car_name in cars:
    # in cazul dictionarelor, for va merge prin cheile acestuia
    car_price = cars[car_name]
    print(f'{car_name} {car_price}')
#   sau
    print(f'{car_name} {cars[car_name]}')

"""
Putem imbrica FOR-urile"""


matrix = [
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
]
for row in matrix:
    for elem in row:
        print(elem)