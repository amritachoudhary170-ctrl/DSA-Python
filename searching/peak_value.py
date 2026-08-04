def peak(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + ( high - low ) // 2

        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return mid

        elif arr[mid] < arr[mid + 1]:
            low = mid + 1

        else:
            high = mid 

    return low

if __name__ == "__main__":
    arr = [1,2,4,5,7,8,3]

    print(peak(arr))