def check(arr, mid, k):
    totalHr = 0
    for i in range(len(arr)):
        totalHr += (arr[i] + mid - 1) // mid

    return totalHr <= k

def kokoEat(arr, k):
    low = 1
    high = max(arr)
    res = high

    while low <= high:
        mid = low + (high - low) // 2

        if check(arr, mid, k) == True:
            high = mid - 1
            res = mid
        else:
            low = mid + 1

    return res

if __name__ == "__main__":
    arr = [5, 10, 3]
    k = 4
    print(kokoEat(arr, k))