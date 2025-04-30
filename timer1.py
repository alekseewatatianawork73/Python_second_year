import time
import customtkinter as ctk
root = ctk.CTk()
root.title("Задание")
root.geometry("1000x700")
second = 0


def timer(entry, btn1_2):
    global second
    k = int(entry.get()) + 1
    second = 0
    while k:
        btn1_2.configure(text=f"Секунд прошло: {second}")
        btn1_2.update()
        time.sleep(1)
        second += 1
        k -= 1





def press1():
    global second
    window = ctk.CTkToplevel(root)
    window.title('Задание_1')
    window.geometry('500x500')

    rows, columns = 7, 7
    for i in range(rows):
        window.rowconfigure(index=i, weight=1)
    for i in range(columns):
        window.columnconfigure(index=i, weight=1)

    btn1_1 = ctk.CTkLabel(master=window)
    btn1_1.configure(text="Таймер", font=ctk.CTkFont(family='Arial', size=24, weight='bold'))
    btn1_1.grid(row=0, column=2, sticky="ew")

    btn1_2 = ctk.CTkLabel(master=window)
    btn1_2.configure(text=f"Секунд прошло: {second}", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
    btn1_2.grid(row=1, column=1, sticky="ew")

    entr = ctk.CTkEntry(master=window)
    entr.configure(placeholder_text='Введите секунд', justify="center", state="normal", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
    entr.grid(row=5, column=1, sticky="ew")

    btn1_3 = ctk.CTkButton(master=window)
    btn1_3.configure(text="Начать отсчет", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=lambda: timer(entr, btn1_2))
    btn1_3.grid(row=5, column=2, padx=20, pady=20, sticky="ew")


rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

btn1 = ctk.CTkLabel(master=root)
btn1.configure(text="Выбор задач", font=ctk.CTkFont(family='Arial', size=24, weight='bold'))
btn1.grid(row=0, column=3, sticky="ew")

btn2 = ctk.CTkButton(master=root)
btn2.configure(text="Таймер", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn2.grid(row=3, column=3,sticky="ew")



root.mainloop()
