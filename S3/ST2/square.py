class Square:

    def __init__(self, l):
        self.l = l

    def get_area(self):
        return self.l * self.l

    def get_perimeter(self):
        return self.l * 4

s1 = Square(5)
print(f' sunt primul patrat, cu latura de {s1.l}, cu aria {s1.get_area()} si perimetrul {s1.get_perimeter()}')

s2 = Square(12)
print(f' sunt al doilea patrat, cu latura de {s2.l}, cu aria {s2.get_area()} si perimetrul {s2.get_perimeter()}')

"""
Tema pentru acasa:

clase pentru Circle, Rectangle, Triangle
fiecare clasa va avea si un atribut de culoare optional
iar cametoda, se vor celele geometrice care au sens, plus o metoda de describe
din fiecare clasa sa faceti 1-3 obiecte cu care sa va jucati 
"""