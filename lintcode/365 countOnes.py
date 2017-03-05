import sys
class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        r = 0
        if num < 0:
        	r = 1
        num = num & sys.maxsize
        while num != 0:
        	r = r + (num & 1)
        	num = num >> 1
        return r
        