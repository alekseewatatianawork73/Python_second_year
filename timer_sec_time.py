import time
import customtkinter as ctk
from datetime import datetime
root = ctk.CTk()
root.title("Задание")
root.geometry("1000x700")
second = 0
hour = 0
mins = 0
second_s, hour_s, mins_s = 0, 0, 0
running = True



def timer(entry, btn1_2,btn1_4,btn1_5,btn1_6):
    global second, hour, mins
    k = int(entry.get())  # начальное количество секунд, которое задал пользователь
    # установили значение на единицу больше, чтобы цикл не закончился раньше времени
    second = k  # текущее количество секунд
    while second + 1:
        hour = second // 3600
        mins = (second % 3600) // 60
        s = (second % 3600) % 60

        btn1_2.configure(text=f"Секунд прошло: {s}")  # меняем надпись
        btn1_2.update()  # обновляем виджет с надписью

        btn1_4.configure(text=f"Минут прошло: {mins}")  # меняем надпись
        btn1_4.update()  # обновляем виджет с надписью

        btn1_5.configure(text=f"Часов прошло: {hour}")  # меняем надпись
        btn1_5.update()  # обновляем виджет с надписью

        time.sleep(1)  # ждём одну секунду
        second -= 1  # увличиваем текущее количество секунд
        k -= 1  # уменьшаем заданное начальное количество секунд
        # когда k достигнет нуля, цикл while завершится

        if second <= 0:
            btn1_6.grid(row=0, column=2, sticky="ew")
        else:
            btn1_6.grid_forget()


def secondomer(btn1_2_s,btn1_4_s,btn1_5_s, con=False):
    global second_s, hour_s, mins_s, running
    if not con:
        second_s = 0  # текущее количество секунд
    while running:
        hour_s = second_s // 3600
        mins_s = (second_s % 3600) // 60
        s = second_s % 60

        btn1_2_s.configure(text=f"Секунд прошло: {s}")  # меняем надпись
        btn1_2_s.update()  # обновляем виджет с надписью

        btn1_4_s.configure(text=f"Минут прошло: {mins}")  # меняем надпись
        btn1_4_s.update()  # обновляем виджет с надписью

        btn1_5_s.configure(text=f"Часов прошло: {hour}")  # меняем надпись
        btn1_5_s.update()  # обновляем виджет с надписью

        time.sleep(1)  # ждём одну секунду
        second_s += 1  # увличиваем текущее количество секунд

def stop():
    global running
    running = False

def cont(btn1_2_s, btn1_4_s, btn1_5_s):
    global running
    running = True
    secondomer(btn1_2_s, btn1_4_s, btn1_5_s, con=True)


def vreme():
    time = datetime.now().strftime("%H:%M:%S")
    btn1_2.configure(text=f"Текущее время: {time}")
    win.after(100, vreme)






