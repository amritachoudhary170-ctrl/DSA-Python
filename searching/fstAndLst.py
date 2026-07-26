# Input : arr[] = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5
# Output : [2, 5]
# Explanation: First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5

# Input : arr[] = [1, 3, 5, 5, 5, 5, 7, 123, 125 ], x = 7
# Output : [6, 6]
# Explanation: First and last occurrence of 7 is at index 6

# Input: arr[] = [1, 2, 3], x = 4
# Output: [-1, -1]
# Explanation: No occurrence of 4 in the array, so, output is [-1, -1]


def findLast(arr, x):
    n = len(arr)
    left = 0
    right = n - 1
    last = -1
    while left <= right:
        mid = left + (right - left) // 2

        if x == arr[mid]:
            last = mid
            left = mid + 1

        elif x < arr[mid]:
            right = mid - 1

        else:
            left = mid + 1
    return last

def findFirst(arr, x):
    n = len(arr)
    left = 0
    right = n - 1
    first = -1
    
    while left <= right:
        mid = left + (right - left) // 2

        if x == arr[mid]:
            first = mid
            right = mid - 1

        elif x > arr[mid]:
            left =  mid + 1

        else:
            right = mid - 1
    return first

def find(arr, x):
    n = len(arr)
    first = findFirst(arr, x)
    last = findLast(arr, x)

    result = [first, last]
    return result

if __name__ == "__main__":
    arr = [3, 4, 5, 5, 5, 5, 7, 123, 125]
    x = 5
    result = find(arr, x)
    print(result[0], result[1])