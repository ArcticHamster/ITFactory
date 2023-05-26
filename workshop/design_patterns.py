class PresedinteRomania:
    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, nume):
        self.nume = nume

    def __str__(self):
        return "Eu sunt presedintele Romaniei."

    def say_hello(self):
        return f'Salut! Ma numesc {self.nume}! {self}'


p1 = PresedinteRomania('Gica Petrescu')
p2 = PresedinteRomania('Gica Petrescu Jr')
print(p1.say_hello())
# print(id(p1))
# print(id(p2))
# print(f'Acelasi obiect? {p1 is p2}')
