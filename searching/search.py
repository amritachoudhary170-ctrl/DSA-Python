# Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3
# Output: 8
# Explanation: 3 is present at index 8.

# Input: arr[] = [3, 5, 1, 2], key = 6
# Output: -1
# Explanation: 6 is not present.

# Input: arr[] = [33, 42, 72, 99], key = 42
# Output: 1
# Explanation: 42 is found at index 1.

def search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low)//2
        
        if arr[mid] == key:
            return mid
        
        if arr[mid] >= arr[low]:

            if arr[low] <= key and arr[mid] > key:
                high = mid - 1

            else:
                low = mid + 1


        else:
            if arr[high] >= key and arr[mid] < key:
                low = mid + 1

            else:
                high = mid - 1

    return -1

if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 23
    print(search(arr, key))