import customtkinter as ctk


def press1():
    pass


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

pict = ctk.CTkCanvas(master=root)
pict.configure(width='250', height='250', bg='yellow', cursor='hand2')
pict.create_text(125, 20, text='Drawings', justify='center', font=ctk.CTkFont(family='Arial', size=20), fill='blue')
pict.create_line(10, 10, 230, 230, fill='red', width=5)
pict.create_line(100, 240, 100, 100, fill='blue', width=5, arrow='last', dash=(50, 2), activefill='green', arrowshape=(10, 20, 10))
pict.create_rectangle(130, 80, 210, 190, fill='red', outline='blue', width=3, activedash=(5, 4))
pict.create_polygon(100, 10, 20, 90, 180, 90)
pict.create_oval(10, 120, 190, 190, fill='grey70')
pict.create_oval(10, 10, 190, 190, fill='lightgrey', outline='white')
pict.create_arc(10, 10, 190, 190, start=0, extent=45, fill='red')
pict.create_arc(10, 10, 190, 190, start=180, extent=25, fill='orange')
pict.create_arc(10, 10, 190, 190, start=240, extent=100, style='chord', fill='green')
pict.create_arc(10, 10, 190, 190, start=160, extent=-70, style='arc', outline='darkblue', width=5)
pict.grid(row=3, column=3, padx=20, pady=20)

menu = ctk.CTkOptionMenu(master=root)
menu.configure(anchor='center', values=['Светлый', 'Тёмный'], font=ctk.CTkFont(family='Arial', size=20, weight='bold', slant='italic'), command=om)
menu.set('Тема фона')
menu.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

entr = ctk.CTkEntry(master=root)
entr.configure(justify="center", state="normal", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
entr.grid(row=1, column=3, padx=20, pady=20, sticky="nsew")

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Draw", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn1.grid(row=2, column=3, padx=20, pady=20, sticky="ew")

root.mainloop()
