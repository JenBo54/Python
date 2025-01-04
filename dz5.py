
# 1


def fun_1():
    for x in range(5): 
        answer = ""  
        for y in range(10): 
            answer += "#   "
        print(answer) 
print(fun_1())



# 2

def fun_2(num_1, num_2):
    if (num_1== num_2):
        return True
    else:
        return False

num_1=int(input("==>"))
num_2=int(input("==>"))
print(fun_2(num_1, num_2))


# 3


def fun_3(arr):
    for i in range(10):
        num_4= random.randint(1,20)
        num_4+=1
        arr.append(num_4)
    return arr


import random
arr=[]
print(fun_3(arr))



# 4



































