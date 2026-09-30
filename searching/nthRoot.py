# CALCULATING N-TH REAL ROOT USING BINARY SEARCH

# I/P: x=5, n=2
# O/P: 2.236067....
# EXP: we want to find:
#     which nno, when multiplied by itself 2 times, becomes 5

def nthRoot(x, n):
    low = 0
    high = x

    while high - low > 1e-7:
        mid = (low + high) / 2

        if mid**n < x:
            low = mid

        else:
            high = mid

    return low

if __name__ == "__main__":
    x = 5
    n= 2

    print(nthRoot(x,n))
