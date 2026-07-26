# Unbounded Binary Search

#  Keep doubling high until f(high) becomes positive. Example: 
# high = 1 (Negative)
# high = 2 (Negative)
# high = 4 (Negative)
# high = 8 (Negative) #LOW
# high = 16 (Positive) #HIGH

#  -> low = high // 2

# Apply Binary Search b/w low and high 

def f(x):
    return x * x - 10 * x - 20

def findFirstPositive():
    if f(0) > 0:
        return 0 
    
    i = 1
    while f(i) <= 0:
        i = i * 2

    return binarySearch(i/2 , i)

def binarySearch(low, high):

    ans = -1

    if low <= high:
        mid = low + (high - low) // 2

        if f(mid) > 0:
            ans = mid
            high = mid - 1

        else:
            low = mid - 1

    return ans

print ("The value n where f() becomes "+"positive first is ", int(findFirstPositive())) 