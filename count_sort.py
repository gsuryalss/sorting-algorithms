"""
In Counting sort, the frequencies of distinct elements of the array to be sorted is counted
and stored in an auxiliary array, by mapping its value as an index of the auxiliary array.
    Initialize the auxillary array Aux[] as 0.
    Note: The size of this array should be ≥max(A[]).
    Traverse array A and store the count of occurrence of each element in the appropriate
    index of the Aux array, which means, execute Aux[A[i]]++ for each i, where i ranges
    from [0,N−1].
    Initialize the empty array sortedA[]
    Traverse array Aux and copy i into sortedA for Aux[i] number of times where 0≤i≤max(A[]).

The array O(N) time and the resulting sorted array is also computed in O(N) time.
Aux[] is traversed in O(K) time. Therefore, the overall time complexity of counting
sort algorithm is O(N+K).
"""


def max_val(a1):
    # a1.sort()
    # return a1[-1]
    # return sorted(a1)[-1]
    n = a1[0]
    for i in range(len(a1)):
        if n < a1[i]:
            n = a1[i]
    return n


def count_sort(arr_param):

    # finds the maximum value in array
    p = max_val(arr_param) + 1

    # initialize auxiliary array of size p
    aux = [0] * p

    c_sorted = [0] * len(arr_param)

    # store the frequency of array elements in aux array
    for j in arr_param:
        aux[j] += 1

    sort_id = 0
    for q in range(len(aux)):
        tmp = aux[q]

        while tmp > 0:
            c_sorted[sort_id] = q
            sort_id += 1
            tmp -= 1

    return c_sorted


arr = []
print("Counting Sort\n")
m = int(input("Enter the number of elements>>"))
for k in range(m):
    arr.append(int(input()))

# count_sort(arr)
# print("Unsorted Array:\n", arr)
print("Sorted array:\n", count_sort(arr))
