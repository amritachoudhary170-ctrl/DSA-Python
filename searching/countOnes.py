# Input: arr[] = [1, 1, 0, 0, 0, 0, 0]
# Output: 2
# Explanation: Count of 1's in the given array is 2.

# Input: arr[] = [1, 1, 1, 1, 1, 1, 1]
# Output: 7

# Input: arr[] = [0, 0, 0, 0, 0, 0, 0]
# Output: 0

def countOnes(arr):
    n = len(arr)
    low = 0
    high = n - 1
    res = n
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == 0:
            res = mid
            high = mid - 1

        else:
            low = mid + 1
    return res
if __name__ == "__main__":

    arr = [0, 0, 0, 0, 0]
    print(countOnes(arr))