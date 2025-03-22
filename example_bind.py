import customtkinter as ctk

count = 1


def change(event):
    global count
    if count % 2 == 0:
        pict.configure(bg='green')
    else:
        pict.configure(bg='yellow')
    count += 1


def move_rct(event):
    if event.keysym == 'Up':
        pict.move(rct, 0, -10)  # двигаем вверх
    elif event.keysym == 'Down':
        pict.move(rct, 0, 10)  # двигаем вниз
    elif event.keysym == 'Left':
        pict.move(rct, -10, 0)  # двигаем влево
    elif event.keysym == 'Right':
        pict.move(rct, 10, 0)  # двигаем вправо


def press1():
    global x1, y1, x2, y2
    x1 += 5
    x2 -= 5
    y1 += 5
    y2 -= 5
    om(menu.get())


def press2():
    global x1, y1, x2, y2
    x1 -= 5
    x2 += 5
    y1 -= 5
    y2 += 5
    om(menu.get())


def press3():
    global x1, x2, y1, y2
    x1, x2, y1, y2 = int(ex1.get()), int(ex2.get()), int(ey1.get()), int(ey2.get())
    om(menu.get())


def om(ch):
    global rct
    pict.delete('all')
    if ch == 'Круг':
        rct = pict.create_oval(x1, y1, x2, y2, fill='red')
    elif ch == 'Прямоугольник':
        rct = pict.create_rectangle(x1, y1, x2, y2, fill='red')
    elif ch == 'Треугольник':
        rct = pict.create_polygon((x2 + x1) / 2, y1, x1, y2, x2, y2, fill='red')


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Моё приложение")
root.geometry("1200x700")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

pict = ctk.CTkCanvas(master=root)
pict.configure(width='250', height='250', bg='yellow', cursor='hand2')
pict.grid(row=3, column=3, padx=20, pady=20)
x1, y1, x2, y2 = 100, 100, 150, 150
rct = pict.create_rectangle(x1, y1, x2, y2, fill='red')
root.bind('<KeyPress>', move_rct)
pict.bind('<Double-Button-1>', change)

menu = ctk.CTkOptionMenu(master=root)
menu.configure(anchor='center', values=['Круг', 'Прямоугольник', 'Треугольник'],
               font=ctk.CTkFont(family='Arial', size=20, weight='bold', slant='italic'), command=om)
menu.set('Выберите фигуру')
menu.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

btn2 = ctk.CTkButton(master=root)
btn2.configure(text="Увеличить", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press2)
btn2.grid(row=1, column=3, padx=20, pady=20, sticky="ew")

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Уменьшить", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn1.grid(row=2, column=3, padx=20, pady=20, sticky="ew")

lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Изменить координаты:', font=ctk.CTkFont(family='Arial', size=15, weight='bold'))
lbl.grid(row=4, column=3, padx=20, pady=20, sticky="ew")

ex1 = ctk.CTkEntry(master=root, placeholder_text='x1')
ex2 = ctk.CTkEntry(master=root, placeholder_text='x2')
ey1 = ctk.CTkEntry(master=root, placeholder_text='y1')
ey2 = ctk.CTkEntry(master=root, placeholder_text='y2')

lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Левый верхний угол:', font=ctk.CTkFont(family='Arial', size=15, weight='bold'))
lbl.grid(row=5, column=2, padx=20, pady=20, sticky="ew")

lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Правый нижний угол:', font=ctk.CTkFont(family='Arial', size=15, weight='bold'))
lbl.grid(row=5, column=4, padx=20, pady=20, sticky="ew")

ex1.grid(row=6, column=1, padx=20, pady=20, sticky="ew")
ey1.grid(row=6, column=2, padx=20, pady=20, sticky="ew")
ex2.grid(row=6, column=4, padx=20, pady=20, sticky="ew")
ey2.grid(row=6, column=5, padx=20, pady=20, sticky="ew")

btn3 = ctk.CTkButton(master=root)
btn3.configure(text="Переместить", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press3)
btn3.grid(row=6, column=3, padx=20, pady=20, sticky="ew")

root.mainloop()
