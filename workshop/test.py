#formatare text:

# text = 'LaurC'
#
# print(f'formatare la  stanga: *****{text:<7}*****')
# print(f'formatare la dreapta: *****{text:>7}*****')
# print(f'formatare la  centru: *****{text:^7}*****')

class ExpressoMachine:

    drinks = {
        'expresso':(40,15,0),
        'long coffee':(100,15,0),
        'latte':(40,15,100)
    }

    def __init__(self,water, milk, beans):
        self.water = water
        self.milk = milk
        self.beans = beans



