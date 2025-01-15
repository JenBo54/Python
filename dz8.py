# 1





# inp = input("==>")

match(inp):
    case("1"):
        print("работа")

    case("2"):
        print("поход к родственникам")

    case("3"):
        print("чемпионат по ралли")

    case("4"):
        print("уборка")

    case("5"):
        print("поездка в магазин")

    case("6"):
        print("выходеной 1")

    case("7"):
        print("выходной 2")

    case _:
        print("X")

        

# 2


inp_1= int(input("==>"))
inp_2= str(input("==>"))
inp_3= int(input("==>"))


match(inp_2):
    case("+"):
        print(inp_1+inp_3)
    case("-"):
        print(inp_1-inp_3)
    case("*"):
        print(inp_1*inp_3)
    case("/"):
        print(inp_1/inp_3)
    case _:
        print("X")







































































