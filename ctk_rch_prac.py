import customtkinter as ctk

K = 2
C = []
D = 0
s = 1


def event1():
    global D, s
    D += s
    if D == 3:
        s = -1
    elif D == 0:
        s = 1
    l = ctk.CTkLabel(master=root)
    l.configure(text=f'Сделано {D} задач!')
    l.grid(row=5, column=4, padx=20, pady=20, sticky="ew")


def light():
    ctk.set_appearance_mode("light")
    rad2.deselect()


def dark():
    rad1.deselect()
    ctk.set_appearance_mode("dark")


def press1():
    global K, C
    ch = ctk.CTkCheckBox(master=root)
    ch.configure(text=entr.get(), font=ctk.CTkFont(family='Arial', size=20, weight='bold', slant='italic'), command=event1)
    ch.grid(row=K, column=4, padx=20, pady=20, sticky="ew")
    C.append(ch)
    if len(C) == 3:
        lb.grid(row=5, column=2, padx=20, pady=20, sticky="ew")
        btn1.configure(state='disabled')
    K += 1


def press2():
    global K, C
    btn1.configure(state='normal')
    lb.grid_forget()
    for ch in C:
        ch.grid_forget()
    C.clear()
    K = 2


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Моё приложение")
root.geometry("1000x500")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Флажки и кнопки', font=ctk.CTkFont(family='Arial', size=25, weight='bold', slant='italic'))
lbl.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

lb = ctk.CTkLabel(master=root)
lb.configure(text='Добавлено максимальное количество задач!', font=ctk.CTkFont(family='Arial', size=12, weight='bold'))

rad1 = ctk.CTkRadioButton(master=root)
rad1.configure(text='Светлый фон', font=ctk.CTkFont(family='Arial', size=20, weight='bold', slant='italic'), command=light)
rad1.grid(row=1, column=2, padx=20, pady=20, sticky="ew")

rad2 = ctk.CTkRadioButton(master=root)
rad2.configure(text='Тёмный фон', font=ctk.CTkFont(family='Arial', size=20, weight='bold', slant='italic'), command=dark)
rad2.grid(row=1, column=4, padx=20, pady=20, sticky="ew")

entr = ctk.CTkEntry(master=root)
entr.configure(placeholder_text='Введите задачу', justify="center", state="normal", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
entr.grid(row=2, column=2, padx=20, pady=20, sticky="nsew")

lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Задачи для выполнения:', font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
lbl.grid(row=2, column=3, padx=20, pady=20, sticky="ew")

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Добавить задачу", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn1.grid(row=3, column=2, padx=20, pady=20, sticky="ew")

btn2 = ctk.CTkButton(master=root)
btn2.configure(text="Удалить все задачи", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press2)
btn2.grid(row=4, column=2, padx=20, pady=20, sticky="ew")

root.mainloop()
