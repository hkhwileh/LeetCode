class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i , v in enumerate(nums):
            temp = target - v
            if temp in d:
                return [i,d[temp]]
            d[v] = i