# импортируем библиотеку
import customtkinter as ctk


def press_btn():
    d1 = int(entr1.get())
    d2 = int(entr2.get())
    d3 = ''
    if cmb.get() == 'Сложение':
        d3 = d2 + d1
    elif cmb.get() == 'Вычитание':
        d3 = d1 - d2
    entr3.configure(state="normal")
    entr3.delete('0.0', "end")
    entr3.insert('0.0', (str(d3) + '\n') * 15)
    entr3.configure(state="disabled")


def choice(ch):
    sign = ctk.CTkLabel(master=root)
    if ch == 'Сложение':
        sign.configure(text='+', font=ctk.CTkFont(family='Arial', size=25, weight='bold'))
    elif ch == 'Вычитание':
        sign.configure(text='-', font=ctk.CTkFont(family='Arial', size=25, weight='bold'))
    sign.grid(row=2, column=2, padx=20, pady=20, sticky="ew")


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
lbl.configure(text='Калькулятор', font=ctk.CTkFont(family='Arial', size=25, weight='bold', slant='italic'))
lbl.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

cmb = ctk.CTkComboBox(master=root)
operations = ['Сложение', 'Вычитание']
cmb.configure(justify="center", values=operations, state='readonly', command=choice)
cmb.grid(row=1, column=3, padx=20, pady=20, sticky="ew")
cmb.set('Выберите операцию')

entr1 = ctk.CTkEntry(master=root)
entr1.configure(justify="center", state="normal", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
entr1.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

entr2 = ctk.CTkEntry(master=root)
entr2.configure(justify="center", state="normal", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
entr2.grid(row=2, column=3, padx=20, pady=20, sticky="nsew")

entr3 = ctk.CTkTextbox(master=root)
entr3.configure(state="disabled", font=ctk.CTkFont(family='Arial', size=20, weight='bold'), wrap='word')
entr3.grid(row=2, column=5, padx=20, pady=20, sticky="nsew")

r = ctk.CTkLabel(master=root)
r.configure(text='=', font=ctk.CTkFont(family='Arial', size=25, weight='bold', slant='italic'))
r.grid(row=2, column=4, padx=20, pady=20, sticky="ew")

btn = ctk.CTkButton(master=root)
btn.configure(text="Вычислить", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press_btn)
btn.grid(row=4, column=3, padx=20, pady=20, sticky="ew")

root.mainloop()
