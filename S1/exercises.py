# grade = float(input("introdu nota\n"))
# american_grade = ""
# if grade > 10 or grade <= 0:
#     print("Ai introdus o valoare gresita!")
# else:
#     if grade <= 4:
#         american_grade = "F"
#     elif grade < 6:
#         american_grade = "E"
#     elif grade < 7:
#         american_grade = "D"
#     elif grade < 8:
#         american_grade = "B"
#     elif grade < 9:
#         american_grade = "B"
#     else:
#         american_grade = "A"
#
#     print(f"Felicitari, ai luat nota {american_grade}")

x = int(input("Introdu x:\n"))
y = int(input("Introdu y:\n"))
z = int(input("Introdu z:\n"))

# maxi = x    # presupunem ca valoarea maxima este x
# if maxi < y:
#     maxi = y
# if maxi < z
#     maxi = z
# print(f"Valoarea maxima este {maxi}")
# print(f"Verificare: {max(x, y, z)}")

# if x >= y and x >= z:
#     print(x)
# elif y >= x and y >= z:
#     print(y)
# else:
#     print(z)

if x >= y:
    if x >= z:
        print(x)
    else:
        print(z)
else:
    if y >= z:
        print(y)
    else:
        print(z)

