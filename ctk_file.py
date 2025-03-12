import customtkinter as ctk


def press_open():
    address = entr.get()
    file = open(address, 'r+')
    res = file.readlines()
    txtb.configure(state="normal")
    txtb.delete('0.0', "end")
    res.reverse()
    for s in res:
        txtb.insert('0.0', s)
    file.close()


def press_save():
    address = entr.get()
    res = txtb.get('0.0', 'end')
    file = open(address, 'w+')
    file.write(res)
    file.close()
    txtb.delete('0.0', "end")
    txtb.insert('0.0', f'Файл {address} сохранён.')
    txtb.configure(state="disabled")


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
lbl.configure(text='Работа с файлами', font=ctk.CTkFont(family='Arial', size=25, weight='bold', slant='italic'))
lbl.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

entr = ctk.CTkEntry(master=root)
entr.configure(justify="center", state="normal", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
entr.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")

btn_open = ctk.CTkButton(master=root)
btn_open.configure(text="Открыть", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press_open)
btn_open.grid(row=1, column=3, padx=20, pady=20, sticky="ew")

btn_save = ctk.CTkButton(master=root)
btn_save.configure(text="Сохранить", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press_save)
btn_save.grid(row=1, column=4, padx=20, pady=20, sticky="ew")

txtb = ctk.CTkTextbox(master=root)
txtb.configure(state="disabled", font=ctk.CTkFont(family='Arial', size=20, weight='bold'), wrap='word')
txtb.grid(row=2, column=3, padx=20, pady=20, sticky="nsew")

root.mainloop()
