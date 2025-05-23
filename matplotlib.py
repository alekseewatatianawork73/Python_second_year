# Библиотека matplotlib: работа с графиками
# Сначала необходимо установить библиотеку через терминал: pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

# создаём данные для примера: списки значений для x и y одинаковой размерности
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# рисуем простой график
plt.plot(x, y)
plt.title("Простой график")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# рисуем линейный и столбчатый графики на одной плоскости
plt.plot(x, y, label='Линейный график')
plt.bar(x, y, color='orange', label='Столбчатый график')
plt.legend(loc='right')
plt.show()

# рисуем гистограмму
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, label='Гистограмма')
plt.show()

# круговая диаграмма
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f %%')  # colors = [...], startangle = angle in degrees
plt.show()

# Диаграмма рассеяния
plt.scatter(x, y, label='Диаграмма рассеяния', color='red')
plt.xlim(-5, 7)
plt.yticks(np.arange(-5, 15, 1), fontsize=12)
plt.legend()
plt.show()

# график функции y = x^2
x = [0, 1, 2, 3, 4, 5]
y = [i**2 for i in x]
plt.plot(x, y, linewidth=2, marker='o', markerfacecolor='red')
plt.grid()
plt.show()

# график функции y = x^2 (другой способ)
x = np.linspace(-10, 10)
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
y = x**2
plt.plot(x, y, linewidth=2)
plt.grid()
plt.show()
