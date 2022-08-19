class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        h = len(arr)-1
        prev_val = 1
        max_val = arr[h]
        missing_vals = []
        while len(missing_vals) < k+1:
         
            if prev_val in arr:
                prev_val +=1
            else:
                missing_vals.append(prev_val)
                prev_val +=1
        
        return missing_vals[k-1]