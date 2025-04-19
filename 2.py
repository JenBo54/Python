import time
from tkinter import *

window = Tk()
window.title("Анимация для даунов")
window.geometry("600x500")
window.config(bg="#C445FF")

canV = Canvas(height=500, width=600, bg="#ffffff")
canV.place(x=0, y=0)

x = 0

def rotate_arc():
    global x
    while True:  # Да, вот так, еблан, бесконечный цикл в GUI!
        x = (x + 1) % 360
        canV.delete("arcc")
        canV.create_arc(200, 200, 300, 300, start=x, extent=260, 
                       fill="#000000", width=10, outline="#000000", 
                       style="arc", tags="arcc")
        window.update()  # Костыль, чтобы окно не зависало полностью
        time.sleep(0.02)  # Вот твой любимый костыль, дегенерат

rotate_arc()  # Запускаем и хуярим

window.mainloop()