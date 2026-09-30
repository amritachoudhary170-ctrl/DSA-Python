# Peak in 2D array/matrix

# Input: mat[][] = [[10, 20, 15],
#                   [21, 30, 14],
#                   [7,  16, 32]]
# Output: [1, 1]
# Explanation:  The value at index {1, 1} is 30, which is greater than or equal to all its valid neighbors:
# Left = 21, Right = 14, Top = 20, Bottom = 16. So, it satisfies the peak condition. Alternatively, {2, 2} with 
# value 32 also qualifies as a peak.

def findPeakGrid(mat):
    rows = len(mat)
    cols = len(mat[0])

    low = 0
    high = cols - 1

    while low <= high :
       mid = (low + high) // 2

       matRow = 0
       for i in range(rows):
           if mat[i][mid] > mat[matRow][mid]:
              matRow = i

       left = mat[matRow][mid-1] if mid > 0 else -1
       right = mat[matRow][mid+1] if mid < cols - 1 else -1

       if mat[matRow][mid] >= left and mat[matRow][mid] >= right:
           return [matRow, mid]

       elif left > mat[matRow][mid]:
           high = mid - 1

       else:
           low = mid + 1

if __name__ == "__main__":
    mat =[[41,8,2,48,18],[16,15,9,7,44],[48,35,6,38,28],[3,2,14,15,33],[39,36,13,46,42]]

    peak = findPeakGrid(mat)
    print(f"{(peak[0])}, {(peak[1])}")