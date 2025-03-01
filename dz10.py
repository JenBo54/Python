import json

# text = open("text.txt" , "w")
# text.write("")
# text.close()






# 1





# def fun():
#     text = open("text.txt", "a")
#     text.write(input("==>"))
#     text.close()
#     text = open("text.txt", "r")
#     content = text.read()
#     text.close()
#     return content

# print(fun())




# 2 


# def calc():
#     x1= int(input("==>"))
#     x2= int(input("==>"))
#     d= input("введи действие")
#     if (d== "+"):
#         answer= x1 + x2
#         print(answer)
#     elif (d== "-"):
#         answer= x1 - x2
#         print(answer)
#     elif (d== "/"):
#         answer= x1 / x2
#         print(answer)
#     elif (d== "*"):
#         answer= x1 * x2
#         print(answer)
#     else:
#         print("error")

#     with open("his.txt", "a", encoding="utf-8") as history:
#         history.write(str(answer))

# print(calc())


# with open("his.txt", "r", encoding="utf-8") as history:
#     print("История вычислений:")
#     print(history.read())





# 3




file_3 = open("w.json" , "r")
file_3.close()

def load():
    users = open("w.json", "r")
    arr_2 = json.loads(users.read())

    if (w== "new"):
        print(arr_2)
        arr_2[input("name ==>")] = input("password ==>")
        with open("w.json", "w") as file:
            json.dump(arr_2 , file)

    elif (w== "del"):
        user= input("==>")
        del arr_2[user]
        print("deleted")
        with open("w.json", "w") as file:
            json.dump(arr_2, file)



w = input("==>")
while(w != "ex" or w != "exit"):
    load()
    w= input("==>")






































