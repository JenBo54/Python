from tkinter import *
 # 1




window = Tk()
window.title("lesson 28")
window.geometry("600x500")
window.config(bg="#000000")



canV = Canvas(height=500 , width=600 , bg="#ffffff")
canV.place(x=0 , y=0)

canV.create_line(0,350 , 360, 320 ,600, 320, fill="#000000" , width=4 , smooth=True)

canV.create_line(0,290, 30, 310, 60, 290, 90, 310, 120, 290, 150, 310, 180, 290, 210, 310, 240, 290, 270, 310, 300, 290, 315, 300, fill="#000000" , width=3 , smooth=True)

canV.create_line(300, 327, 340, 250, 355, 270, 400, 130, 600, 320, fill="#000000" , width=4)

canV.create_oval(100 , 100 , 150, 150 , fill="#ffe032" , width= 5 , outline="#ffe032")

canV.create_line(300, 110,320, 90, 340, 110, fill="#000000" , width=4,smooth=True )
canV.create_line(260, 110,280, 90, 300, 110, fill="#000000" , width=4,smooth=True )

canV.create_line(260, 140,280, 120, 300, 140, fill="#000000" , width=4,smooth=True )
canV.create_line(220, 140,240, 120, 260, 140, fill="#000000" , width=4,smooth=True )

canV.create_oval(110 , 370 , 130, 380 , fill="#ffffff" , width= 3 , outline="#000000")
canV.create_oval(150 , 390 , 170, 400 , fill="#ffffff" , width= 3 , outline="#000000")



window.mainloop()








# 2



# window = Tk()
# window.title("lesson 28")
# window.geometry("600x500")
# window.config(bg="#000000")



# canV = Canvas(height=500 , width=600 , bg="#ffffff")
# canV.place(x=0 , y=0)



# canV.create_oval(100 , 100 ,300,300 , fill="#ffe032" , width= 5 , outline="#ffe032")


# canV.create_oval(150 , 150 ,180,180 , fill="#000000" , width= 10 , outline="#ffffff")

# canV.create_oval(220 , 150 ,250,180 , fill="#000000" , width= 10 , outline="#ffffff")

# canV.create_line(150,220, 200, 260, 250, 220,  fill="#000000" , width=5 , smooth=True)




window.mainloop()




# 4



# window = Tk()
# window.title("lesson 28")
# window.geometry("600x500")
# window.config(bg="#000000")



# canV = Canvas(height=500 , width=600 , bg="#ffffff")
# canV.place(x=0 , y=0)





# # canV.create_line(0,300 , 300, 300, fill="#000000" , width=5)

















