#The trick here was to add the extra variable val=None in the function argument to use the previous value every single time for comparison. 
#Time taken: Your code took 37 milliseconds — faster than 54.28% in Python

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, val=None):
        if not root:
            return True
        if val is None:
            val = root.val
        return root.val == val and self.solve(root.left, val) and self.solve(root.right, val)
        
