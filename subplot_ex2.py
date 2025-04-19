# Библиотека matplotlib: работа с графиками
import matplotlib.pyplot as plt
import numpy as np


# создаём фигуру для отображения графиков с четырьмя координатными плоскостями axs
fig, axs = plt.subplots(2, 2)
# задаём размер фигуры и название
fig.set_size_inches(10, 7)
plt.suptitle('Графики', fontsize=15)
# задаём значения x
x = np.linspace(-10, 10)

# график функции y = 2x
y1 = 2 * x
axs[0, 0].plot(x, y1, linewidth=2, color='black', linestyle='--')

# график функции y = x^2
y2 = x**2
axs[0, 1].plot(x, y2, linewidth=2, color='red', linestyle='-.')

# график функции y = x^3
y3 = x**3
axs[1, 0].plot(x, y3, linewidth=2, color='green', linestyle=':')

# график функции y = sin(x)
y4 = np.sin(x)
axs[1, 1].plot(x, y4, linewidth=2, color='blue', linestyle='-')

# добаавим общую легенду для графиков
fig.legend(labels=['y = 2x', 'y = x^2', 'y = x^3', 'y = sin(x)'], title="Легенда")

# оптимизируем расположение элементов графика (помогает избежать наложения)
plt.tight_layout()
# сохранение графика в виде файла (png, jpg, pdf), transparent=True - прозрачный фон
fig.savefig('graphics (2).pdf', format='pdf')

plt.show()
