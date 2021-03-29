"""""
Bubble sort is based on the idea of repeatedly comparing pairs of adjacent elements
and then swapping their positions if they exist in the wrong order.

Complexity:
The complexity of bubble sort is O(n2)
O(n2) in both worst and average cases, because the entire array needs to be iterated
for every element.

"""


def bubble_sort(arr_param):
    n = len(arr_param)

    # no of passes required
    for i in range(n-1):

        # compare and swap adjacent elements
        for j in range(n-i-1):
            if arr_param[j] > arr_param[j+1]:
                arr_param[j], arr_param[j+1] = arr_param[j+1], arr_param[j]

        print("\n {} pass {} \n".format(i, arr_param))

    return arr_param


arr = []
print("Bubble Sort")
m = int(input("Enter the number of elements>>"))
print("\nEnter the array values (one by one):\n")

for k in range(m):
    arr.append(int(input()))

print("Unsorted Array:\n", arr)
print("Sorted array:\n", bubble_sort(arr))
print("\nTotal Passes:", (m-1))
