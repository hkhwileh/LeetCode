class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        #To understand the approach better let us use the same example for better understanding. Count the number of ones in each row. 
        ones = []
        indexs = []
        
        for index , val in enumerate(mat):
            cnt = 0
            for v in val:
                if v == 1:
                    cnt +=1
            
            ones.append((cnt,index))
        print(ones)
        ones = sorted(ones)
        
        for i in range(k):
            indexs.append(ones[i][1])
        
        return indexs