def press2():
    global second
    window = ctk.CTkToplevel(root)
    window.title('Задание_2')
    window.geometry('500x500')

    rows, columns = 7, 7
    for i in range(rows):
        window.rowconfigure(index=i, weight=1)
    for i in range(columns):
        window.columnconfigure(index=i, weight=1)

    btn1_1 = ctk.CTkLabel(master=window)
    btn1_1.configure(text="Таймер", font=ctk.CTkFont(family='Arial', size=24, weight='bold'))
    btn1_1.grid(row=0, column=1, sticky="ew")

    btn1_6 = ctk.CTkLabel(master=window)
    btn1_6.configure(text="Таймер закончился", font=ctk.CTkFont(family='Arial', size=24, weight='bold'))


    btn1_2 = ctk.CTkLabel(master=window)
    btn1_2.configure(text=f"Секунд прошло: {second}", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
    btn1_2.grid(row=1, column=1, sticky="ew")


    btn1_4 = ctk.CTkLabel(master=window)
    btn1_4.configure(text=f"Минут прошло: {mins}", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
    btn1_4.grid(row=2, column=1, sticky="ew")

    btn1_5 = ctk.CTkLabel(master=window)
    btn1_5.configure(text=f"Часов прошло: {hour}", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
    btn1_5.grid(row=3, column=1, sticky="ew")

    entr = ctk.CTkEntry(master=window)
    entr.configure(placeholder_text='Введите секунд', justify="center", state="normal", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
    entr.grid(row=5, column=1, sticky="ew")

    btn1_3 = ctk.CTkButton(master=window)
    btn1_3.configure(text="Начать отсчет", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=lambda: timer(entr, btn1_2,btn1_4,btn1_5,btn1_6))
    btn1_3.grid(row=5, column=2, padx=20, pady=20, sticky="ew")



def press3():
    window = ctk.CTkToplevel(root)
    window.title('Задание_3')
    window.geometry('500x500')

    rows, columns = 7, 7
    for i in range(rows):
        window.rowconfigure(index=i, weight=1)
    for i in range(columns):
        window.columnconfigure(index=i, weight=1)

    btn1_1 = ctk.CTkLabel(master=window)
    btn1_1.configure(text="Секундомер", font=ctk.CTkFont(family='Arial', size=24, weight='bold'))
    btn1_1.grid(row=0, column=1, sticky="ew")

    btn1_2_s = ctk.CTkLabel(master=window)
    btn1_2_s.configure(text=f"Секунд прошло: {second_s}", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
    btn1_2_s.grid(row=1, column=1, sticky="ew")

    btn1_4_s = ctk.CTkLabel(master=window)
    btn1_4_s.configure(text=f"Минут прошло: {mins_s}", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
    btn1_4_s.grid(row=2, column=1, sticky="ew")

    btn1_5_s = ctk.CTkLabel(master=window)
    btn1_5_s.configure(text=f"Часов прошло: {hour_s}", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
    btn1_5_s.grid(row=3, column=1, sticky="ew")

    btn1_3_s = ctk.CTkButton(master=window)
    btn1_3_s.configure(text="Начать отсчет", font=ctk.CTkFont(family='Arial', size=15, weight='bold'),
                       command=lambda: secondomer(btn1_2_s, btn1_4_s, btn1_5_s))
    btn1_3_s.grid(row=5, column=1, padx=20, pady=20, sticky="ew")

    btn1_7_s = ctk.CTkButton(master=window)
    btn1_7_s.configure(text="Стоп", font=ctk.CTkFont(family='Arial', size=15, weight='bold'),
                      command=stop)
    btn1_7_s.grid(row=5, column=2, padx=20, pady=20, sticky="ew")

    btn1_8_s = ctk.CTkButton(master=window)
    btn1_8_s.configure(text="Продолжить", font=ctk.CTkFont(family='Arial', size=15, weight='bold'),
                       command=lambda: cont(btn1_2_s, btn1_4_s, btn1_5_s))
    btn1_8_s.grid(row=5, column=3, padx=20, pady=20, sticky="ew")


def press1():
    global win, btn1_2
    win = ctk.CTkToplevel(root)
    win.title('Задание_1')
    win.geometry('500x500')

    rows, columns = 7, 7
    for i in range(rows):
        win.rowconfigure(index=i, weight=1)
    for i in range(columns):
        win.columnconfigure(index=i, weight=1)

    btn1_1 = ctk.CTkLabel(master=win)
    btn1_1.configure(text="Время", font=ctk.CTkFont(family='Arial', size=24, weight='bold'))
    btn1_1.grid(row=0, column=1, sticky="ew")

    btn1_2 = ctk.CTkLabel(master=win, text="", font=ctk.CTkFont(family='Arial', size=24, weight='bold'))
    btn1_2.grid(row=1, column=1, sticky="ew")
    vreme()


rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

btn1 = ctk.CTkLabel(master=root)
btn1.configure(text="Выбор задач", font=ctk.CTkFont(family='Arial', size=24, weight='bold'))
btn1.grid(row=0, column=3, sticky="ew")

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Время", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn1.grid(row=3, column=1, sticky="ew")

btn2 = ctk.CTkButton(master=root)
btn2.configure(text="Таймер", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press2)
btn2.grid(row=3, column=3, sticky="ew")

btn3 = ctk.CTkButton(master=root)
btn3.configure(text="Секундомер", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press3)
btn3.grid(row=3, column=5, sticky="ew")

root.mainloop()
