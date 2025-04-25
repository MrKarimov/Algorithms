def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index=j
                arr[i],arr[min_index]=arr[min_index], arr[i]
    return arr



arr = [64, 34, 25, 12, 22, 11, 90]

sorted_numbers = selection_sort(arr)
print(sorted_numbers)
# Output: Sorted array is: [2, 11, 25, 45, 56, 64, 88]
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# The time complexity of the selection sort algorithm is O(n^2) in the worst and average cases.
# The space complexity is O(1) because it only requires a constant amount of additional memory.
# The selection sort algorithm is not a stable sort, meaning that it may change the relative order of equal elements.