# 1


arr= [1, 2 ,3 ,4 ,5, 6, 7]

lam_1= list(map(lambda x: 0 if x==1 or x==2 or x==3 else x, arr))
print(lam_1)

 

# 2 
arr_1=[1, 2, 3, 4, "texr", "text_1"]

lam_2= list(filter(lambda x: type(x) == int, arr_1))
print(lam_2)




# 3


ar1 = [1,3,6]
ar2 = [3,9,2]


lam_3= list(map(lambda x, y: x if x > y else y, ar1, ar2))
print(lam_3)




# 4

arr_4 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

def fun(num):
    lam_4= list(map(lambda arr_x: list(map(lambda x: x * num, arr_x)) , arr_4))
    num += 1
    return lam_4

print(fun(2))













