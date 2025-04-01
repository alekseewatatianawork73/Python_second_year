import customtkinter as ctk
count = 0


def press2():
    file = open('note.txt', 'r+', encoding='UTF-8')
    notes = file.readlines()
    txt_output.configure(state='normal')
    txt_output.delete(0.0, 'end')
    for i in range(len(notes) - 1, -1, -1):
        txt_output.insert(0.0, f'{i+1}. {notes[i]}\n')
    file.close()
    txt_output.configure(state='disabled')


def press3():
    txt_output.configure(state='normal')
    txt_output.delete(0.0, 'end')
    txt_output.configure(state='disabled')


def press4():
    file = open('note.txt', 'w')
    file.close()


def press_add(note, mssg):
    global count
    file = open('note.txt', 'a+', encoding='UTF-8')
    file.write(note.get() + '\n')
    file.close()
    count += 1
    mssg.configure(text=f'Добавлено {count} заметок.')
    note.delete(0, 'end')


def press1():
    window = ctk.CTkToplevel()
    window.title('Режим редактирования')
    window.geometry('900x500')
    window.configure(fg_color='lightblue')
    r, c = 7, 7
    for i in range(r):
        window.rowconfigure(index=i, weight=1)
    for i in range(c):
        window.columnconfigure(index=i, weight=1)
    lbl1 = ctk.CTkLabel(master=window)
    lbl1.configure(text='Введите заметку:',
                   font=ctk.CTkFont(family='Arial', size=20, weight='bold', slant='italic'))
    lbl1.grid(row=0, column=3, padx=20, pady=20, sticky="ew")
    new_note = ctk.CTkEntry(master=window)
    new_note.configure(justify='center', border_width=3, border_color='darkblue',
                       font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
    new_note.grid(row=1, column=3, padx=20, pady=20, sticky="nsew")
    mssg = ctk.CTkLabel(master=window)
    mssg.configure(text=f'Добавлено {count} заметок.',
                   font=ctk.CTkFont(family='Arial', size=20, weight='bold', slant='italic'))
    mssg.grid(row=5, column=3, padx=20, pady=15, sticky="ew")
    btn = ctk.CTkButton(master=window)
    btn.configure(text="Добавить", fg_color='darkblue', hover_color='grey',
                  font=ctk.CTkFont(family='Arial', size=15, weight='bold'),
                  command=lambda: press_add(new_note, mssg))
    btn.grid(row=2, column=3, padx=20, pady=20, sticky="ew")


root = ctk.CTk()
root.title("Блокнот с заметками")
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

menu = ctk.CTkLabel(master=root)
menu.configure(text='Редактор заметок', font=ctk.CTkFont(family='Arial', size=25, weight='bold', slant='italic'))
menu.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

lbl = ctk.CTkLabel(master=frm)
lbl.configure(text='Мои заметки', text_color='white', font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
lbl.grid(row=0, column=3, padx=10, pady=10, sticky='nsew')

txt_output = ctk.CTkTextbox(master=frm)
txt_output.configure(font=ctk.CTkFont(family='Arial', size=15, weight='bold'), fg_color='white',
                     wrap='word', state='disabled', border_color='darkgreen', border_width=2)
txt_output.grid(row=1, column=3, padx=10, pady=10, sticky='nsew')

btn2 = ctk.CTkButton(master=frm)
btn2.configure(text="Посмотреть заметки", text_color='black', fg_color='lightgreen', hover_color='lightgrey', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press2)
btn2.grid(row=2, column=3, padx=20, pady=20, sticky="nsew")
btn4 = ctk.CTkButton(master=frm)
btn4.configure(text="Удалить все заметки", text_color='black', fg_color='lightgreen', hover_color='lightgrey', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press4)
btn4.grid(row=4, column=3, padx=20, pady=20, sticky="nsew")
btn3 = ctk.CTkButton(master=frm)
btn3.configure(text="Скрыть заметки", text_color='black', fg_color='lightgreen', hover_color='lightgrey', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press3)
btn3.grid(row=3, column=3, padx=20, pady=20, sticky="nsew")

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Добавить заметки", fg_color='darkgreen', hover_color='green', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn1.grid(row=4, column=3, padx=20, pady=20, sticky="nsew")

root.mainloop()
