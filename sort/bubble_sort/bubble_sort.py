def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
    return numbers




numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers= bubble_sort(numbers)
print("Sorted array is:", sorted_numbers)
# Output: Sorted array is: [11, 12, 22, 25, 34, 64, 90]
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# The time complexity of the bubble sort algorithm is O(n^2) in the worst and average cases.