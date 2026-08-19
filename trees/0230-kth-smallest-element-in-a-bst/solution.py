# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current  = root
        order = []
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                r = stack.pop()
                order.append(r.val)
                current = r.right
            if len(order) == k:
                return order[k - 1]

