import customtkinter as ctk
count = 1


def change(event):
    global count
    if count % 2 == 0:
        btn1.configure(fg_color='red', hover_color='orange')
    else:
        btn1.configure(fg_color='blue', hover_color='darkblue')
    count += 1


def move_rct(event):
    if event.keysym == 'Up':
        pict.move(rct, 0, -10)  # двигаем вверх
    elif event.keysym == 'Down':
        pict.move(rct, 0, 10)    # двигаем вниз
    elif event.keysym == 'Left':
        pict.move(rct, -10, 0)   # двигаем влево
    elif event.keysym == 'Right':
        pict.move(rct, 10, 0)    # двигаем вправо


def press1():
    pict.delete('all')


def press2():
    global rct
    rct = pict.create_rectangle(100, 100, 150, 150, fill='red')


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
pict.grid(row=3, column=3, padx=20, pady=20)

rct = pict.create_rectangle(100, 100, 150, 150, fill='red')
root.bind('<KeyPress>', move_rct)
#pict.coords(rct, 0, 0, 50, 50)

menu = ctk.CTkOptionMenu(master=root)
menu.configure(anchor='center', values=['Светлый', 'Тёмный'], font=ctk.CTkFont(family='Arial', size=20, weight='bold', slant='italic'), command=om)
menu.set('Тема фона')
menu.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

btn2 = ctk.CTkButton(master=root)
btn2.configure(text="Create", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press2)
btn2.grid(row=1, column=3, padx=20, pady=20, sticky="ew")

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Delete", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn1.grid(row=2, column=3, padx=20, pady=20, sticky="ew")
btn1.bind('<Double-Button-1>', change)

root.mainloop()
