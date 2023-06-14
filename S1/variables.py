'''
Variabila = o locatie din memorie care tine o valoare, si are un nume
1. variabilele au nume unice
2. numele de variabile in python sunt valide daca contin litere mici, mari numere si underscore
3. in general, numele de variabile folosesc litere mici si underscore
4. in general, numele de constante folosesc litere mari si underscore
5. important: folositi mereu nume sugestive
'''


varsta_mea = 31 # nume valid, bun
VARSTA_MEA = 31 # nume valid, nu e in standard Python => este de fapt constanta
VarstaMea = 31 # nume valid, nu e in standard Python
# varsta mea = 31 # nume invalid, contine spatiu
varsta_mea = 31 # nume valid, se foloseste in alte situatii
# 21varsta_mea = 31 nume invalid

'''
putem schimba valoarea variabilelor, chiar si tipul de date pe care le contin
'''
print(varsta_mea)

varsta_mea = 50 # am schimbat valoarea variabilei
print(varsta_mea)

'''putem atribui mai multe valori intr-o singura linie:
a, b, c = 10, 20. 30 <= trebuie sa avem potrivire intre numel variabilelor si valorile lor
'''

# a, b, c = 10, 20, 30, 40 da eroare
# a, b, c = 10, 20, da eroare
a, b, c, = 10, 20, 30

# toate cele 3 variabile vor avea valoarea 100, dar ele sunt variavbile diferite

x = y = z = 100