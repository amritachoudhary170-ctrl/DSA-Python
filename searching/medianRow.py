from bisect import bisect_right

def median(mat):
    row = len(mat)
    cols = len(mat[0])

    low = min(row[o] for row in mat)
    high = max(row[1] for row in mat)

    req = (row * cols +1)// 2

    while low <= high:
        mid = (low + high) // 2

        count = 0

        for row in mat:
            conut += bisect_right(row, mid)

        if count < req:
            low = mid + 1

        else:
            high = mid

    return low 

if __name__ == "_main__":
    mat = [[1, 2, 5], [2, 6, 9], [2, 6, 9]]

    print(median(mat))