'''
functia print ne ajuta sa aflam informatii in terminal
'''

print('laurentiu', 'cosa', 1234, True)
nume = 'Laurentiu Cosa'
print('Numele meu este: ' + nume)

# functia print trece pe o linie noua la fiecare apelare

print('numele meu este')
print(nume)

varsta = 30
# print('varsta mea este: ' + varsta) va da eroare
#f-string => un mod my pythonic de a afisa variabile in mesaje

print(f"Numele meu este {nume} si am {varsta} ani ")