"""
In max-heaps, maximum element will always be at the root. Heap Sort uses this property of heap to sort the array.
    * Initially build a max heap of elements in Arr.
    * The root element, that is Arr[1], will contain maximum element of
    * Arr. After that, swap this element with the last element of
    * Arr and heapify the max heap excluding the last element which is already in its correct position and then decrease
      the length of heap by one.
    * Repeat the step 2, until all the elements are in their correct position.
"""


def build_heap(arr_hp, hp_size, j):

    max_val = j
    left_val = 2 * j + 1
    right_val = 2 * j + 2

    # print(j, left_val, right_val)
    if left_val < hp_size and arr_hp[max_val] < arr_hp[left_val]:
        max_val = left_val
        # print("left_val", left_val)
        # print(j)
        # print(arr_hp[max_val])

    if right_val < hp_size and arr_hp[max_val] < arr_hp[right_val]:
        max_val = right_val
        # print("right_val", right_val)
        # print(j)
        # print(arr_hp[max_val])

    # print("Max_val", max_val)

    if max_val != j:
        arr_hp[j], arr_hp[max_val] = arr_hp[max_val], arr_hp[j]

        # re-build the heap with parent maximum node
        arr_hp = build_heap(arr_hp, hp_size, max_val)

    # print("build array", arr_hp)

    return arr_hp


def heap_sort(arr_param, n):

    # print("Array", arr_param)
    # build a max heap
    for i in range(n, -1, -1):
        arr_param = build_heap(arr_param, n, i)

    # list the elements one by one
    for p in range(n-1, 0, -1):
        arr_param[p], arr_param[0] = arr_param[0], arr_param[p]
        arr_param = build_heap(arr_param, p, 0)

    # print("Sorted", arr_param)
    return arr_param


arr = []
print("Heap Sort\n")
m = int(input("Enter the number of elements>>"))
for k in range(m):
    arr.append(int(input()))

# heap_sort(arr, m)
print("Sorted Array: ", heap_sort(arr, m))
