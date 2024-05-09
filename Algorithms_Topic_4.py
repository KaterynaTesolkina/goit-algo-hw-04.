import timeit
import random

# Алгоритм сортування злиттям
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

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Тестування алгоритмів
arr = random.sample(range(10000), 500)

print("Merge Sort:")
print(timeit.timeit(lambda: merge_sort(arr.copy()), number=50)) 

print("Insertion Sort:")
print(timeit.timeit(lambda: insertion_sort(arr.copy()), number=50)) 

print("Timsort:")
print(timeit.timeit(lambda: sorted(arr.copy()), number=50))

# отримані часи виконання кожного з алгоритмів:
# Merge Sort: близько 0.0198 секунди
# Insertion Sort: близько 0.1324 секунди
# Timsort: близько 0.00098 секунди
# Ці результати підтверджують, що Timsort значно ефективніший за інші алгоритми, особливо на масивах даних такого розміру. 