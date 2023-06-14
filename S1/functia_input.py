'''
ne permite sa obtinem date de la utilizator
'''

# print('incepe programul...')
# input()   #programul asteapta aici info de la utilizator
# print("gata")

# cu \n fortam cursorul sa treaca pe linia urmatoare
name = input("care este numele tau?\n")
print(f"Salut, {name}!")

age = input("Ce varsta ai?\n")
age = int(age) # by default variabila va fi string, trebuie convertit in numar
print(f"Acum ai {age} ani, la anul vei avea {age + 1} ani")