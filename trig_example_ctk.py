import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


def graph3d(f):
    fig = Figure(figsize=(7, 5))
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(-10, 10, 500)
    y = x
    if f == 'sin':
        z = np.sin(x)
    elif f == 'cos':
        z = np.cos(x)
    else:
        z = np.tan(x)
    ax.plot(x, y, z, color='darkred')

    # Отображение графика в customtkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)  # создаем виджет Canvas
    canvas.draw()  # рисуем график на Canvas
    canvas.get_tk_widget().grid(row=3, column=3, padx=5, pady=5)  # добавляем Canvas в окно


def graph2d(f):
    fig = Figure(figsize=(7, 5))
    ax = fig.add_subplot(111)
    x = np.linspace(-10, 10, 500)
    if f == 'sin':
        y = np.sin(x)
    elif f == 'cos':
        y = np.cos(x)
    else:
        y = np.tan(x)
    ax.plot(x, y, color='darkred')

    # Отображение графика в customtkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)  # создаем виджет Canvas
    canvas.draw()  # рисуем график на Canvas
    canvas.get_tk_widget().grid(row=3, column=3, padx=5, pady=5)  # добавляем Canvas в окно


def press1():
    pass


root = ctk.CTk()
root.title("Графики")
root.geometry("1000x700")

frame = ctk.CTkFrame(master=root)
frame.configure(width=500, height=500, fg_color='lightgrey', cursor='hand2', border_width=3)
frame.grid(row=1, column=1, columnspan=5, padx=10, pady=10, sticky="nsew")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
    frame.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)
    frame.columnconfigure(index=i, weight=1)

lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Тригонометрические функции', font=ctk.CTkFont(family='Arial', size=25, weight='bold', slant='italic'))
lbl.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="sin 2D", font=ctk.CTkFont(family='Arial', size=20, weight='bold'), command=lambda: graph2d('sin'))
btn1.grid(row=2, column=2, padx=20, pady=20, sticky="nsew")
btn2 = ctk.CTkButton(master=root)
btn2.configure(text="cos 2D", font=ctk.CTkFont(family='Arial', size=20, weight='bold'), command=lambda: graph2d('cos'))
btn2.grid(row=2, column=3, padx=20, pady=20, sticky="nsew")
btn3 = ctk.CTkButton(master=root)
btn3.configure(text="tg 2D", font=ctk.CTkFont(family='Arial', size=20, weight='bold'), command=lambda: graph2d('tan'))
btn3.grid(row=2, column=4, padx=20, pady=20, sticky="nsew")

btn4 = ctk.CTkButton(master=root)
btn4.configure(text="sin 3D", font=ctk.CTkFont(family='Arial', size=20, weight='bold'), command=lambda: graph3d('sin'))
btn4.grid(row=3, column=2, padx=20, pady=20, sticky="nsew")
btn5 = ctk.CTkButton(master=root)
btn5.configure(text="cos 3D", font=ctk.CTkFont(family='Arial', size=20, weight='bold'), command=lambda: graph3d('cos'))
btn5.grid(row=3, column=3, padx=20, pady=20, sticky="nsew")
btn6 = ctk.CTkButton(master=root)
btn6.configure(text="tg 3D", font=ctk.CTkFont(family='Arial', size=20, weight='bold'), command=lambda: graph3d('tan'))
btn6.grid(row=3, column=4, padx=20, pady=20, sticky="nsew")

root.mainloop()
