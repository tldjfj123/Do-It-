from typing import MutableSequence


def selection_sort(a : MutableSequence) -> None :
    n = len(a)
    for i in range(n-1) :
        min = i
        for j in range(i+1, n) :
            if a[min] > a[j] :
                min = j
        a[i], a[min] = a[min], a[i]

a = [100, 22, 25, 3, 1, 7]

selection_sort(a)

print(a)