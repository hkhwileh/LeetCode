"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        OldCopyList = {None:None}
        
        cur = head
        
        while cur:
            copy = Node(cur.val)
            OldCopyList[cur] = copy
            cur = cur.next
        
        cur = head
        
        while cur:
            copy = OldCopyList[cur]
            copy.next = OldCopyList[cur.next]
            copy.random = OldCopyList[cur.random]
            cur = cur.next
        
        return OldCopyList[head]