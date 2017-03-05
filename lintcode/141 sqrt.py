class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x == 0:
            return x
        a = 1
        b = x
        while a < b - 1:
            r = int((a+b)/2)
            if r ** 2 > x:
                b = r - 1
            else:
                a = r
        if b ** 2 < x:
            return b
        else:
            return a