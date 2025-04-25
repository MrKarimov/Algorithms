# 🥮 Sorting Algorithms in Python

This repository demonstrates some of the most well-known sorting algorithms implemented in Python. Each algorithm is explained with a short description, time complexity, and code example.

---

## 📚 Table of Contents

1. [Bubble Sort](#1-bubble-sort)
2. [Selection Sort](#2-selection-sort)
3. [Insertion Sort](#3-insertion-sort)
4. [Merge Sort](#4-merge-sort)
5. [Quick Sort](#5-quick-sort)
6. [Heap Sort](#6-heap-sort)
7. [Comparison Table](#7-comparison-table)

---

## 1. 🔁 Bubble Sort

**Idea**: Repeatedly compares adjacent elements and swaps them if they are in the wrong order.

**Time Complexity**:
- Best: O(n)
- Average: O(n²)
- Worst: O(n²)

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

---

## 2. ✅ Selection Sort

**Idea**: Finds the smallest element in the unsorted portion and moves it to the sorted part.

**Time Complexity**:
- Best: O(n²)
- Average: O(n²)
- Worst: O(n²)

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

---

## 3. 🧙 Insertion Sort

**Idea**: Builds the final sorted array one item at a time by inserting it into its correct position.

**Time Complexity**:
- Best: O(n)
- Average: O(n²)
- Worst: O(n²)

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

---

## 4. ⚡ Merge Sort

**Idea**: Divides the array into halves, sorts each half, and merges them back together.

**Time Complexity**:
- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n log n)

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
```

---

## 5. 🚀 Quick Sort

**Idea**: Picks a pivot element and partitions the array into two parts — less than and greater than the pivot.

**Time Complexity**:
- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n²)

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)
```

---

## 6. 🏗️ Heap Sort

**Idea**: Builds a heap from the array and repeatedly removes the largest/smallest element.

**Time Complexity**:
- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n log n)

```python
import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]
```

---

## 7. 📊 Comparison Table

| Algorithm       | Best       | Average    | Worst      | Stable | In-Place |
|----------------|------------|------------|------------|--------|----------|
| Bubble Sort     | O(n)       | O(n²)       | O(n²)       | Yes    | Yes      |
| Selection Sort  | O(n²)      | O(n²)       | O(n²)       | No     | Yes      |
| Insertion Sort  | O(n)       | O(n²)       | O(n²)       | Yes    | Yes      |
| Merge Sort      | O(n log n) | O(n log n)  | O(n log n)  | Yes    | No       |
| Quick Sort      | O(n log n) | O(n log n)  | O(n²)       | No     | Yes      |
| Heap Sort       | O(n log n) | O(n log n)  | O(n log n)  | No     | Yes      |

---

## �� Tip

For real-world Python sorting, prefer the built-in:

```python
sorted(arr)  # or arr.sort()
```

Python uses **Timsort**, a hybrid of Merge Sort and Insertion Sort — fast and stable.

---

## �� Author

Created by Mr_Karimov

---


