"""
Создайте класс Worker, у которого есть:

метод __init__, принимающий 4 аргумента: имя, зарплата, пол и паспорт. Необходимо сохранить их в следующих атрибутах: name, salary, gender и passport.
свойство get_info, которое распечатает информацию о сотруднике в следующем виде: «Worker {name}; passport-{passport}»

Ниже имеется список кортежей persons, содержащий информацию о десяти работниках.
На основании этих данных необходимо создать 10 экземпляров класса Worker и добавить их в список  worker_objects.
Работников в списке следует разместить в том же порядке, в каком они встречаются в списке persons.

В этом же порядке для каждого объекта в списке worker_objects вызовите метод get_info
"""

class Worker:
    def __init__(self, name, salary, gender, passport):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        return print(f'Worker {self.name}; passport-{self.passport}')

persons= [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]

worker_objects = [Worker(*i) for i in persons]

for i in worker_objects:
    i.get_info()


# bob = Worker('Bob Moore', 330000, 'M', '1635777202')
#bob.get_info() # печатает "Worker Bob Moore; passport-1635777202"