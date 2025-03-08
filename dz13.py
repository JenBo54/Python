from tkinter import *
from tkinter import ttk


# window = Tk()
# window.title("game")
# window.geometry("700x500")
# window.config(bg="#0b138c")



# lab_text_1 = Label(text="1) сколько будет 2+2?" , bg="#0b138c", fg="#ffffff" , font=["Arial Black" , 15])
# lab_text_1.place(x= 230 , y=190)



# def fun_1():
#     print(value_radio.get())
#     if(value_radio.get() == "b01"):

#         lab_text_1.config(text="2) сколько лет 10 летнему мальчику?")
#         check_1.config(command= fun_2)
#         check_2.config(command= fun_2)
#         check_3.config(command= fun_2)
#         check_4.config(command= fun_2)
#         check_1.config(text= "9")
#         check_2.config(text= "10")
#         check_3.config(text= "8")
#         check_4.config(text= "7")
#     elif(value_radio.get() == "b02"):
#         lab_text_1.config(text="ответ неверный")
#         check_1.config(value=None)
#         check_2.config(value=None)
#         check_3.config(value=None)
#         check_4.config(value=None)
#     elif(value_radio.get() == "b03"):
#         lab_text_1.config(text="ответ неверный")
#         check_1.config(value=None)
#         check_2.config(value=None)
#         check_3.config(value=None)
#         check_4.config(value=None)
#     elif(value_radio.get() == "b04"):
#         lab_text_1.config(text="ответ неверный")
#         check_1.config(value=None)
#         check_2.config(value=None)
#         check_3.config(value=None)
#         check_4.config(value=None)



# def fun_2():
#     print(value_radio.get())
#     if(value_radio.get() == "b02"):
#         lab_text_1.config(text="3) почему?")
#         check_1.config(command= fun_3)
#         check_2.config(command= fun_3)
#         check_3.config(command= fun_3)
#         check_4.config(command= fun_3)
#         check_1.config(text= "1")
#         check_2.config(text= "да")
#         check_3.config(text= "нет")
#         check_4.config(text= "потому что")
#     elif(value_radio.get() == "b01"):
#         lab_text_1.config(text="ответ неверный")
#         check_1.config(value=None)
#         check_2.config(value=None)
#         check_3.config(value=None)
#         check_4.config(value=None)
#     elif(value_radio.get() == "b03"):
#         lab_text_1.config(text="ответ неверный")
#         check_1.config(value=None)
#         check_2.config(value=None)
#         check_3.config(value=None)
#         check_4.config(value=None)
#     elif(value_radio.get() == "b04"):
#         lab_text_1.config(text="ответ неверный")
#         check_1.config(value=None)
#         check_2.config(value=None)
#         check_3.config(value=None)
#         check_4.config(value=None)    


# def fun_3():
#     print(value_radio.get())
#     if(value_radio.get() == "b04"):
#         lab_text_1.config(text="4) да?")
#         check_1.config(command= fun_4)
#         check_2.config(command= fun_4)
#         check_3.config(command= fun_4)
#         check_4.config(command= fun_4)
#         check_1.config(text= "2")
#         check_2.config(text= "да(нет)")
#         check_3.config(text= "да")
#         check_4.config(text= "нет")
#     elif(value_radio.get() == "b01"):
#         lab_text_1.config(text="ответ неверный")
#         check_1.config(value=None)
#         check_2.config(value=None)
#         check_3.config(value=None)
#         check_4.config(value=None)
#     elif(value_radio.get() == "b03"):
#         lab_text_1.config(text="ответ неверный")
#         check_1.config(value=None)
#         check_2.config(value=None)
#         check_3.config(value=None)
#         check_4.config(value=None)
#     elif(value_radio.get() == "b02"):
#         lab_text_1.config(text="ответ неверный")
#         check_1.config(value=None)
#         check_2.config(value=None)
#         check_3.config(value=None)
#         check_4.config(value=None)  



# def fun_4():
#     print(value_radio.get())
#     if(value_radio.get() == "b03"):
#         lab_text_1.config(text="krassava")
#     else:
#         lab_text_1.config(text="loh")

    





# value_radio = StringVar()


# check_1 = ttk.Radiobutton(text="4(да)" , variable=value_radio , value="b01" , command= fun_1)
# check_1.place(x=10 , y=10)

# check_2 = ttk.Radiobutton(text="4(нет)" , variable=value_radio , value="b02" , command= fun_1)
# check_2.place(x=10 , y=50)

# check_3 = ttk.Radiobutton(text="да(нет)" , variable=value_radio , value="b03" , command= fun_1)
# check_3.place(x=10 , y=90)

# check_4 = ttk.Radiobutton(text="нет(да)" , variable=value_radio , value="b04" , command= fun_1)
# check_4.place(x=10 , y=130)

# window.mainloop()




# 2

window = Tk()
window.title("Перекрестье")
window.geometry("700x500")
window.config(bg="#b3b8ff")

lab_hor = Label(window, bg="white", width=30, height=1)
lab_hor.place(x=200, y=250)

lab_ver = Label(window, bg="white", width=1, height=10)
lab_ver.place(x=350, y=150)

scale_hor = Scale(window, from_=100, to=600, orient=HORIZONTAL, label="Горизонтальная", bg="#0b138c", fg="white")
scale_hor.place(x=200, y=400)

scale_ver = Scale(window, from_=50, to=400, orient=VERTICAL, label="Вертикальная", bg="#0b138c", fg="white")
scale_ver.place(x=50, y=100)

def fun_1():
    lab_hor.place(x=scale_hor.get(), y=250)
    lab_ver.place(x=350, y=scale_ver.get())

def fun_2():
    acc_x = 100 - abs(scale_hor.get() - 350) / 3.5
    acc_y = 100 - abs(scale_ver.get() - 250) / 2.5
    accuracy = (acc_x + acc_y) / 2
    lab_result.config(text=f"Точность: {accuracy:.2f}%")

but_update = Button(window, text="Обновить", command=fun_1, bg="#ffffff")
but_update.place(x=300, y=450)

but_check = Button(window, text="Зафиксировать", command=fun_2, bg="#ffffff")
but_check.place(x=400, y=450)

lab_result = Label(window, text="Точность: 100%", bg="#0b138c", fg="white", font=["Arial Black", 15])
lab_result.place(x=280, y=50)

window.mainloop()












































