

# 1

obj_0= {0: "q", 1: "w", 2: "e"}
obj_1= {3: "r", 4: "t", 5: "y"}

obj_0.update(obj_1)
print(obj_0)


# # 2

 
obj_2= {}


for key in range (1,10+1):
    obj_2.update({
        key: key**3
    })

print(obj_2)





# 3

obj_3= {}

num_3= "hello python"

for i in range(len(num_3)):
    obj_3[num_3[i]]= i
    
print(obj_3)



# 4

list_0= [0, 1, 2, 3, 4, 5]
list_1= ["a", "b", "c", "d", "e"]
obj_4= {}
for i in range(len(list_1)):
    obj_4.update({
        list_0[i]: list_1[i]
    })

print(obj_4)


























































































































































