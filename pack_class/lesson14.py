1

# class Calculator:
#     def __init__(self, num_1, num_2):
#         self.numbers= [num_1, num_2]

#     def fun_0(self):
#         self.numbers.append
        


#     def fun_1(self):
#         print(self.num_1 * self.num_2)

#     def fun_2(self):
#         print(self.num_1 / self.num_2)

#     def fun_3(self):
#         print(self.num_1 + self.num_2)

#     def fun_4(self):
#         print(self.num_1 - self.num_2)



# calc_1 = Calculator(int(input("==>")), int(input("==>")))

# sigh= str(input("==>"))
# if (sigh == "*"):
#     print(calc_1.fun_1())
# elif (sigh == "/"):
#     print(calc_1.fun_2())
# elif (sigh == "+"):
#     print(calc_1.fun_3())
# elif (sigh == "-"):
#     print(calc_1.fun_4())
# else:
#     print("error")







# 2



class Transport:
    def __init__(self, manuf, mod, year, speed):
        self.manuf = manuf
        self.mod = mod
        self.year = year
        self.speed = speed

    def info(self):
        print("manufacturer:" , self.manuf, "Model name:", self.mod, "Year:", self.year, "middle speed:", self.speed)

    def speed0(self):
        dist = int(input("==>"))
        print(dist / self.speed)


class Cars(Transport):
    def __init__(self, manuf, mod, year, speed, seats):
        super().__init__(manuf, mod, year, speed)
        self.seats = seats

    def info(self):
        super().info()
        print(self.seats)


transport_1 = Transport("Subaru", "Impreza WRX STI", 1998, 120)
transport_1.info()
transport_1.speed0()


car_1 = Cars("Toyota", "Camry", 2020, 150, 5)
car_1.info()
car_1.speed0()



class Helicopter(Transport):
    def __init__(self, manuf, mod, year, speed, lift_capacity):
        super().__init__(manuf, mod, year, speed)
        self.lift_capacity = lift_capacity

    def take_off(self):
        print(self.mod)

    def info(self):
        super().info()
        print(self.lift_capacity)


helicopter_1 = Helicopter("Sikorsky", "S-76", 2015, 250, 4000)
helicopter_1.info()
helicopter_1.take_off()
helicopter_1.speed0()












