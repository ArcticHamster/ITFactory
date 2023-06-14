def poz(list_):
    list_poz = []
    for number in list_:
        if number >= 0:
            list_poz.append(number)
    return list_poz


lista1 = poz([1, 5, -1, 4, -8])
lista2 = poz([0, -7, -33, 81, 46, -11, 9])
print(lista1)
print(lista2)

t(f'INSERT INTO Countries VALUES ({country_code[i]}, {country_name[i]}, {continent_id[i]}, {population[i]});')