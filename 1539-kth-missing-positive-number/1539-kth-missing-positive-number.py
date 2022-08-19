class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        prev_val = 1

        missing_vals = []
        while len(missing_vals) < k+1:
         
            if prev_val in arr:
                prev_val +=1
            else:
                missing_vals.append(prev_val)
                prev_val +=1
        
        return missing_vals[k-1]