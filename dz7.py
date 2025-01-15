# 1


# def fun(arr):










# arr = [1, 2, 3, "text1", "text2", "text3"]




# 2






def fun(arr):
    if not arr:
        return []

    if isinstance(arr[0], str):

        return fun(arr[1:])
    else:

        return [arr[0]] + fun(arr[1:])


arr = [1, 'apple', 3.14, 'banana', 42]
num = fun(arr)

print(num)

















