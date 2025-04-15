import matplotlib.pyplot as plt
import numpy as np

# задание 1
'''
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
'''

# задание 3

