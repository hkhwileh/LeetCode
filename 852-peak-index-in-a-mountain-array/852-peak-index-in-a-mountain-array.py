class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) < 3:
            return 0
        
        low , high = 0, len(arr)-1
        
        while low <= high:
            mid = (low+high)//2
            
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            else:
                if arr[mid-1] < arr[mid] < arr[mid+1]:
                    low = mid +1
                else:
                    high = mid
                        
                    
