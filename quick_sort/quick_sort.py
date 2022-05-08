def partition(A, l, r):
    i = l+1
    j = r

    while True:
        while i < r and A[i] <= A[l]:
            i += 1

        while j > l and A[j] >= A[l]:
            j -= 1

        if i >= j:
            break

        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    
    A[l], A[j] = A[j], A[l]
    return j

def quick_sort(A, l, r):
    if l >= r:
        return None
    
    p = partition(A, l, r)

    quick_sort(A, l, p-1)
    quick_sort(A, p+1, r)

unsorted_list = list(map(int, input("Put in some integers, seperated with spaces: -> ").split(" ")))
quick_sort(unsorted_list, 0, len(unsorted_list)-1)
print(unsorted_list)
