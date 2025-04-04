# Теория: метод after(), классы CtkSwitch(), CtkSlider(), добавление звука
import customtkinter as ctk
from pygame import mixer
mixer.init()  # не забывайте инициализировать модули при использовании pygame

# загрузка звукового файла
mixer.music.load('audio.mp3')


def press1():
    # удаляем текстовую метку
    lbl1.grid_forget()
    # ждём 3 секунды (3000 мс) и снова возвращаем текстовую метку на экран
    root.after(3000, lambda: lbl1.grid(row=1, column=3, padx=10, pady=10, sticky='nsew'))
    # синтаксис: [окно, фрейм, окно toplevel].afler([время ожидания в мс],[функция, которую необходимо выполнить])


def press2():
    # воспроизводим звуковой файл
    mixer.music.play(-1)


def press3():
    # приостанавливаем воспроизведение
    mixer.music.stop()


def sld(value):
    # value - значение на слайдере (дробное число!), округляем при помощи функций int() или round()
    lbl1.configure(text=f'{round(value)}')


def sw_comm():
    # sw_var.get() - возвращает значение переключателя (True или False)
    if sw_var.get():
        sw.configure(text='on')
    else:
        sw.configure(text='off')


root = ctk.CTk()
root.title("Моё приложение")
root.geometry("1000x500")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

lbl1 = ctk.CTkLabel(master=root)
lbl1.configure(text=f'Text', font=ctk.CTkFont(family='Arial', size=30, weight='bold'))
lbl1.grid(row=1, column=3, padx=10, pady=10, sticky='nsew')

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Удалить текст на 3 секунды", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn1.grid(row=4, column=3, padx=20, pady=20, sticky="nsew")

btn2 = ctk.CTkButton(master=root)
btn2.configure(text="Включить звук", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press2)
btn2.grid(row=5, column=2, padx=20, pady=20, sticky="nsew")

btn3 = ctk.CTkButton(master=root)
btn3.configure(text="Выключить звук", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press3)
btn3.grid(row=5, column=4, padx=20, pady=20, sticky="nsew")

# создание слайдера slider
slider = ctk.CTkSlider(master=root)
slider.configure(from_=1, to=50, number_of_steps=50, fg_color='darkorange', button_color='darkred',
                           progress_color='red2', button_hover_color='coral', command=sld)
slider.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky="ew")

# создание переключателя switch
sw = ctk.CTkSwitch(master=root)
sw_var = ctk.BooleanVar(value=False)  # значение по умолчанию (True - вкл, False - выкл)
sw.configure(text='off', variable=sw_var, font=ctk.CTkFont(family='Arial', size=20, weight='bold'), command=sw_comm,
                 fg_color='yellow', button_color='yellow4', progress_color='yellow3', button_hover_color='lightgrey')
sw.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

root.mainloop()
