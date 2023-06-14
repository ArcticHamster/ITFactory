"""
Exceptiile sunt modalitatea lui Python de a informa progrmatorul ca ceva nu a mers bine in cod.
Exceptie vs eroare: in Python sunt destul de similare, in alte limbaje sunt diferite
"""

"""
Folosim exceptiile ca un mecanism de protejare a programului, a i acesta sa nu se opreasca in situatii in care nu totul merge perfect

try:
    aici avem codul
    care ar putea arunca o exceptie
except:
    aici acem codul
    care va fi apelat DACA in timpul executiei blocului try a aparut o exceptie
"""

try:
    age = int(input("Age:\n"))
    print(f"Felicitari, ai introdus o varsta corecta: {age}")
except ValueError:
    print(f"Ai introdus o varsta gresita!")
print('Am cerut varsta!')

age_intervals = ['0-18', '18-35', '35-65', '65+']
for i in range(len(age_intervals)):
    print(f'{i}: {age_intervals[i]}')
try:
    user_ai = int(input(f'In ce interval de varsta te afli?\n'))
    print(f'Te afli in intervalul {age_intervals[user_ai]}')
except ValueError:
    print('Nu ai introdus un numar')