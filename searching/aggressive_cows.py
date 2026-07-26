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