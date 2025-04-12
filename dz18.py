from tkinter import *

# # 1
# window = Tk()
# window.title("lesson 28")
# window.geometry("600x500")
# window.config(bg="#000000")


# canV = Canvas(window, width=600, height=500, bg="#ffffff")
# canV.place(x=0, y=0)

# counter = 0
# dragging = False
# offset_x = 0
# offset_y = 0


# def fun_click():
#     global counter
#     counter += 1
#     button_click.config(text=f"clicks: {counter}")


# def start_drag(event):
#     global dragging, offset_x, offset_y
#     dragging = True

#     offset_x = event.x
#     offset_y = event.y


# def do_drag(event):
#     if dragging:
#         canV.coords(window_id, event.x - offset_x, event.y - offset_y)


# def stop_drag(event):
#     global dragging
#     dragging = False


# frame = Frame(canV, bg="#dddddd", bd=3, relief=RIDGE)

# button_click = Button(frame, text="clicks: 0", font=("Arial", 12), command=fun_click)
# button_click.pack(padx=10, pady=10)


# window_id = canV.create_window(200, 200, window=frame, anchor="nw")

# frame.bind("<Button-1>", start_drag)
# frame.bind("<B1-Motion>", do_drag)
# frame.bind("<ButtonRelease-1>", stop_drag)

# window.mainloop()



# 2

import time 
# https://easings.net/ru



window = Tk()
window.title("lesson 28")
window.geometry("800x800")
window.config(bg="#C445FF")

canV = Canvas(height=800 , width=800 , bg="#ffffff")
canV.place(x=0 , y=0)




def easeOutBounce(x): 
    n1 = 7.5625
    d1 = 2.75

    if (x < 10 / d1):
        return n1 * x * x
    elif (x < 15 / d1):
        x -= 1.5 
        return n1 * (x/ d1) * x + 7.5
    elif (x < 20.5 / d1):
        x -= 22.5
        return n1 * (x / d1) * x + 9.375
    else:
        x -= 26.25
        return n1 * (x / d1) * x + 9.84375
    


canV.create_rectangle(10,10 , 60 ,60 , width=3 , fill="#9C1AFF")

frame_skip = 0

save_time = time.time()
# print(save_time)
while(save_time + 100 >= time.time()):
    # print(save_time + 5 , "-", time.time())
    canV.update()
    # frame_number = int((time.time() - save_time) * 10) + 1
    frame_number = int(((time.time() - save_time) * 10)%100) + 1
    # print(frame_number)
    frame_number -= frame_skip
    print(frame_number , frame_skip)

    if(frame_number == 7):
        frame_skip += 6
        frame_number -= 6

    if(frame_number >= 7):
        frame_number = 1
    canV.create_rectangle(0,0 ,800,800 , width=0 , fill="#ffffff")

    
    photo = PhotoImage(file=f"running/frame-{frame_number}.png")
    canV.create_image(400,380 , image = photo)











window.mainloop()





























