# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build(preorder: list[int], inorder: list[int]):
            if not inorder:
                return None
            if not preorder:
                return None
            root = TreeNode(preorder[0])
            root_idx = inorder.index(preorder[0])
            left_io = inorder[:root_idx]
            if left_io:
                root.left = build(preorder[1:1 + len(left_io)], left_io)
                right_io = inorder[root_idx + 1:]
                root.right = build(preorder[1 + len(left_io):], right_io)
            else:
                root.left = None
                root.right = build(preorder[1:], inorder[root_idx + 1:])
            return root
        return build(preorder, inorder)
