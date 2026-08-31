# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        pos = 1
        prev = head
        curr = head.next
        critical = []

        while curr and curr.next:
            nxt = curr.next
            if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
                critical.append(pos)
            prev, curr = curr, nxt
            pos += 1

        if len(critical) < 2:
            return [-1, -1]

        minDist = min(b - a for a, b in zip(critical, critical[1:]))
        maxDist = critical[-1] - critical[0]
        return [minDist, maxDist]
