import customtkinter as ctk
import random

#func
def press1():
    global count, m
    def cl(yc):
        yc.configure(text='X', state='disabled', text_color_disabled='white')
        btnsc.remove(yc)
        m[btns.index(yc)] = 1

        if bool(btnsc):
            bc = random.choice(btnsc)
            bc.configure(text='O', state='disabled', text_color_disabled='white')
            btnsc.remove(bc)
            m[btns.index(bc)] = 0
        if (m[0]==m[3]==m[6] or m[0]==m[4]==m[8] or m[0]==m[1]==m[2]) and m[0] == 1 or (m[1]==m[4]==m[7] or m[3]==m[4]==m[5]
            or m[2]==m[4]==m[6]) and m[4] == 1 or (m[2]==m[8]==m[5] or m[6]==m[7]==m[8]) and m[8] == 1:
            ito = 'ПОБЕДА'
            for i in btnsc:
                i.configure(state='disabled')
        elif (m[0]==m[3]==m[6] or m[0]==m[4]==m[8] or m[0]==m[1]==m[2]) and m[0] == 0 or (m[1]==m[4]==m[7] or m[3]==m[4]==m[5]
            or m[2]==m[4]==m[6]) and m[4] == 0 or (m[2]==m[8]==m[5] or m[6]==m[7]==m[8]) and m[8] == 0:
                ito = 'ПОРАЖЕНИЕ'
                for i in btnsc:
                    i.configure(state='disabled')

        lblv = ctk.CTkLabel(master=window)
        lblv.configure(text=f'{ito}', font=ctk.CTkFont(family='Arial', size=17, slant='italic'))
        lblv.grid(row=4, column=3, padx=20, pady=20, sticky="ew")

    m = [None] * 9

    count = 0
    el = None
    window = ctk.CTkToplevel(root)
    window.geometry('400x400')
    window.configure(bg='black')
    window.title("крестики-нолики")
    root.title("xexexexexexexe")
    r, c = 7, 7
    for i in range(r):
        window.rowconfigure(index=i, weight=1)
    for i in range(c):
        window.columnconfigure(index=i, weight=1)

    btns = [ctk.CTkButton(master=window) for _ in range(9)]
    btns[0].configure(text=f'', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=lambda: cl(btns[0]), fg_color='red')
    btns[0].grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    btns[1].configure(text=f'', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=lambda: cl(btns[1]), fg_color='red')
    btns[1].grid(row=1, column=2, padx=10, pady=10, sticky="ew")
    btns[2].configure(text=f'', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=lambda: cl(btns[2]), fg_color='red')
    btns[2].grid(row=1, column=3, padx=10, pady=10, sticky="ew")
    btns[3].configure(text=f'', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=lambda: cl(btns[3]), fg_color='red')
    btns[3].grid(row=2, column=1, padx=10, pady=10, sticky="ew")
    btns[4].configure(text=f'', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=lambda: cl(btns[4]), fg_color='red')
    btns[4].grid(row=2, column=2, padx=10, pady=10, sticky="ew")
    btns[5].configure(text=f'', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=lambda: cl(btns[5]), fg_color='red')
    btns[5].grid(row=2, column=3, padx=10, pady=10, sticky="ew")
    btns[6].configure(text=f'', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=lambda: cl(btns[6]), fg_color='red')
    btns[6].grid(row=3, column=1, padx=10, pady=10, sticky="ew")
    btns[7].configure(text=f'', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=lambda: cl(btns[7]), fg_color='red')
    btns[7].grid(row=3, column=2, padx=10, pady=10, sticky="ew")
    btns[8].configure(text=f'', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=lambda: cl(btns[8]), fg_color='red')
    btns[8].grid(row=3, column=3, padx=10, pady=10, sticky="ew")
    btnsc = btns.copy()







def press2():

    window = ctk.CTkToplevel(root)
    window.geometry('400x400')
    window.configure()
    window.title("камень-ножницы-бумага")
    root.title("xaxaxaxaxaxa")
    r, c = 7, 7
    for i in range(r):
        window.rowconfigure(index=i, weight=1)
    for i in range(c):
        window.columnconfigure(index=i, weight=1)

    lblv = ctk.CTkLabel(master=window)
    lblv.configure(text='Выберите', font=ctk.CTkFont(family='Arial', size=25, weight='bold', slant='italic'))
    lblv.grid(row=0, column=3, padx=20, pady=20, sticky="ew")
    c1, c2, c3 = 'камень', 'ножницы', 'бумага'
    #vibor
    c1, c2, c3 = 'камень', 'ножницы', 'бумага'
    btnk = ctk.CTkButton(master=window)
    btnk.configure(text='камень', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=lambda: choice(c1),fg_color='red')
    btnk.grid(row=1, column=3, padx=10, pady=10, sticky="ew")
    btnn = ctk.CTkButton(master=window)
    btnn.configure(text='ножницы', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=lambda: choice(c2),fg_color='red')
    btnn.grid(row=2, column=3, padx=10, pady=10, sticky="ew")
    btnb = ctk.CTkButton(master=window)
    btnb.configure(text='бумага', font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=lambda: choice(c3),fg_color='red')
    btnb.grid(row=3, column=3, padx=10, pady=10, sticky="ew")
    c1, c2, c3 = 'камень', 'ножницы', 'бумага'

    def choice(n):
        cho = ['камень', 'ножницы', 'бумага']
        yc = n
        bc = random.choice(cho)

        if bc == yc:
            itog = 'nicha'
        elif (bc == 'камень' and yc == 'бумага') or (bc == 'ножницы' and yc == 'камень') or (bc == 'бумага' and yc == 'ножницы'):
            itog = 'pobeda'
        else:
            itog = 'proigris'


        lblv = ctk.CTkLabel(master=window)
        lblv.configure(text=f'вы выбрали {yc.upper()}\n противник выбрал {bc.upper()}\nИтог: {itog.upper()}',
                       font=ctk.CTkFont(family='Arial', size=17, slant='italic'))
        lblv.grid(row=4, column=3, padx=20, pady=20, sticky="ew")



def press3():
    window = ctk.CTkToplevel(root)
    window.geometry('400x400')
    window.configure()
    window.title("Мемори")
    root.title("xyxyxyxyxyxyxy")
    r, c = 7, 7
    for i in range(r):
        window.rowconfigure(index=i, weight=1)
    for i in range(c):
        window.columnconfigure(index=i, weight=1)




####
root = ctk.CTk()
root.title("Games")
root.geometry("500x500")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)
####
#nazvanie
lbl = ctk.CTkLabel(master=root)
lbl.configure(text= 'Выберите игру', font=ctk.CTkFont(family='Arial', size=25, weight='bold', slant='italic'))
lbl.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

#knopki
btn11 = ctk.CTkButton(master=root)
btn11.configure(text="крестики-нолики", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1, fg_color='red')
btn11.grid(row=3, column=3, padx=10, pady=10, sticky="ew")
btn22 = ctk.CTkButton(master=root)
btn22.configure(text="камень-ножницы-бумага", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press2, fg_color='red')
btn22.grid(row=4, column=3, padx=10, pady=10, sticky="ew")
btn33 = ctk.CTkButton(master=root)
btn33.configure(text="Мемори", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press3, fg_color='red')
btn33.grid(row=5, column=3, padx=10, pady=10, sticky="ew")



root.mainloop()
