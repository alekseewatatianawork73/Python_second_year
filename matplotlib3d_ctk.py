# Библиотека matplotlib: трёхмерные графики (3D), пример поверхностей на 3D-графиках, отрисовка графиков в customtkinter

# основные библиотеки для отрисовки графиков
import matplotlib.pyplot as plt
import numpy as np
import random
#библиотеки для вставки графиков в окно customtkinter
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


x = np.linspace(-5, 5)
y = x
z = x**2
fig = plt.figure()
ax = fig.add_subplot(221, projection='3d')  # добавляем первый подграфик в сетку 2x2, указываем размерность 3D
ax.plot(x, y, z, color='red')

zz = np.sin(x)
ax = fig.add_subplot(222, projection='3d')  # добавляем второй подграфик в сетку 2x2, указываем размерность 3D
ax.plot(x, y, zz)

xxx = np.linspace(-5, 5, 15)
yyy = xxx
zzz = [random.randint(-10, 10) for i in range(15)]
ax = fig.add_subplot(223, projection='3d')  # добавляем третий подграфик в сетку 2x2, указываем размерность 3D
ax.scatter(xxx, yyy, zzz)

plt.show()  # отображаем фигуру с тремя графиками

# примеры поверхностей в matplotlib
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z)  # отрисовываем сетчатую поверхность
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)  # отрисовываем сплошную поверхность
plt.show()

# отображение графика в окне customtkinter
# создаём окно
root = ctk.CTk()
root.title("Графики")
root.geometry("1000x700")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

# создаём график matplotlib
fig = Figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-10, 10, 500)
y = x
z = x**2
ax.plot(x, y, z, color='darkred')

# добавляем график в окно
canvas = FigureCanvasTkAgg(fig, master=root)  # создаем виджет Canvas
canvas.draw()  # рисуем график на Canvas
canvas.get_tk_widget().grid(row=3, column=3, padx=5, pady=5)  # добавляем Canvas в окно

root.mainloop()
