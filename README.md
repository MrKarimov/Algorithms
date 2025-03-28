# Algorithms
## **Linear Search vs Binary Search Algorithms**  

### **1. Linear Search**  
Linear search is a **simple searching algorithm** that checks each element **sequentially** from the beginning to the end of the list until it finds the target value.  

#### **Algorithm:**  
1. Start from the **first element** (**L = 0**).
2. Compare each element with the target.
3. If the target is found, return the index.
4. If the list ends without finding the target, return **not found**.

#### **Big O Complexity:**  
- **Best case:** **O(1)** (if the first element is the target).  
- **Worst case:** **O(N)** (if the target is at the last position or not in the list).  

---

### **2. Binary Search**  
Binary search works only on **sorted lists**. It repeatedly **divides the search space in half** until the target is found.  

#### **Algorithm:**  
1. Set **L = 0** (lower bound) and **H = N - 1** (upper bound).  
2. Find the **middle element**:  
   \[
   M = \frac{L + H}{2}
   \]  
3. If **M == target**, return M.  
4. If **M < target**, set **L = M + 1** (search in the right half).  
5. If **M > target**, set **H = M - 1** (search in the left half).  
6. Repeat until **L > H** or the target is found.  

#### **Big O Complexity:**  
- **Best case:** **O(1)** (if the middle element is the target).  
- **Worst case:** **O(log N)** (as the search space is halved in each step).  

---

### **Comparison Table**  

| **Search Type**   | **Best Case** | **Average Case** | **Worst Case**  |
|------------------|--------------|----------------|--------------|
| **Linear Search** | **O(1)**     | **O(N)**       | **O(N)**     |
| **Binary Search** | **O(1)**     | **O(log N)**   | **O(log N)** |

### **Conclusion:**  
- **Linear search** works on both **sorted and unsorted lists**, but it is inefficient for large datasets.  
- **Binary search** is much faster but **only works on sorted lists**.


