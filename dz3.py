


# # задача 1

num_1= (input("==>"))
num_2= (input("==>"))
while(num_1 != "y" and num_2 != "y"):
    num_int_1=int(num_1)
    num_int_2=int(num_2)
    print(num_int_1+num_int_2)
    num_1= (input("==>"))
    num_2= (input("==>"))
print("error")


# задача 2
num_20= (input("введите числовое значение от 1 до 1000000 (копейки) ==>"))
while(num_20 != "y" and num_20 != "Y" and num_20 != 1):
    num_int_20=int(num_20)
    num_21= str(input("какую валюту ты хочешь выбрать? (рубли/доллары) ==>"))
    if(num_21 == "рубли"):
        print(num_int_20 , "копеек в рублях и копейках:" , num_int_20//100 , num_int_20%100)
    if(num_21 == "доллары"):
        print(num_int_20 , "копеек в долларах и центах:" , num_int_20*100//100 , num_int_20*100%100)
    else:
        print("error")
        num_20= (input("введите числовое значение от 1 до 1000000 (копейки) ==>"))
print("error")




# задача 3

print("6*6?")
num_31= int(input("==>"))
if(num_31==6*6):
    print("welldone!")
else:
    (print("uncorrect."))

print("7*4?")
num_32= int(input("==>"))
if(num_32==7*4):
    print("welldone!")
else:
    (print("uncorrect."))

print("9*5?")
num_33= int(input("==>"))
if(num_33==9*5):
    print("welldone!")
else:
    (print("uncorrect."))

print("8*8?")
num_34= int(input("==>"))
if(num_34==8*8):
    print("welldone!")
else:
    (print("uncorrect."))



















































































































































































































































































































































