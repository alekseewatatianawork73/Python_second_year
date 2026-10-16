# Объектно-ориентированное программирование. Переопределение операторов.
#------------------------------------------------------------------------------
# Переопределение оператора сложения "+" на примере класса для хранения списков
class MyList:
    # начальные данные - список значений lst
    def __init__(self, lst):
        self.lst = lst

    # добавим метод для вывода элементов списка MyList через запятую
    def show(self):
        sp = [str(x) for x in self.lst]
        s = ', '.join(sp)
        print(s)

    # изменим действие операции сложения над объектами MyList
    def __add__(self, other_object):
        first_list = self.lst  # => список значений нашего объекта (до +)
        second_list = other_object.lst  # => список значений второго объекта (после +)
        res_lst = []
        # будем складывать значения списков поэлементно
        for i in range(len(first_list)):
            res_lst.append(first_list[i] + second_list[i])
        return MyList(res_lst)

    # или короткий способ через генератор списков
    def __add__(self, other_object):
        first_list = self.lst
        second_list = other_object.lst
        return MyList([first_list[i] + second_list[i] for i in range(len(first_list))])


a = MyList([1, 2, 3])
b = MyList([4, 5, 6])
print('Объекты MyList:')
a.show()
b.show()
print('Результат сложения:')
c = a + b
c.show()

#-------------------------------------------------------------------------------------------
# Переопределение оператора функции str() для предыдущего класса
class MyList:
    # начальные данные - список значений lst
    def __init__(self, lst):
        self.lst = lst

    # переопределим функцию str() для возможности вывода элементов через запятую
    def __str__(self):
        sp = [str(x) for x in self.lst]
        return ', '.join(sp)


words = MyList(['red', 'green', 'blue'])
print(words)


#-------------------------------------------------------------------------------------------
# Переопределение оператора repr() на примере класса домашних животных
class Pet:
    # начальные данные - вид питомца и имя
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    # переопределим функцию str() для возможности вывода информации о животном
    def __str__(self):
        return f'Питомец-{self.kind} по имени {self.name}'

    # переопределим функцию repr() для вида объекта внутри списка
    def __repr__(self):
        return f"Pet('{self.kind}', '{self.name}')"


pet1 = Pet('собака', 'Рыжик')
pet2 = Pet('кот', 'Персик')
print('Обычный вывод:', pet1, pet2)
pets = [pet1, pet2]  # => список животных
print('Вывод внутри списка:', pets)
