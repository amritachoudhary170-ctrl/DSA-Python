# Aggressive Cows
# Last Updated : 14 Jul, 2026
# Given an integer array arr[], which denotes the positions of stalls. All the positions are distinct. There are k aggressive cows.

# Assign the cows to the stalls such that the minimum distance between any two cows is maximized.

# Examples: 
# Input: arr[] = [1, 2, 4, 8, 9], k = 3
# Output: 3
# Explanation: The first cow can be placed at arr[0], the second at arr[2], and the third at arr[3]. The minimum distance between any
# two cows is 3 (between arr[0] and arr[2]), which is the maximum possible among all valid arrangements



def check(arr, k , distance):
    count = 1
    prev = arr[0]

    for i in range(1, len(arr)):
        if arr[i] - prev >= distance:
            prev = arr[i]
            count += 1

    return count >= k

def aggressive_cows(arr, k):
    arr.sort()
    res = 0
    low = 1
    high = arr[-1] - arr[0]

    while low <= high:
        mid = low + (high - low)// 2

        if check(arr, k, mid):
            res = mid
            low = mid + 1

        else:
            high = mid - 1

    return res

if __name__ == "__main__":
    print(aggressive_cows(arr=[1,2,4,8,9] , k=3))