def bucket_sort(A):
    max_val = A[0]
    min_val = A[0]

    for i in range(1, len(A)):
        if A[i] > max_val:
            max_val = A[i]
        if A[i] < min_val:
            min_val = A[i]

    buckets = []
    for i in range(1, (max_val - min_val + 2)):
        buckets.append([])

    for i in range(0, len(A)):
        buckets[A[i] - min_val].append(A[i])

    count = 0
    for i in buckets:
        for j in i:
            A[count] = j 
            count += 1 

unsorted_list = list(map(int, input("Put in some integers, seperated with spaces: -> ").split(" ")))
bucket_sort(unsorted_list)
print(unsorted_list)
