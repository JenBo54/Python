# 1


# def fun(arr):










# arr = [1, 2, 3, "text1", "text2", "text3"]




# 2





def fun(num, num_1):
    if num_1 == 0:
        return 1
    elif num_1 > 0:
        return num * fun(num, num_1 - 1)
    else:
        return 1 / fun(num, -num_1)


num = int(input("==>"))
num_1 = int(input("==>"))
print(fun(num, num_1))






# 3


def fun(arr_1):
    if len(arr_1) == 1:
        return arr_1[0]


arr_1 = [1, 5, 3, 9, 2]

print(fun(arr_1))



























# 5

def fun(arr):
    if not arr:
        return []
    if isinstance(arr[0], str):
        return fun(arr[1:])
    else:
        return [arr[0]] + fun(arr[1:])


arr = [1, 'text_1', 2, 'text', 42]
print(fun(arr))

















