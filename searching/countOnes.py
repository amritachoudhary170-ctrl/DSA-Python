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