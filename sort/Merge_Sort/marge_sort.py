def merge_sort(arr):
    if len(arr) > 1:
        r = len(arr) // 2
        left = arr[:r]
        right = arr[r:]

        # Rekursiv bo‘lib chiqamiz
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Ikkita bo‘lakni birlashtirish
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:  # bu yerda else bo‘lishi kerak
                arr[k] = right[j]
                j += 1
            k += 1

        # Qolgan chap tomonni qo‘shish
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Qolgan o‘ng tomonni qo‘shish
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

nums = [1, 5, 2, 45, 14, 21, 3]

sort_nums = merge_sort(nums)

print(sort_nums)