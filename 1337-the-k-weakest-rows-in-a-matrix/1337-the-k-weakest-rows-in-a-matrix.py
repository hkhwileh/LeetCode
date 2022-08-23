class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        #To understand the approach better let us use the same example for better understanding. Count the number of ones in each row. 
        ans={}
        for i in range(len(mat)):
            ans[i]=sum(mat[i])
        ans=sorted(ans, key=ans.get)
        return ans[:k]