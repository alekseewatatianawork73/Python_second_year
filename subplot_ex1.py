# Библиотека matplotlib: работа с графиками
import matplotlib.pyplot as plt
import numpy as np


# создаём фигуру для отображения графиков
fig = plt.figure(figsize=(10, 7))
plt.suptitle('Графики', fontsize=15)
# задаём значения x
x = np.linspace(-10, 10)

# график функции y = 2x
y1 = 2 * x
plt.subplot(2, 2, 1)
# синтаксис: plt.subplot(общ. кол-во строк, общ. кол-во столбцов, номер текущего графика)
plt.plot(x, y1, linewidth=2, color='black', linestyle='--')
# linestyle: '', '-', '--', '-.', ':' ('None', 'solid', 'dashed', 'dashdot', 'dotted')
plt.title('График функции y = 2x', pad=20)

# график функции y = x^2
y2 = x**2
plt.subplot(2, 2, 2)
plt.plot(x, y2, linewidth=2, color='red', linestyle='-.')
plt.title('График функции y = x^2', pad=20)

# график функции y = x^3
y3 = x**3
plt.subplot(2, 2, 3)
plt.plot(x, y3, linewidth=2, color='green', linestyle=':')
plt.title('График функции y = x^3', pad=20)

# график функции y = sin(x)
y4 = np.sin(x)
plt.subplot(2, 2, 4)
plt.plot(x, y4, linewidth=2, color='blue', linestyle='-')
plt.title('График функции y = sin(x)', pad=20)

# оптимизируем расположение элементов графика (помогает избежать наложения)
plt.tight_layout()
# сохранение графика в виде файла (png, jpg, pdf), transparent=True - прозрачный фон, dpi=300 - разрешение
fig.savefig('graphics.png')

plt.show()
