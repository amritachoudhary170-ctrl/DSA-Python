# 1945. Sum of Digits of String After Convert

# Example 1:
# Input: s = "iiii", k = 1

# Output: 36

# Explanation:

# The operations are as follows:
# - Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
# - Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
# Thus the resulting integer is 36.

class Solution:
    def getLucky(self, s: str, k: int) -> int:

        num = ""

        for ch in s:
            num += str(ord(ch) - ord('a') + 1)

        num = int(num)

        for i in range(k):
            total = 0

            while num > 0:
                total += num % 10

                num //= 10

            num = total

        return num