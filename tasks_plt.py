import matplotlib.pyplot as plt
import numpy as np

# задание 1
a, b, c = map(int, input("Введите коэффициенты уравнения: ").split())

x = np.linspace(-5, 5)
y = a * x**2 + b * x + c

plt.figure(figsize=(9, 5))
plt.plot(x, y, linewidth=2, color='red', zorder=1, label='График функции')

x0 = -b / (2 * a)
y0 = a * x0**2 + b * x0 + c
plt.scatter(x0, y0, color='black', zorder=2, s=100, label='Точка минимума')

plt.title(f'Точка минимума функции y = {a}x^2 + {b}x + {c}')
plt.legend(loc='lower right')
plt.grid()
plt.show()

# задание 2
months = ['январь', 'фервраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
temps = []
for x in months:
    t = float(input(f'Средняя температура за {x}: '))
    temps.append(t)
plt.bar(months, temps, color='orange')
plt.title('Ежемесячная температура')
plt.show()

# задание 3
# food, house, clothes, relax, others
expenses = list(map(int, input('Введите расходы на еду/жильё/одежду/развлечения/другое через пробел: ').split()))
names = ['еда', 'жильё', 'одежда', 'развлечения', 'другое']
plt.figure(figsize=(10, 7))
plt.pie(expenses, labels=names, colors=['orange', 'blue', 'green', 'red', 'lightgrey'], autopct='%1.3f%%', startangle=90)
plt.legend(loc='lower right')
plt.title('Расходы', fontsize=20)
plt.show()

# задание 4
a, b, c = map(int, input("Введите коэффициенты уравнения: ").split())

fig = plt.figure(figsize=(9, 5))
fig.suptitle(f'Функция y = {a}x^2 + {b}x + {c}')

x = np.linspace(-5, 5)
y = a * x**2 + b * x + c
plt.subplot(1, 2, 1)
plt.plot(x, y, linewidth=2, color='red', label='График функции')
plt.grid()

x2 = np.linspace(-5, 5, 12)
y2 = a * x2**2 + b * x2 + c
plt.subplot(1, 2, 2)
plt.scatter(x2, y2, color='black', label='Диаграмма рассеяния')
plt.grid()

fig.legend(loc='lower right')
plt.show()

# задание 5
fig = plt.figure(figsize=(10, 7))
fig.suptitle(f'Тригонометрические функции')

x = np.linspace(-2 * np.pi, 2 * np.pi)
y1 = np.sin(x)
plt.subplot(2, 2, 1)
plt.plot(x, y1, linewidth=2, color='black', label='График синуса', linestyle='-')

y2 = np.cos(x)
plt.subplot(2, 2, 2)
plt.plot(x, y2, linewidth=2, color='red', label='График косинуса', linestyle='--')

y3 = np.tan(x)
plt.subplot(2, 2, 3)
plt.plot(x, y3, linewidth=2, color='green', label='График тангенса', linestyle='-.')

y4 = np.arctan(x)
plt.subplot(2, 2, 4)
plt.plot(x, y4, linewidth=2, color='blue', label='График арктангенса', linestyle=':')

fig.legend(loc='lower right')
plt.show()
