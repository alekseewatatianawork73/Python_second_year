import matplotlib.pyplot as plt
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import random


x = np.linspace(-5, 5)
y = x
z = x**2
fig = plt.figure()
ax = fig.add_subplot(221, projection='3d')
ax.plot(x, y, z, color='red')

zz = np.sin(x)
ax = fig.add_subplot(222, projection='3d')
ax.plot(x, y, zz)

xxx = np.linspace(-5, 5, 15)
yyy = xxx
zzz = [random.randint(-10, 10) for i in range(15)]
ax = fig.add_subplot(223, projection='3d')
ax.scatter(xxx, yyy, zzz)
plt.show()

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z)
plt.show()

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)
plt.show()

root = ctk.CTk()
root.title("Графики")
root.geometry("1000x700")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

fig = Figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-10, 10, 500)
y = x
z = x**2
ax.plot(x, y, z, color='darkred')

# Отображение графика в customtkinter
canvas = FigureCanvasTkAgg(fig, master=root)  # создаем виджет Canvas
canvas.draw()  # рисуем график на Canvas
canvas.get_tk_widget().grid(row=3, column=3, padx=5, pady=5)  # добавляем Canvas в окно

root.mainloop()
