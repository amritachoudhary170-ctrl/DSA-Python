# arr = [2,5,8,12,16,23,38,56,72,92]
# target = 23

# low = 0
# high = len(arr) - 1

# while low <= high:
#     mid = (low + high) //2
#     if arr[mid] == target:
#         print("Target is found", mid)
#         break
#     elif arr[mid] < target:
#         low = mid + 1

#     else:
#         high = mid-1

# else:
#     print("Target is not found ")

import bisect
arr = [1,3,4,4,5]
print(bisect.bisect(arr,4))
print(arr)
print(bisect.bisect(arr,4,0,3))
print(arr)