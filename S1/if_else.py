'''
piesa_faina = True

print ('pornim radio')
if piesa_faina == True:
    print ("dam mai tare")
    print ("fredonam")
print ("oprim radio")
'''
# exercitiu
# daca numarul este par printam asta, altfel printam impar

# nr = -5
#
# if nr % 2 == 0:
#     print ("numarul" + " " + str(nr) + " " + "este numar par")
# else:
#     print ("numarul" + " " + str(nr) + " " + "este numar impar")
#
# # este un numar pozitiv?
#
# if nr > 0:
#     print ("numarul este pozitiv")
# else:
#     print ("numarul nu este pozitiv")
#
# # if, else if, else
# # cum ne saluta robotelul in functie de ora?
#
# ora = int(input('Introdu ora: '))
# if ora < 0:
#     print ("ora trebuie sa fie intre 0 si 24")
# elif ora <=11 and ora >=5:
#     print ("buna dimineata!")
# elif ora <=18 and ora >=5:
#     print ('buna ziua!')
# elif ora <=21 and ora >=5:
#     print ('buna seara')
# elif ora <=24 and ora >=5:
#     print ('noapte buna')
# else:
#     print ('n-ar trebui sa dormi la ora asta?')
# CTRL + /

# robotel telefonic

optiunea = int(input("alege o optiune: "))
if optiunea == 0:
    print ("meniul anterior")
elif optiunea == 1:
    print ("ati ales ro")
elif optiunea == 2:
    print("ati ales en")
else:
    print ("nu am identificat optiunea")
