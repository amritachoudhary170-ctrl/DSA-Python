# INORDER TRAVERSAL
# ITERATIVE SOLUTION
# For example of a tree -
#https://assets.leetcode.com/uploads/2024/08/29/tree_2.png

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,2,6,5,7,1,3,9,8]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):

        res = []
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)

        return res

    