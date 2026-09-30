#PREORDER TRAVERSAL

#RECURSIVE SOLUTION

class TreeNode:
    def __init__(self, val, right, left):
        self.val = val
        self.right = right
        self.left = left

class sol:
    def preorder(self, root):
        res = []

        def preorder(root):
            if not root:
                return

            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return res
        
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(-10, 10, 100)
# y = np.linspace(-10, 10, 100)

# xx, yy = np.meshgrid(x, y)

# # z = xx**2 + yy**2

# z = np.sin(xx) + np.cos(yy)
# z.shape

# fig = plt.figure(figsize=(12, 8))
# ax = plt.subplot(projection='3d')
# ax.plot_surface(xx,yy,z, cmap ='viridis')

# plt.show()