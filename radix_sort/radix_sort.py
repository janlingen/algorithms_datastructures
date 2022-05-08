def radix_sort(A, d):
    buckets = [x for x in range(0, len(A)-1)]
    for t in range(0, d):
        count = [x for x in range(0,10)]
        for i in range(0, len(A)-1):
            x = A[i][t]
            count[int(x)] += 1

        count[9] = len(A) - count[9]
        for d in range(8, -1, -1):
            count[d] = count[d+1] - count[d]

        for i in range(0, len(A)-1):
            x = A[i][t]
            buckets[int(count[x])] = A[i]
            count[int(x)] += 1
        
        for i in range(0, len(A)-1):
            A[i] = buckets[i]

unsorted_list = list(input("Put in some integers, seperated with spaces: -> ").split(" "))
radix_sort(unsorted_list, 3)
print(unsorted_list)