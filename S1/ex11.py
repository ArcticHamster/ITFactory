"""
11. citeste de la tastatura un string de dimensiune impara;
afiseaza caracterul din mijloc
"""

# inp_string = input("Introdu un string impar, minim 3 caractere:\n")
#
# # mai intai eliminam stringurile neconforme: mai mici de 3 sau pare:
#
# if len(inp_string) < 3:
#     print("Ai introdus mai putin de 3 caractere!")
# elif (len(inp_string) % 2) == 0:
#     print("Numarul caracterelor introduse este par, te rog introdu un string impar!")
#
# # daca totul e ok atunci printam rezultat
#
# else:
#     print(f"Caracterul din mijloc este: {inp_string[len(inp_string) // 2]}")    # parantezele patrate se folosesc pentru indexarea caracterelor din string


# sir = input("Scrie un string:\n")

# x = sir[0]
# y = sir.replace(x, x.upper())
# print(y[0].replace(y[0],y[0].lower())+y[1:-1]+y[-1].replace(y[-1],y[-1].lower()))

user = input("user: ")
parola = input("parola: ")
print(f"parola este {'*' * len(parola)} si are {len(parola)} caractere")