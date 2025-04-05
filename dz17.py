from tkinter import *

# 1

window = Tk()
window.geometry("600x500")
window.config(bg="#000000")


canV = Canvas(window, width=600, height=500, bg="#ffffff")
canV.place(x=0, y=0)


entry = Entry(window, font=("Arial", 16), bg="#d0d0d0", fg="#000000", justify="center")
entry.place(x=150, y=30, width=300, height=30)


def update_text(event):
    text = entry.get()
    canV.delete("text_frame")  
    x, y = 300, 250 


    canV.create_text(x + 2, y + 2, text=text, font=("Arial", 30, "bold"), fill="#777777", tags="text_frame")


    canV.create_text(x, y, text=text, font=("Arial", 30, "bold"), fill="#000000", tags="text_frame")


    bbox = canV.bbox("text_frame")
    if bbox:
        canV.create_rectangle(bbox[0]-10, bbox[1]-10, bbox[2]+10, bbox[3]+10,
                              outline="#444444", width=4, tags="text_frame")


entry.bind("<KeyRelease>", update_text)


window.mainloop()




# 2



from tkinter import *

window = Tk()
window.title("lesson 28")
window.geometry("600x500")
window.config(bg="#000000")

canV = Canvas(height=500, width=600, bg="#ffffff")
canV.place(x=0, y=0)


a = 0
style1 = "pieslice"
radius = 100


def fun_1(val):
    global a, style1
    a = int(val)
    canV.delete("arc")
    if a == 360:
        style1 = "chord"
    else:
        style1 = "pieslice"
    canV.create_arc(100, 100, 300, 300, start=1, extent=a,fill="#4DE487", width=4, outline="#D5EA87", style=style1, tags="arc")
    

def fun_2(val):
    global radius
    radius = int(val)
    canV.delete("arc") 

    canV.create_arc(100, 100, radius, radius, start=1, extent=a, 
                    fill="#4DE487", width=4, outline="#D5EA87", style=style1, tags="arc")
    



scale_1 = Scale(orient=HORIZONTAL, command=fun_1, from_=1, to=360, length=300)
scale_1.place(x=30, y=10)

scale_2 = Scale(orient=HORIZONTAL, command=fun_2, from_=100, to=400, length=300)
scale_2.place(x=30, y=60)




canV.create_arc(100, 100, 300, 300, start=1, extent=a,fill="#4DE487", width=0, outline="#D5EA87", style=style1, tags="arc")




window.mainloop()




































































