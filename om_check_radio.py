import customtkinter as ctk


def event1():
    pass


def press1():
    ch = ctk.CTkCheckBox(master=root)
    ch.configure(text=entr.get(), font=ctk.CTkFont(family='Arial', size=20, weight='bold', slant='italic'), command=event1)
    ch.grid(row=3, column=2, padx=20, pady=20, sticky="ew")


def press2():
    ch = ctk.CTkRadioButton(master=root)
    ch.configure(text=entr.get(), font=ctk.CTkFont(family='Arial', size=20, weight='bold', slant='italic'))
    ch.grid(row=3, column=4, padx=20, pady=20, sticky="ew")


def om(ch):
    if ch == 'Светлый':
        ctk.set_appearance_mode("light")
    elif ch == 'Тёмный':
        ctk.set_appearance_mode("dark")


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

menu = ctk.CTkOptionMenu(master=root)
menu.configure(anchor='center', values=['Светлый', 'Тёмный'], font=ctk.CTkFont(family='Arial', size=20, weight='bold', slant='italic'), command=om)
menu.set('Тема фона')
menu.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

entr = ctk.CTkEntry(master=root)
entr.configure(justify="center", state="normal", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
entr.grid(row=1, column=3, padx=20, pady=20, sticky="nsew")

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Checkbox", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn1.grid(row=2, column=2, padx=20, pady=20, sticky="ew")

btn2 = ctk.CTkButton(master=root)
btn2.configure(text="Radiobutton", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press2)
btn2.grid(row=2, column=4, padx=20, pady=20, sticky="ew")

root.mainloop()
