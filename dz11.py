import threading

arr = [5, 2, 9, 1, 5, 6]




def sort_arr(arr_loc):
    for r in arr_loc:
        for i in range(len(arr_loc) - 1):
            if(arr_loc[i] > arr_loc[i+1]):
                print(arr_loc[i] , arr_loc[i+1])
                el = arr_loc[i]
                arr_loc[i] = arr_loc[i + 1]
                arr_loc[i + 1] = el
                print(arr_loc)
    
    return arr_loc

print(arr)
print(sort_arr(arr))

thread_1 = threading.Thread(target=sort_arr, ar=(arr,))

thread_1.start()




thread_1.join()





































































