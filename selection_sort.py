"""
The Selection sort algorithm is based on the idea of finding the minimum or maximum element in an unsorted array and
then putting it in its correct position in a sorted array.
To find the minimum element from the array of
N elements, N−1 comparisons are required. After putting the minimum element in its proper position, the size of an
unsorted array reduces to N−1 and then N−2 comparisons are required to find the minimum in the unsorted array
Therefore (N−1) + (N−2) + ....... + (N⋅(N−1))/2 comparisons and N swaps result in the overall complexity of
O(N2).
"""


def selection_sort(arr_param):

    n = len(arr_param)

    # reduces the effective size of the array by one in  each iteration
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr_param[j] < arr_param[min_idx]:
                min_idx = j
        arr_param[min_idx], arr_param[i] = arr_param[i], arr_param[min_idx]

        print("\n {} pass {} \n".format(i, arr_param))

    return arr_param


arr = []
print("Selection Sort\n")
m = int(input("Enter the number of elements>>"))
for k in range(m):
    arr.append(int(input()))

print("Unsorted Array:\n", arr)
print("Sorted array:\n", selection_sort(arr))
print("\nTotal Passes:", m-1)
