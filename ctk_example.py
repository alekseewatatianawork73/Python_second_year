# импортируем библиотеку
import customtkinter as ctk


def press_btn():
    s = entr1.get()
    entr2.configure(state="normal")
    entr2.delete(0, "end")
    entr2.insert(0, s.upper())
    entr2.configure(state="disabled")

    
def press_btn2():
    s = entr1.get()
    entr2.configure(state="normal")
    entr2.delete(0, "end")
    entr2.insert(0, s.lower())
    entr2.configure(state="disabled")


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
lbl.configure(text='Преобразователь строк', font=ctk.CTkFont(family='Arial', size=25, weight='bold', slant='italic'))
lbl.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

entr1 = ctk.CTkEntry(master=root)
entr1.configure(justify="center", state="normal")
entr1.grid(row=2, column=2, padx=20, pady=20, sticky="nsew")

entr2 = ctk.CTkEntry(master=root)
entr2.configure(justify="center", state="disabled")
entr2.grid(row=2, column=4, padx=20, pady=20, sticky="nsew")

btn = ctk.CTkButton(master=root)
btn.configure(text="Преобразовать в верхний регистр", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press_btn)
btn.grid(row=3, column=3, padx=20, pady=20, sticky="ew")

btn = ctk.CTkButton(master=root)
btn.configure(text="Преобразовать в нижний регистр", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press_btn2)
btn.grid(row=4, column=3, padx=20, pady=20, sticky="ew")

# запускаем бесконечный цикл для отображения окна
root.mainloop()
