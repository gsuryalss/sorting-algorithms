"""
Quick sort is based on the divide-and-conquer approach based on the idea of choosing one element as a pivot element
and partitioning the array around it such that: Left side of pivot contains all the elements that are less than the
pivot element Right side contains all elements greater than the pivot
It reduces the space complexity and removes the use of the auxiliary array that is used in merge sort. Selecting a
random pivot in an array results in an improved time complexity in most of the cases.
Use randorm function to reduce the time complexity of this algorithm.
Complexity The worst case time complexity of this algorithm is O(N2) , but as this is randomized algorithm, its time
complexity fluctuates between O(N2) and O(NlogN) and mostly it comes out to be O(NlogN)
"""


def quick_sort(arr_param):
    qsort_helper(arr_param, 0, len(arr_param)-1)
    return arr_param


def qsort_helper(arr_param, first, last):
    if first < last:
        split_point = qsort_partition(arr_param, first, last)

        qsort_helper(arr_param, first, split_point-1)
        qsort_helper(arr_param, split_point+1, last)


def qsort_partition(arr_param, first, last):
    pivot_value = arr_param[first]

    left_mark = first + 1
    right_mark = last

    flag = False
    while not flag:

        while left_mark <= right_mark and arr_param[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while right_mark >= left_mark and arr_param[right_mark] >= pivot_value:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            flag = True
        else:
            arr_param[left_mark], arr_param[right_mark] = arr_param[right_mark], arr_param[left_mark]

        arr_param[first], arr_param[right_mark] = arr_param[right_mark], arr_param[first]

    return right_mark


arr = []
print("Selection Sort\n")
m = int(input("Enter the number of elements>>"))
for k in range(m):
    arr.append(int(input()))

print("Unsorted Array:\n", arr)
print("Sorted array:\n", quick_sort(arr))
