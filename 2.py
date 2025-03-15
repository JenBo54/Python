from tkinter import *

window = Tk()
window.title("lesson 21")
window.geometry("700x500")
window.config(bg="#f4ffad")

obj = {}

# Глобальные переменные для хранения полей ввода
entry_1 = None
entry_2 = None

def fun_b_1():
    global entry_1, entry_2  # Используем глобальные переменные
    if entry_1:
        text = entry_1.get()
        if text == "1":
            obj[20] = text
            print(obj)
        else:
            print("error")

def fun_1():
    global entry_1, entry_2  # Используем глобальные переменные

    entry_1 = Entry(bg="#005d9b", fg="#ffffff", font=["Yu Gothic UI Light", 15])
    entry_1.place(x=180, y=75, width=180)

    entry_2 = Entry(bg="#005d9b", fg="#ffffff", font=["Yu Gothic UI Light", 15])
    entry_2.place(x=180, y=145, width=180)

    lab_text_1 = Label(text="Введите товар", bg="#f4ffad", fg="#005d9b", font=["Yu Gothic UI Light", 15])
    lab_text_1.place(x=10, y=70)

    lab_text_2 = Label(text="Введите кол-во", bg="#f4ffad", fg="#005d9b", font=["Yu Gothic UI Light", 15])
    lab_text_2.place(x=10, y=140)

    button_1 = Button(text="but 1", command=fun_b_1)
    button_1.place(x=30, y=200)

# Создание меню
all_menu = Menu(tearoff=0)
num_radio = IntVar()
all_menu.add_radiobutton(label="b1", variable=num_radio, value=1, command=fun_1)
all_menu.add_separator()
all_menu.add_radiobutton(label="b2", variable=num_radio, value=2)
all_menu.add_separator()
all_menu.add_radiobutton(label="b3", variable=num_radio, value=3)

main_menu = Menu()
main_menu.add_cascade(label="all_menu", menu=all_menu)

window.config(menu=main_menu)
window.mainloop()