def selection_sort(A):
    for i in range(0,len(A)-1):
        min_pos = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_pos]:
                min_pos = j
        A[i], A[min_pos] = A[min_pos], A[i]
    return A

unsorted_list = list(map(int, input("Put in some integers, seperated by spaces: -> ").split(" ")))
print(selection_sort(unsorted_list))
