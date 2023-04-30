"""
While (cat timp) = bucla (loop) iterativa in care un cod se executa
CAT TIMP o conditie este adevarata

while <conditie>:
    fa ceva
    fa altceva
    samd
"""

while True:
    age = input('Introdu Varsta:\n')
    if age.isdigit():
        break
print(f'Varsta este {int(age)}')