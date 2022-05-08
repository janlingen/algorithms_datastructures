def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

unsorted_list = list(map(int, input("Put in some integers, seperated with spaces: -> ").split(" ")))
print(insertion_sort(unsorted_list))