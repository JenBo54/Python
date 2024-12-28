# 1

num = []
sq = []
cub = []
for x in range (1, 11) :
    num.append (x)
    sq.append (x**2)
    cub.append (x**3)
print ("numbers: ",num)
print ("squares: ",sq)
print ("cubes : ",cub)

# # 2
pr=[]
num_21=int(input("==>"))
num_22=int(input("==>"))
num_23=int(input("==>"))
num_24=int(input("==>"))
num_25=int(input("==>"))
num_26=int(input("==>"))
pr.append(num_21)
pr.append(num_22)
pr.append(num_23)
pr.append(num_24)
pr.append(num_25)
pr.append(num_26)
print(sum(pr))


# 3

arr= [1, 2, 3, 4, 5, 6]
print(arr)
arr.reverse()
print(arr)



# 4

per=[]

num_1=int(input("==>"))
num_2=int(input("==>"))
num_3=int(input("==>"))
num_4=int(input("==>"))
num_5=int(input("==>"))
per.append(num_1)
per.append(num_2)
per.append(num_3)
per.append(num_4)
per.append(num_5)
print(per)
print("периметр =" , num_1*num_2*num_3*num_4*num_5)



# 5
y=[]
num_11= int(input("==>"))
num_12= int(input("==>"))
num_13= int(input("==>"))
num_14= int(input("==>"))
num_15= int(input("==>"))
num_16= int(input("==>"))
num_17= int(input("==>"))
num_18= int(input("==>"))
num_19= int(input("==>"))
num_110= int(input("==>"))
num_111= int(input("==>"))
num_112= int(input("==>"))
y.append(num_11)
y.append(num_12)
y.append(num_13)
y.append(num_14)
y.append(num_15)
y.append(num_16)
y.append(num_17)
y.append(num_18)
y.append(num_19)
y.append(num_110)
y.append(num_111)
y.append(num_112)
max_1=max(y)
print(y.index(max_1))
min_1=min(y)
print(y.index(min_1))





# 6
temp=[-30,-32,-34,-28,-45,-120,-12,-26,-23,-21,-21,-21,-32,-22,-25,-29,-27,-22,-30,-30,-32,-30,-2,-30,-30,-40,-26,-28,-25,-21]

srznach= sum(temp)/len(temp)
print(srznach)


# 7

num_1=[1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
num_2=list(dict.fromkeys(num_1))
print(num_2)























