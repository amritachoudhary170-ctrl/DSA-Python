# ALLOCATE MINIMUM PAGES

# Input: arr[] = [12, 34, 67, 90], k = 2
# Output: 113
# Explanation: Books can be distributed in following ways:

# [12] and [34, 67, 90] - The maximum pages assigned to a student is  34 + 67 + 90 = 191.
# [12, 34] and [67, 90] - The maximum pages assigned to a student is 67 + 90 = 157.
# [12, 34, 67] and [90] - The maximum pages assigned to a student is 12 + 34 + 67 = 113.
# The third combination has the minimum pages assigned to a student which is 113.

def canAllocate(arr, k, limit):
    students = 1
    pages = 0

    for book in arr:

        if pages + book <= limit:
            pages += book
        else:
            students += 1
            pages = book

    return students <= k


def findPages(arr, k):

    if k > len(arr):
        return -1

    low = max(arr)
    high = sum(arr)
    answer = high

    while low <= high:

        mid = (low + high) // 2

        if canAllocate(arr, k, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


arr = [12, 34, 67, 90]
k = 2

print(findPages(arr, k))
