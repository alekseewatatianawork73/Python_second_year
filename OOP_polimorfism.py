# Второе занятие по ООП. Понятие полиморфизма. Создание полиморфных функций
#------------------------------------------------------------------------
# Оператор + как пример полиморфизма
print(17 + 8)  # => 15
print(3.5 + 6.4)  # => 9.9
print('abc' + 'def')  # => abcdef

#------------------------------------------------------------------------
# Полиморфизм на примере классов Животные и Растения
class Animal:
    def __init__(self, color, species):
        self.color = color
        self.species = species

    def get_information(self):
        print(f'Вид: {self.color}. Окрас: {self.species}.')


class Plant:
    def __init__(self, color, species):
        self.color = color
        self.species = species

    def get_information(self):
        print(f'Вид: {self.color}. Окрас: {self.species}.')


a = Plant('Бежевый', 'Гортензия')
b = Animal('Бурый', 'Медведь')
a.get_information()  # => Вид: Гортензия. Окрас: Бежевый.
b.get_information()  # => Вид: Медведь. Окрас: Бурый.

# Перепишем программу с использованием полиморфной функции
class Animal:
    def __init__(self, color, species):
        self.color = color
        self.species = species


class Plant:
    def __init__(self, color, species):
        self.color = color
        self.species = species


def get_information(self):
    print(f'Вид: {self.color}. Окрас: {self.species}.')


a = Plant('Бежевый', 'Гортензия')
b = Animal('Бурый', 'Медведь')
get_information(a)  # => Вид: Гортензия. Окрас: Бежевый.
get_information(b)  # => Вид: Медведь. Окрас: Бурый.

#------------------------------------------------------------------------
# Пример создания полиморфной функции для трёх классов с использованием функции isinstance()

class Pupil:  # класс учеников
    def __init__(self, form, studyplace):
        self.form = form
        self.studyplace = studyplace


class Student:  # класс студентов
    def __init__(self, course, studyplace):
        self.course = course
        self.studyplace = studyplace


class Employee:  # класс работников
    def __init__(self, name, workplace):
        self.name = name
        self.workplace = workplace

# полиморфная функция для получения места работы/учёбы
def get_workplace(obj):
    if isinstance(obj, Employee):
        return obj.workplace
    elif isinstance(obj, Student) or isinstance(obj, Pupil):
        return obj.studyplace
    else:
        return f'Объект типа {type(obj)} не имеет место работы/учёбы.'


#------------------------------------------------------------------------

