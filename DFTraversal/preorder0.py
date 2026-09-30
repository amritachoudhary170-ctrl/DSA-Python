#RECURSIVE SOLUTION 

class treeNode:
    def __init__(self, right, left, val):
        self.right = right
        self.left = left
        self.val = val

class solution:
    def preorder(self, root):
        curr, stack = root, []
        res = []

        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left

            else:
                curr = stack.pop()

        return res