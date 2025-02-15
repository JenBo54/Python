text = open("text.txt" , "w")
text.write("")
text.close()






# 1





def fun():
    text = open("text.txt", "a")
    text.write(input("==>"))
    text.close()
    text = open("text.txt", "r")
    content = text.read()
    text.close()
    return content

print(fun())




2 


def calc():
    x1= int(input("==>"))
    x2= int(input("==>"))
    d= input("введи действие")
    if (d== "+"):
        answer= x1 + x2
        print(answer)
    elif (d== "-"):
        answer= x1 - x2
        print(answer)
    elif (d== "/"):
        answer= x1 / x2
        print(answer)
    elif (d== "*"):
        answer= x1 * x2
        print(answer)
    else:
        print("error")

    with open("his.txt", "a", encoding="utf-8") as history:
        history.write(str(answer))

print(calc())


with open("his.txt", "r", encoding="utf-8") as history:
    print("История вычислений:")
    print(history.read())





# 3



def load():
    w= input("==>")
    if (w== "new"):
        users = open("p.txt", "a")
        users.write(input("==>"))
        users.close()
    # elif (w== "del"):
    #     dele= open()

    elif (w== "ex" or "exit"):
        use = open("p.txt", "r")
        use.close()
        return use

print(load)











































