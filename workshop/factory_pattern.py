from abc import ABC

class AbsractTranslator(ABC):

    def localize(self,text):
        raise NotImplementedError

class EnglishTranslator(AbsractTranslator):

    def __init__(self):
        self.translations = {
            'masina': 'car',
            'joc': 'game',
            'fericit': 'happy',
            'apa': 'water'
        }

    def localize(self,text):
        if text in self.translations:
            return self.translations[text]
        print('Cuvantul nu este in dictionar')


class FrenchTranslator(AbsractTranslator):

    def __init__(self):
        self.translations = {
            'masina': 'voiture',
            'joc': 'jeu',
            'fericit': 'content',
            'apa': 'eau'
        }