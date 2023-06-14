"""
Iterator =

orice clasa care este iterabila (o putem parcurge cu un for in) trebuie sa implementeze 2 metode:
def __iter__(self)
    -> aici se initializeaza un iterator, adica se foloseste o variabila in care sa se poata retine
    iteratia curenta (self.contor = 0)
def __next__(self)
    -> aici se va returna mereu urmatoarea valoare din colectia iterata
    self.contor += 1
    return lista[self.contor]

aceste 2 metode sut apelabile din exterior fara underscore
"""

l = list([1, 5, 100])

my_iterator = iter(l)   # creez un iterator
print(next(my_iterator))    # va printa 1
print(next(my_iterator))    # 5
print(next(my_iterator))    # 100

"""
orice calsa care implementeaza cele 2 metode mentionate devine automat iterabila
astfel putem construi proprii iteratori
"""

class AlphabetIterator:

    def __iter__(self):
        self.letter = "A"
        return self

    def __next__(self):
        current_letter = self.letter
        if current_letter == 'Z':
            raise StopIteration
        self.letter = chr(ord(self.letter) + 1)
        return current_letter

alpha_iter = iter(AlphabetIterator())

# print(next(alpha_iter))
# print(next(alpha_iter))
# print(next(alpha_iter))
# print(next(alpha_iter))

for letter in alpha_iter:
    print(letter)