"""
Bucket sort is a comparison sort algorithm that operates on elements by dividing them into different buckets and
then sorting these buckets individually. Each bucket is sorted individually using a separate sorting algorithm or
by applying the bucket sort algorithm recursively. Bucket sort is mainly useful when the input is uniformly distributed
over a range.
bucketSort(arr[], n)
    1) Create n empty buckets (Or lists).
    2) Do following for every array element arr[i].
    .......a) Insert arr[i] into bucket[n*array[i]]
    3) Sort individual buckets using insertion sort.
    4) Concatenate all sorted buckets.
"""


from bble_srt import bubble_sort
import math


def max_val(arr_mv):
    d = arr_mv[0]
    for i in range(len(arr_mv)):
        if d < arr_mv[i]:
            d = arr_mv[i]
    return d


def hashing(A):
    m = A[0]
    for i in range(1, len(A)):
        if m < A[i]:
            m = A[i]
    result = [m, int(math.sqrt(len(A)))]
    return result


def re_hashing(i, code):
    return int(i / code[0] * (code[1] - 1))


def bucket_sort(arr_param, n):

    # buck_arr = [0] * (max_val(arr_param) + 1)
    code = hashing(arr_param)
    print("code hash", code)
    buck_arr = [list() for _ in range(code[1])]

    buck_size = len(buck_arr)
    print("bucket size", buck_size)

    for x in arr_param:
        i = re_hashing(x, code)
        print("rehash val", i)
        buck_arr[i].append(x)

    for j in buck_arr:
        print(j)
        bubble_sort(j)

    r = 0
    for p in range(buck_size):
        for q in buck_arr[p]:
            arr_param[r] = q
            r += 1
    return arr_param


arr = []
print("Bucket Sort\n")
m = int(input("Enter the number of elements>>"))
for k in range(m):
    arr.append(int(input()))

# bucket_sort(arr, m)
print("Sorted Array: ", bucket_sort(arr, m))