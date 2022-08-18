class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <=1:
            return True
        
        low, high = 0, num-1
        
        while low <=high:
            mid= (low+high)//2
            
            square = mid*mid
            
            if square==num:
                return True
            else:
                if square<num:
                    low = mid +1
                else:
                    high = mid -1
                    
        
        return False