# Find the minimum element present in the array
# Input: arr[] = [5, 6, 1, 2, 3, 4]
# Output: 1
# Explanation: 1 is the minimum element present in the array.

# Input: arr[] = [3, 1, 2]
# Output: 1
# Explanation: 1 is the minimum element present in the array.

def findMin(arr):
    
    n =  len(arr)
    low = 0
    high = n - 1
    while low < high:

        if arr[low] < arr[high]:
            return arr[low]
        
        mid = low + (high - low) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        
        else:
            high = mid

    return arr[low]

if __name__ == "__main__":
    arr = [5, 6, 1, 2, 3, 4]
    print(findMin(arr))