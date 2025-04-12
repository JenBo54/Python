from tkinter import *

# 1 — основное окно
window = Tk()
window.title("lesson 28")
window.geometry("600x500")
window.config(bg="#000000")

# 2 — канвас
canV = Canvas(window, width=600, height=500, bg="#ffffff")
canV.place(x=0, y=0)

# 3 — переменные
counter = 0
dragging = False
start_x = 0
start_y = 0

# 4 — функция увеличения счётчика
def fun_click():
    global counter
    counter += 1
    button_click.config(text=f"clicks: {counter}")

# 5 — обработка начала перетаскивания
def start_drag(event):
    global dragging, start_x, start_y
    dragging = True
    start_x = event.x
    start_y = event.y

# 6 — обработка движения
def do_drag(event):
    global dragging, start_x, start_y
    if dragging:
        dx = event.x - start_x
        dy = event.y - start_y
        canV.move(window_id, dx, dy)

# 7 — окончание перетаскивания
def stop_drag(event):
    global dragging
    dragging = False

# 8 — создаём отдельное "окно" в canvas
frame = Frame(canV, bg="#dddddd", bd=3, relief=RIDGE)

button_click = Button(frame, text="clicks: 0", font=("Arial", 12), command=fun_click)
button_click.pack(padx=10, pady=10)

# 9 — добавляем frame в canvas
window_id = canV.create_window(200, 200, window=frame, anchor="nw")

# 10 — привязка событий
canV.tag_bind(window_id, "<Button-1>", start_drag)
canV.tag_bind(window_id, "<B1-Motion>", do_drag)
canV.tag_bind(window_id, "<ButtonRelease-1>", stop_drag)

# 11 — запускаем окно
window.mainloop()