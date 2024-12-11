



# дз 1
num_inp_1= int(input("==>"))
if(num_inp_1 % 2 == 0):
    print("четное")
else:
    print("нечетное")



# дз 2
num_2= int(input("==>"))
num_3= int(input("==>"))
if(num_2>num_3):
    print(num_2)
else:
    print(num_3)



# дз 3
num_4= int(input("==>"))
if(num_4 > 0):
    print("положительное")
else:
    if(num_4 < 0):
        print("отрицательное")
    else:
        print("равно 0")



# дз 4
num_5= int(input("==>"))
num_6= int(input("==>"))
if(num_5==num_6):
    print("равно")
else:
    if(num_5>num_6):
        print(num_5 , num_6)
    else:
        print(num_6 , num_5)




# дз 5
num_01= int(input("==>"))
num_02= int(input("==>"))
num_03= int(input("==>"))
num_04= int(input("==>"))
num_05= int(input("==>"))
num_mid= (num_01+num_02+num_03+num_04+num_05) // 5
if(num_mid>= 3):
    print("допущен")
else:
    print("недопущен")



# дз 6
num_inp_2= int(input("==>"))
if(num_inp_2 % 2 == 0):
    print(num_inp_2* 3)
else:
    print(num_inp_2 // 2)



# дз 7
num_10= int(input("==>"))
num_11= int(input("==>"))
simb_1= int(input("числа от 1 до 4 ==>"))
if(simb_1 == 1):
    print(num_10+num_11)
else:
    if(simb_1 == 2):
         print(num_10-num_11)
    else:
        if(simb_1 == 3):
            print(num_10*num_11)
        else:
            if(simb_1 == 4):
                print(num_10//num_11)
            else: print("введи число от 1 до 4")

        




























































































































