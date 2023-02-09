"""
Создайте класс Zebra, внутри которого есть метод which_stripe ,
который поочередно печатает фразы "Полоска белая", "Полоска черная", начиная именно с фразы "Полоска белая"

Пример работы с классом Zebra>

"""

class Zebra:
    def __init__(self, co = 1):
        self.co = co

    def which_stripe(self):
        print(f'Полоска белая' if self.co % 2 == 1 else f'Полоска черная')
        self.co += 1



z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"

