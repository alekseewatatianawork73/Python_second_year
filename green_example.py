import customtkinter as ctk


def press1():
    window = ctk.CTkToplevel()
    window.configure(title='Заметки', fg_color='yellow')


def om(ch):
    if ch == 'Светлый':
        ctk.set_appearance_mode("light")
    elif ch == 'Тёмный':
        ctk.set_appearance_mode("dark")


root = ctk.CTk()
root.title("Моё приложение")
root.geometry("1000x700")
root.configure(fg_color='lightgreen')

frm = ctk.CTkFrame(master=root, width=200, height=200)
frm.configure(fg_color='green', border_color='darkgreen', border_width=3)
frm.grid(row=1, rowspan=3, column=2, columnspan=3, padx=20, pady=20, sticky="nsew")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
    frm.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)
    frm.columnconfigure(index=i, weight=1)

menu = ctk.CTkOptionMenu(master=root)
menu.configure(anchor='center', fg_color='green', dropdown_fg_color='lightgreen', button_color='darkgreen', button_hover_color='green', values=['Светлый', 'Тёмный'], font=ctk.CTkFont(family='Arial', size=20, weight='bold', slant='italic'), command=om)
menu.set('Тема фона')
menu.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

lbl = ctk.CTkLabel(master=frm)
lbl.configure(text='Мои заметки', text_color='white', font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
lbl.grid(row=0, column=3, padx=10, pady=10, sticky='nsew')

txt_output = ctk.CTkTextbox(master=frm)
txt_output.configure(font=ctk.CTkFont(family='Arial', size=15, weight='bold'), fg_color='white',
                     wrap='word', state='disabled', border_color='darkgreen', border_width=2)
txt_output.grid(row=1, column=3, padx=10, pady=10, sticky='nsew')

btn2 = ctk.CTkButton(master=frm)
btn2.configure(text="Посмотреть заметки", text_color='black', fg_color='lightgreen', hover_color='lightgrey', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn2.grid(row=2, column=3, padx=20, pady=20, sticky="nsew")
btn3 = ctk.CTkButton(master=frm)
btn3.configure(text="Удалить все заметки", text_color='black', fg_color='lightgreen', hover_color='lightgrey', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn3.grid(row=3, column=3, padx=20, pady=20, sticky="nsew")

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Открыть диалог", fg_color='darkgreen', hover_color='green', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn1.grid(row=4, column=3, padx=20, pady=20, sticky="nsew")

root.mainloop()
