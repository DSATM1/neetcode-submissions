# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            # A node is "good" if its value is greater than or equal to the maximum seen so far on the path
            res = 1 if node.val >= max_val else 0
            
            # Update the maximum value seen along the current path
            max_val = max(max_val, node.val)
            
            # Traversal
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)
            
            return res

        return dfs(root, root.val)