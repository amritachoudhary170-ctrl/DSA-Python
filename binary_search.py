arr = [2,5,8,12,16,23,38,56,72,92]
target = 23

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high)//2

    if arr[mid] == target:
        print("Target is found", mid)
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid-1

else:
    print("Target is not found ")

