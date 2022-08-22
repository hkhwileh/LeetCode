class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        temp = []

        for i, v in enumerate(mat):
            cnt = 0
            cnt2=0
            for n in v:
                if n == 1:
                    cnt +=1
            temp.append((cnt,i))
        temp = sorted(temp)
        index = []

        for i in range(k):
            index.append(temp[i][1])
        
        return index