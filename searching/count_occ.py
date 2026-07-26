
# Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
# Output: 4
# Explanation: 2 occurs 4 times in the given array.

# Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
# Output: 0
# Explanation: 4 is not present in the given array.


# METHOD 01
# from bisect import bisect_left, bisect_right
# def countOcc(arr, target):
#     left = bisect_left(arr, target)
#     right = bisect_right(arr, target)

#     return right - left

# if __name__ == "__main__":
#     arr = [1, 1, 2, 2, 2, 2, 3]
#     target = 2
#     print(countOcc(arr, target))

# MWTHOD 02
def lower_bound(arr, target):
    res = len(arr)
    low = 0
    high = res - 1
     
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] >= target:
            res = mid
            high = mid - 1

        else:
            low = mid + 1
    return res

def upper_bound(arr, target):
    res = len(arr)
    low = 0
    high = res - 1
     
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] > target:
            res = mid
            high = mid - 1

        else:
            low = mid + 1
    return res

def findocc(arr, target):
    res = len(arr)
    lower = lower_bound(arr, target)
    upper = upper_bound(arr, target)

    final = upper - lower
    return final 


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 2, 2, 3, 3]
    target = 2

    final = findocc(arr, target)
    print(final)
