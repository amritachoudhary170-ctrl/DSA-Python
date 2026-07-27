#SEACH IN NORMAL SORTED ARRAY
# I/P: arr[] = [1,3,5,6], k=5
# O/P: 2

# I/P: arr[] = [1,3,4,5], k= 2
# O/P: 1

### Element 2 is not present but inserting at index is 1 i.e. arr[] = [1,3,6], k=5 the O/P will be 2

def search(arr, k):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) //2

        if arr[mid] == k:
            return mid

        elif arr[mid] > k:
            high = mid - 1

        else:
            low = mid + 1

    return low

if __name__ == "__main__":
    arr = [1,3,6]
    k = int(input('k: '))

    print(search(arr,k))