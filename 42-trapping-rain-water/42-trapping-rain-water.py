class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:return 0
        
        max_right = height[len(height)-1]
        max_left = height [0]
        left = 0
        high = len(height)-1
        res = 0
        
        while left < high:
            
            if max_left <= max_right:
                left +=1
                max_left = max(max_left ,height[left] )
                res +=max_left - height[left]
                
            else:
                high -=1
                max_right = max(max_right ,height[high] )
                res +=  max_right - height[high]
                
        
        return res
                