# sq rt
# Input: n = 4
# Output: 2
# Explanation: The square root of 4 is 2.

# Input: n = 11
# Output: 3
# Explanation: The square root of 11 lies in between 3 and 4 so floor of the square root is 3.

def floorSquare(n):
    low = 1
    high = n
    res = 1

    while low <= high:
        mid = low + (high - low) // 2

        if mid * mid <= n:
            res = mid
            low = mid + 1
           
        else:
            high = mid - 1

    return res

if __name__ == "__main__":
    n = 16
    print(floorSquare(n))