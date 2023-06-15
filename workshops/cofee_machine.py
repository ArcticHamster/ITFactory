class CoffeeMachine:
    def __init__(self, water, milk, beans):  # clasa contine ingredientele (se va defini cu resursele initiale)
        self.water = water
        self.milk = milk
        self.beans = beans

    def make_coffee(self):
        print('Enter choice:')
        print("1 - Espresso", "2 - Long Coffee", "3 - Cappuccino", "4 - Latte")
        coffee = int(input())

        if coffee == 1:
            print('Making Expresso...done!')
            self.water -= 40
            self.beans -= 14

        elif coffee == 2:
            print('Making Long Coffe...done!')
            self.water -= 120
            self.beans -= 14

        elif coffee == 3:
            print('Making Cappuccino...done!')
            self.water -= 80
            self.beans -= 14
            self.milk -= 20

        elif coffee == 4:
            print('Making Latte...done!')
            self.water -= 40
            self.beans -= 14
            self.milk -= 100
        print('Enjoy')

    def report(self):

        return {
            'Water': self.water,
            'Milk': self.milk,
            'Beans': self.beans
        }

    def available(self):
        if self.water < 100:
            print('Please add water')

m = CoffeeMachine(500, 200, 150)
m.make_coffee()
print(m.report())
