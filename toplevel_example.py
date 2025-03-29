import customtkinter as ctk
col = 'red'


def color(ch):
    global col
    if ch == 'Красный':
        col = 'red'
    elif ch == 'Синий':
        col = 'blue'
    elif ch == 'Зелёный':
        col = 'green'


def press(ch, a, b, c, d):
    if ch == 'Круг':
        pict.create_oval(a, c, b, d, fill=col)
    elif ch == 'Прямоугольник':
        pict.create_rectangle(a, c, b, d, fill=col)
    elif ch == 'Треугольник':
        pict.create_polygon((a + b) / 2, c, a, d, b, d, fill=col)


def press1():
    window = ctk.CTkToplevel(root)
    window.title('Параметры и вид фигуры')
    window.geometry('700x500')
    window.configure(fg_color='lightgrey')
    r, c = 7, 7
    for i in range(r):
        window.rowconfigure(index=i, weight=1)
    for i in range(c):
        window.columnconfigure(index=i, weight=1)
    lbl1 = ctk.CTkLabel(master=window)
    lbl1.configure(text='Выберите фигуру', font=ctk.CTkFont(family='Arial', size=15, weight='bold'))
    lbl1.grid(row=0, column=3, padx=20, pady=20, sticky="ew")
    cmb = ctk.CTkComboBox(master=window)
    cmb.configure(justify='center', values=['Круг', 'Прямоугольник', 'Треугольник'],
               font=ctk.CTkFont(family='Arial', size=15, weight='bold', slant='italic'))
    cmb.set('Фигура')
    cmb.grid(row=1, column=3, padx=20, pady=20, sticky="ew")
    lbl2 = ctk.CTkLabel(master=window)
    lbl2.configure(text='Выберите цвет', font=ctk.CTkFont(family='Arial', size=15, weight='bold'))
    lbl2.grid(row=2, column=3, padx=20, pady=20, sticky="ew")
    cmb1 = ctk.CTkComboBox(master=window)
    cmb1.configure(justify='center', values=['Красный', 'Синий', 'Зелёный'],
                  font=ctk.CTkFont(family='Arial', size=15, weight='bold', slant='italic'), command=color)
    cmb1.set('Цвет')
    cmb1.grid(row=3, column=3, padx=20, pady=20, sticky="ew")
    lbl3 = ctk.CTkLabel(master=window)
    lbl3.configure(text='Задайте координаты',
                   font=ctk.CTkFont(family='Arial', size=15, weight='bold'))
    lbl3.grid(row=4, column=3, padx=20, pady=20, sticky="ew")
    ex1 = ctk.CTkEntry(master=window, placeholder_text='x1')
    ex2 = ctk.CTkEntry(master=window, placeholder_text='x2')
    ey1 = ctk.CTkEntry(master=window, placeholder_text='y1')
    ey2 = ctk.CTkEntry(master=window, placeholder_text='y2')
    ex1.grid(row=5, column=2, padx=20, pady=20, sticky="ew")
    ey1.grid(row=6, column=2, padx=20, pady=20, sticky="ew")
    ex2.grid(row=5, column=4, padx=20, pady=20, sticky="ew")
    ey2.grid(row=6, column=4, padx=20, pady=20, sticky="ew")
    btn = ctk.CTkButton(master=window)
    btn.configure(text="Добавить фигуру", fg_color='green', hover_color='lightgreen',
                  font=ctk.CTkFont(family='Arial', size=15, weight='bold'),
                  command=lambda: press(cmb.get(), int(ex1.get()), int(ex2.get()), int(ey1.get()), int(ey2.get())))
    btn.grid(row=7, column=3, padx=20, pady=20, sticky="ew")


def press2():
    pict.delete('all')


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Моё приложение")
root.geometry("1000x700")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Холст', font=ctk.CTkFont(family='Arial', size=25, weight='bold'))
lbl.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

pict = ctk.CTkCanvas(master=root)
pict.configure(width='500', height='300', bg='yellow', cursor='hand2', relief='sunken', borderwidth=5)
pict.grid(row=1, column=3, padx=20, pady=20)

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Нарисовать фигуру", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn1.grid(row=4, column=3, padx=20, pady=20, sticky="nsew")

btn2 = ctk.CTkButton(master=root)
btn2.configure(text="Очистить холст", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press2)
btn2.grid(row=5, column=3, padx=20, pady=20, sticky="nsew")

root.mainloop()
