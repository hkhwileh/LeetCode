class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1], reverse = True)
        
        boxs = 0
        
        for box , unit in boxTypes:
            if truckSize > box:
                boxs += (box*unit)
                truckSize -= box
            else:
                boxs += truckSize * unit
                return boxs
        return boxs
        
