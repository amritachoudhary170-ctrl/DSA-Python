#SMALLEST FIRST STABLE STATE

def firstStableIndex(nums, k):
    n = len(nums)

        # Minimum from i to the end
    right = [0] * n
    right[-1] = nums[-1]

    for i in range(n - 2, -1, -1):
        right[i] = min(nums[i], right[i + 1])

        # Maximum from 0 to i
    left = nums[0]

    for i in range(n):
        left = max(left, nums[i])

        if left - right[i] <= k:
            return i

    return -1

if __name__ == "__main__":
    # nums = [0,0]
    # k = 0

    print(firstStableIndex(nums=[0,0], k=0))

