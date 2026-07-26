# Input: arr[] = {4, 6, 10, 12, 18, 20}, K = 6 
# Output: 
# Lower bound of 6 is 6 at index 1 
# Upper bound of 6 is 10 at index 2
# Input: arr[] = {4, 6, 10, 12, 18, 20}, K = 20 
# Output: 
# Lower bound of 20 is 20 at index 5 
# Upper bound doesn't exist 

def lower_bound(arr, k):
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

def upper_bound(arr, k):
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


arr = [4, 6, 10, 12, 18, 20]
k = int(input("Enter K: "))

lb = lower_bound(arr, k)
ub = upper_bound(arr, k)

if lb != len(arr):
    print(f"Lower bound of {k} is {arr[lb]} at index {lb}")
else:
    print("Lower bound doesn't exist")

if ub != len(arr):
    print(f"Upper bound of {k} is {arr[ub]} at index {ub}")
else:
    print("Upper bound doesn't exist")