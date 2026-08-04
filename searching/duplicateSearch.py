#SEARCH IN SORTED AND ROTATED ARRAY WITH DUPLICATES
#I/P: arr[] = [3,3,3,1,2,3], key = 3
#O/P: True

#I/P: arr[] = [3,3,3,1,2,3], key = 12
#O/P: False

def search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return True

        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1

        elif arr[low] <= arr[mid]:
            if arr[low] <= key < arr[mid]:
                high = mid - 1

            else:
                low = mid + 1

        else:
            if arr[mid] < key <= arr[high]:
                low = mid + 1

            else:
                high = mid - 1

    return False

if __name__ == "__main__":
    arr = [3,3,3,1,2,3]
    key = 3

    print(search(arr, key))
                