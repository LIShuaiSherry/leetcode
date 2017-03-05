# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if l == 0:
        	return None
        elif l == 1:
            return TreeNode(nums[0])
        else:
        	i = int((l+1)/2)-1
        	r = TreeNode(nums[i])
        	if i > 0:
        	    r.left = self.sortedArrayToBST(nums[:i])
        	r.right = self.sortedArrayToBST(nums[i+1:])
        return r
        