#RECURSIVE SOLUTION 

class treenode:
    def __init__(self, right, left, val):
        self.right = right
        self.left = left
        self.val = val

class solution:
    def postorder(self, root):
        res = []

        def postorder(root):
            if not root:
                return 

            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res