 


# 1


class One:
    def __init__(self):
        self.num_1 = 3
        self.num_2 = 12
        self.num_3 = 6

    def fun(self):
        arr = []
        arr.append(self.num_1)
        arr.append(self.num_2)
        arr.append(self.num_3)
        print(arr)

one_1= One()
one_1.fun()



# 2




class Car:
    def __init__ (self):
        self.manuf = "Subaru"
        self.mod = "Impreza WRX STI"
        self.year = "1998"
        self.speed = 120

    def info(self):
        print("manufacturer:" , self.manuf, "Model name:", self.mod, "Year:", self.year, "middle speed:", self.speed)
    
    def speed0(self):
        dist= int(input("==>"))
        time= dist / self.speed
        print(time)


car_1= Car()
car_1.info()
car_1.speed0()




# 3


class Calculator:
    def __init__(self):
        self.num_1= int(input("==>"))
        self.num_2= int(input("==>"))

    def fun_1(self):
        print(self.num_1 * self.num_2)

    def fun_2(self):
        print(self.num_1 / self.num_2)


    def fun_3(self):
        print(self.num_1 + self.num_2)

    def fun_4(self):
        print(self.num_1 - self.num_2)


calc_1 = Calculator()

sigh= str(input("==>"))
if (sigh == "*"):
    print(calc_1.fun_1())
elif (sigh == "/"):
    print(calc_1.fun_2())
elif (sigh == "+"):
    print(calc_1.fun_3())
elif (sigh == "-"):
    print(calc_1.fun_4())
else:
    print("error")

