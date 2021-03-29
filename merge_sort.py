"""
Merge sort is a divide-and-conquer algorithm based on the idea of breaking down a list into several sub-lists until
each sublist consists of a single element and merging those sublists in a manner that results into a sorted list.

The list of size N is divided into a max of logN parts, and the merging of all sublists into a single list takes
O(N) time, the worst case run time of this algorithm is O(NLogN)

- Recursively sort the first half of the input array.
— Recursively sort the second half of the input array.
— Merge two sorted sub-lists into one list.
"""


def merge_sort(arr_param):

    print("Splitting ", arr_param)

    if len(arr_param) > 1:

        mid = len(arr_param)//2
        left_half = arr_param[:mid]
        right_half = arr_param[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        p = q = r = 0

        # merge the sub-lists
        while p < len(left_half) and q < len(right_half):
            if left_half[p] < right_half[q]:
                arr_param[r] = left_half[p]
                p = p+1
            else:
                arr_param[r] = right_half[q]
                q = q+1
            r = r+1

        # to process/merge one element - left half
        while p < len(left_half):
            arr_param[r] = left_half[p]
            p = p+1
            r = r+1

        # to process/merge one element - right half
        while q < len(right_half):
            arr_param[r] = right_half[q]
            q = q+1
            r = r+1

    print("Merging ", arr_param)


arr = []
print("Merge Sort")
m = int(input("Enter the number of elements>>"))
print("\nEnter the array values (one by one):\n")
for k in range(m):
    arr.append(int(input()))
print("Sorted array:\n", merge_sort(arr))
