class Masina:
    __MARCA = 'Mercedes'
    CULORI_DISPONIBILE = ('ROSU', 'BLUE', 'GRI', 'ALB')
    def __init__(self, model, viteza_max):
        # variabile de instanta, exista doar cand facem un obiect
        self.model = model
        self.viteza_max = viteza_max
        self.culoare = "GRI"
        self.viteza_act = 0
        self.__inmatriculata = False
        self.__nr_inmatriculare = None    # putem folosi si ''

    """nu facem setteri pentru inmatriculata si nr_unmatriculare, deoarece aceste ar trebui
    sa sepoate modifica DOAR prin intermediul metodei inmatriculare"""
    @property
    def inmatriculare(self):
        return self.__inmatriculata

    @property
    def nr_inmatriculare(self):
        return self.__nr_inmatriculare
    @property
    def culori_disponibile(self):
        return self.__culori_disponibile
    @property
    def marca(self):
        return Masina.MARCA

    def descrie(self):
        print(f'{self.marca} {self.model} {self.culoare}')
        print(f'Viteza : {self.viteza_act} / {self.viteza_max}')
        if self.inmatriculata:
            print('Masina este inmatriculata cu numarul {self.nr_inmatriculare}')
        else:
            print('Masina NU este inmatriculata')

    def inmatriculare(self, nr_inmatriculare):
        self.__inmatriculata = True
        self.__nr_inmatriculare = nr_inmatriculare

    @property
    def culoare(self, culoare):
        return self.__culoare

    # def vopseste(self, culoare):
    #     if culoare in self.culori_disponibile:
    #         self.culoare = culoare
    #     else:
    #         print('Culoarea nu este disponibila')

    def accelereaza(self, viteza):
        if viteza < 0:
            print('Eroare, viteza nu poate fi negativa')
        elif viteza > self.viteza_max
            self.viteza_act = self.viteza_max
        else:
            self.viteza_act = viteza

    def franeaza(self):
        self.viteza_act = 0


m1 = Masina ('clasa S', 200)
print(m1.CULORI_DISPONIBILE)
print(m1.marca)
print(Masina.__MARCA) # nu am nevoie de un obiect ca sa accesez variabileled e la clasa