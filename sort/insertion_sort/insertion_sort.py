def insertion_sort(arr)->list:
    for i in range(1 , len(arr)):
        key = arr[i]
        j = i-1
        
        
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
            
        arr[j+1] = key
    return arr
        
test = [1, 3, 14, 2, 5, 56,45,456,85,74,18]

nums_sort = insertion_sort(test)

print (nums_sort)