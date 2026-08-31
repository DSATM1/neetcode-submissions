# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map values to their indices in the inorder traversal for O(1) lookup
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        
        # Keep track of the current index in the preorder array
        self.pre_idx = 0
        
        def helper(left: int, right: int) -> Optional[TreeNode]:
            # If there are no elements to construct the subtree
            if left > right:
                return None
            
            # The current root value is the next element in the preorder traversal
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            root = TreeNode(root_val)
            
            # Split the inorder array into left and right subtrees using the hash map
            mid = inorder_idx[root_val]
            
            # Recursively build the left and right subtrees
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root

        return helper(0, len(inorder) - 1)