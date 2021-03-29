"""
Insertion sort is based on the idea that one element from the input elements is consumed
in each iteration to find its correct position i.e, the position to which it belongs in
a sorted array.

In worst case,each element is compared with all the other elements in the sorted array.
For N elements, there will be N2 comparisons. Therefore, the time complexity is O(N2)
"""


def insertion_sort(arr_param):

    n = len(arr_param)

    # define no of passes required
    for i in range(n):
        temp, j = arr_param[i], i

        # check whether adjacent element in left possess greater or less than curr element
        while j > 0 and temp < arr_param[j-1]:
            arr_param[j] = arr_param[j-1]
            j -= 1

        arr_param[j] = temp
        print("\n {} pass {} \n".format(i, arr_param))

    return arr_param


arr = []
print("Insertion Sort")
m = int(input("Enter the number of elements>>"))
print("\nEnter the array values (one by one):\n")
for k in range(m):
    arr.append(int(input()))

print("Unsorted Array:\n", arr)
print("Sorted array:\n", insertion_sort(arr))
print("\nTotal Passes:", m)
