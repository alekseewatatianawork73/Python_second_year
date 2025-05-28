# Меню для пользователя
def menu():
    print('\nВыберите действие:')
    print('1. Сложение')
    print('2. Вычитание')
    print('3. Умножение\n')
    while True:
        try:
            m = int(input('Введите номер действия >> '))
            if 0 < m < 4:
                break
            else:
                print('Вы ввели некорректный ответ!')
                print('Требуется ввести целое число от 1 до 3.')
        except ValueError:
            print('Вы ввели некорректный ответ!')
            print('Пожалуйста, введите целое число.')
    return m


a, b = map(int, input('Введите два числа: ').split())
d = menu()
if d == 1:
    print(a + b)
elif d == 2:
    print(a - b)
else:
    print(a * b)
