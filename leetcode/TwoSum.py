def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    s = sorted(nums)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] + s[j] > target:
            j = j - 1
        elif s[i] + s[j] < target:
            i = i + 1
        else:
            i = nums.index(s[i]) + 1
            nums.reverse()
            j = len(s) - nums.index(s[j])
            index = [i,j]
            index.sort()
            return index