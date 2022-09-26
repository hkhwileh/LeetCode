class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x , y in points:
            z = (x**2)+(y**2)
            heap.append([z,x,y])
        
        heapq.heapify(heap)
        res = []
        for i in range(k):
            z,x,y = heapq.heappop(heap)
            res.append([x,y])
        
        return res