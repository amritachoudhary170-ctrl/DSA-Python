# K-th Element of Merged Two Sorted Arrays

# Examples: 

# Input: a[] = [2, 3, 6, 7, 9], b[] = [1, 4, 8, 10], k = 5
# Output: 6
# Explanation: The final sorted array is [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element is 6.

def kthElement(a,b,k):
    if len(a)> len(b):
        a,b = b,a

    n1 = len(a)
    n2 = len(b)

    low = max(0, k-n1)
    high = min(k, n1)

    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k- cut1

        leftA = float('-inf') if cut1 == 0 else a[cut1 - 1]
        rightA = float('inf') if cut1 == n1 else a[cut1]

        leftB = float('-inf') if cut2 == 0 else b[cut2 - 1]
        rightB = float('inf') if cut2 == n2 else b[cut2]

        if leftA <= rightB and leftB <= rightA:
            return max(leftA, leftB)

        elif leftA > rightB:
            high = cut1 - 1

        else:
            low = cut1 + 1

    return -1

if __name__ == "__main__":
    a = [2,3,6,7,9]
    b = [1,4,8,10]
    k = 5
    print(kthElement(a,b,k))