def binary_search(A, x):
    left = 0
    right = len(A)-1
    while left <= right:
        mid = (left + right)//2
        if A[mid] < x:
            left = mid + 1
        elif A[mid] > x:
            right = mid - 1
        else:
            return mid+1
    return len(A)

sorted_list = list(map(int, input("Put in a sorted list of integers, seperated by spaces: -> ").split(" ")))
wanted = int(input("Put in the number you're looking for!"))
print("The number you're looking for is at Position: ",binary_search(sorted_list, wanted))
