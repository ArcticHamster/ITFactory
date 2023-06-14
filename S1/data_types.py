'''
Tipuri de date:

1. numere   -> int (numere intregi)
            -> float (numere zecimale)
2. boolean  -> valoare logica true / false
3. string   -> siruri de caractere
'''

age = 30
height = 1.70
is_married = True

first_name = 'laurentiu'
last_name = 'cosa'
description = 'putem scrie aici tot ce ne dorim, un string poate contine cam orice'

alfa = "1243" #string
beta = 'True' #string
gamma = '1.21' #string

'''
Functia Type ne poate spune ce tip de data este intr-o variabila
'''

print(type(age))
print(type(height))
print(type(first_name))

'''
ca sa schimbam tipul unei variablie folosim o tehnica numita type casting
adica functii speciale numite int, str, bool, float
care ne ajuta sa schimbam tipul variabilei'''

alfa = int(alfa)
print('Dupa type casting, alfa: ',type (alfa))
beta = bool(beta)

var_x = 'text ce nu poate fi convertit'
# var_x = int(var_x) # va da eroare

'''
int si float pot fi converite una la cealalta, cu mentiunea ca pierdem zecimalele
3.14 (float) -> 3'''
print(int(3.14))    # va afisa 3
print (float(10))   # vaafisa 10.0

'''
int si bool si ele pot fi convertite una la cealalta
True -> 1
False -> 0
viceversa, 0 va deveni False si orice alta valoare devine True
Toate tipurile de date se pot converti la string, cu functia str()'''

print(bool(-1))
print(bool(0)) # singura valoare convertita la False
print(bool(1000))

