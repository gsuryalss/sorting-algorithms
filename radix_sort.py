"""
CountSort is not comparison based algorithm. It has the complexity of O(n+k), where k is the maximum element
of the input array.So, if O(n) ,CountSort becomes linear sorting, which is better than comparison based sorting
algorithms that have O(nlogn) time complexity. The idea is to extend the CountSort algorithm to get a better
time complexity when k goes O(n2). Here comes the idea of Radix Sort.
Algorithm
    For each digit i where i varies from the least significant digit to the most significant digit of a number
    Sort input array using countsort algorithm according to ith digit.
The Radix Sort algorithm is an important sorting algorithm that is integral to suffix -array construction
algorithms. It is also useful on parallel machines.
"""


def max_val(arr_mv):
    arr_mv.sort()
    return arr_mv[-1]


def count_sort(arr_cs, n):

    x = 0
    arr_len = len(arr_cs)

    # frequency range 0,1,2..9 = 10
    freq = [0] * 10

    output = [0] * arr_len

    for i in range(arr_len):
        idx = arr_cs[i] // n

        freq[idx % 10] += 1
        # print(idx % 10)

    print("frequency 1")
    print(n, freq)

    for j in range(1, 10):
        freq[j] += freq[j-1]

    print("frequency 2")
    print(freq)

    r = arr_len - 1
    while r >= 0:
        idx1 = arr_cs[r] // n
        output[freq[idx1 % 10] - 1] = arr_cs[r]
        freq[idx1 % 10] -= 1
        r -= 1

    # print("output")
    print(n, output)
    print("frequency3", freq)

    for q in range(len(arr_cs)):
        arr_cs[q] = output[q]

    # print(output)
    return arr_cs


def radix_sort(arr_param):

    mul = 1
    p = max_val(arr_param)

    while p > 0:
        arr_param = count_sort(arr_param, mul)
        mul *= 10
        p //= 10

    return arr_param


arr = []
print("Radix Sort\n")
m = int(input("Enter the number of elements>>"))
for k in range(m):
    arr.append(int(input()))

# radix_sort(arr)
print(radix_sort(arr))