class NumbersError(Exception):  # базовый класс исключения
    pass


# исключение, которое вызывается при наличии хотя бы одного нечётного числа
class EvenError(NumbersError):
    pass


 # исключение, которое вызывается при наличии хотя бы одного отрицательного числа
class NegativeError(NumbersError):
    pass


# проверяем список на наличие нечётных чисел
def no_even(numbers):
    flag = 1
    for x in numbers:
        if x % 2 != 0:
            flag = 0
    if flag:
        return True
    raise EvenError("В списке не должно быть нечётных чисел")


# проверяем список на наличие отрицательных чисел
def no_negative(numbers):
    flag = 1
    for x in numbers:
        if x < 0:
            flag = 0
    if flag:
        return True
    raise NegativeError("В списке не должно быть отрицательных чисел")


# основная программа
def main():
    print("Введите числа в одну строку через пробел:")
    try:
        numbers = list(map(int, input().split()))
        if no_negative(numbers) and no_even(numbers):
            print(f"Сумма чисел равна: {sum(numbers)}.")
    except NumbersError as e:  # обращение к исключению как к объекту
        print(f"Произошла ошибка: {e}.")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}.")


main()
