# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        s=set(nums)
        temp=ListNode(0)
        temp.next=head
        curr=temp
        while curr.next:
            if curr.next.val in s:
                curr.next=curr.next.next
            else:
                curr=curr.next
        final=temp.next
        return final
            