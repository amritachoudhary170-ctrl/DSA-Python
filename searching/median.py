# MEDIAN OF TWO SORTED ARRAYS OF DIFFERENT SIZE

# Input: a[] = [-5, 3, 6, 12, 15], b[] = [-12, -10, -6, -3, 4, 10]
# Output: 3
# Explanation: The merged array is [-12, -10, -6, -5 , -3, 3, 4, 6, 10, 12, 15]. So the median of the merged array is 3.

def findMedian(num1, num2):
    if len(num1)>len(num2):
        num1, num2 = num2, num1

    n1 = len(num1)
    n2 = len(num2)

    left = (n1 + n2 + 1) // 2

    low = 0
    high = n1

    while low <= high:
        cut1 = low + (high - low) // 2
        cut2 = left - cut1

        l1 = float('-inf') if cut1 == 0 else num1[cut1 - 1]
        r1 = float('inf') if cut1 == n1 else num1[cut1]

        l2 = float('-inf') if cut2 ==0 else num2[cut2 - 1]
        r2 = float('inf') if cut2 == n2 else num2[cut2]

        if l1 <= r2 and l2 <= r2:
            if (n1 + n2) % 2 == 1:
                return max(l1, l2)

            else:
                return (max(l1,l2) + min(r1, r2)) / 2

        elif l1 > r2:
            high = cut1 - 1

        else:
            low = cut1 + 1

if __name__ == "__main__":
    p= findMedian(num1= [-5, 3, 6, 12, 15], num2= [-12, -10, -6, -3, 4, 10])
    print(p)