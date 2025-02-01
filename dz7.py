

# 2


# def fun_1(n,m):

#     return n * fun_1(n, m - 1)






# 3

def fun_2(arr, index = 0):
    if index == len(arr) - 1:
        return arr[index]
    max_in_rest = fun_2(arr, index + 1)
    
    if arr[index] > max_in_rest:
        return arr[index]
    else:
        return max_in_rest


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(fun_2(arr))




# 4




def create_dict(keys, values):
    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]
    
    return result_dict


keys = ['a', 'b', 'c']
values = [1, 2, 3]

print(create_dict(keys, values))



























