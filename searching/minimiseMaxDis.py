# Minimize the maximum distance between adjacent points after adding K points anywhere in between

# Input: stations[] = {3, 6, 12, 19, 33}, K = 3
# Output: 6.00
# Explanation: The largest gap is 14 (between 19 and 33). Adding 2 stations there splits it into ≈4.67. 
# The next largest gap is 7 (between 12 and 19). Adding 1 station splits it into 3.5. Now the maximum gap left is 6.

import math

def possible(stations, k, mid):
    count = 0
    for i in range (len(stations)-1):
        gap = stations[1+i] - stations[i]
        count+= math.ceil(gap/mid) - 1

    return count <= k

def minimiseMaxDis(stations, k):
    low = 0
    high = 0

    for i in range (len(stations) - 1):
        high = max(high, stations[i+1] - stations[i])

    while high-low > 1e-6:
        mid = (low + high) / 2

        if possible(stations, k, mid):
            high = mid

        else:
            low = mid

    return round(high, 2)

if __name__ == "__main__":
    stations = [3,6,12,19,33]
    k = 3

    print(minimiseMaxDis(stations, k))
