# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []
        if not root:
            return 0
        def go(root):
            nonlocal k
            if not root:
                return
            go(root.left)
            order.append(root.val)
            go(root.right)
        go(root)
        return order[k-1]
