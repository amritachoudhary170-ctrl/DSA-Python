# CAPACITY OF SHIP PACKAGES IN D DAYS

# Input: weights[] = [1, 2, 3, 4, 5, 6, 7], d = 5
# Output: 7
# Explanation:

# Day 1: Load the boat with packages [1, 2, 3] (total weight = 6).
# Day 2: Load the boat with package [4] (total weight = 4).
# Day 3: Load the boat with package [5] (total weight = 5).
# Day 4: Load the boat with package [6] (total weight = 6).
# Day 5: Load the boat with package [7] (total weight = 7).
# The minimum capacity of boat needed is 7. With this capacity, we can ship all packages within 5 days by 
# optimally distributing the packages as shown above.

def possible(weights, days, capacity):
    currentWeight = 0
    requiredDays = 1

    for weight in weights:
        if currentWeight + weight <= capacity:
            currentWeight += weight

        else:
            requiredDays += 1
            currentWeight = weight 

    return requiredDays <= days

def shipWithinDays(weights, days):
    low = max(weights)
    high = sum(weights)

    ans = high 

    while low <= high:
        mid = (low + high) // 2

        if possible(weights, days, mid):
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    return ans 

if __name__ == "__main__":
    weights = [3,2,2,4,1,4]
    days = 3

    print(shipWithinDays(weights, days))