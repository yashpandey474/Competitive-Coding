class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        #BINARY REPRESENTATION MULTIPLICATION

        if n<0:
            x = 1/x

        y = 1
        n = abs(n)
        while n > 0:
            #CHECK LEAST SIGNIFICANT BIT
            if (n&1) != 0:
                y *= x
            
            x *= x
            #DIVIDE N BY 2
            n >>= 1

        return y

        
