import customtkinter as ctk
count = 0


def press(lbl):
    global count
    mssg = ctk.CTkLabel(master=frm)
    mssg.configure(text=lbl, font=ctk.CTkFont(family='Arial', size=15, weight='bold'))
    mssg.grid(row=count, column=0, padx=20, pady=20, sticky="ew")
    count += 1


def press1():
    window = ctk.CTkToplevel(root)
    window.title('Меню')
    window.geometry('500x200')
    window.configure(fg_color='yellow')
    r, c = 7, 7
    for i in range(r):
        window.rowconfigure(index=i, weight=1)
    for i in range(c):
        window.columnconfigure(index=i, weight=1)
    entry_input = ctk.CTkEntry(master=window, width=250)
    entry_input.configure(justify="center", font=ctk.CTkFont(family='Arial', size=15, weight='bold'))
    entry_input.grid(row=1, column=3, padx=20, pady=20, sticky="ew")
    btn = ctk.CTkButton(master=window)
    btn.configure(text="Добавить текстовую метку", fg_color='red', font=ctk.CTkFont(family='Arial', size=15, weight='bold'),
                  command=lambda: press(entry_input.get()))
    btn.grid(row=2, column=3, padx=20, pady=20, sticky="ew")


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

frm = ctk.CTkFrame(master=root, width=200, height=200)
frm.configure(fg_color='yellow')
frm.grid(row=1, column=3, padx=20, pady=20, sticky="ew")

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Открыть меню", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn1.grid(row=4, column=3, padx=20, pady=20, sticky="ew")

root.mainloop()
