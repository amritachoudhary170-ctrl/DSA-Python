#ITERATIVE SOLUTION

class treenode:
    def __init__(self, right, left, val):
        self.right = right
        self.left = left
        self.val = val

class solution:
    def postorder(self, root):
        stack = [root]
        visit = [False]
        res = []

        while stack:
            curr, v = stack.pop(), visit.pop()

            if curr:
                if v:
                    res.append(curr.val)

                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)

        return res
    