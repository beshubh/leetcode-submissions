# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def go(po, io):
            if not po or not io:
                return None
            root = TreeNode(po[0]) 
            idx = io.index(po[0])
            left_io = io[:idx]
            right_io = io[idx + 1:]
            left_po = po[1:len(left_io) + 1]
            right_po = po[len(left_io) + 1:]
            root.left = go(left_po, left_io)
            root.right = go(right_po, right_io)
            return root
        return go(preorder, inorder) 
