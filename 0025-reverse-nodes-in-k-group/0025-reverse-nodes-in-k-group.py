class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        
        prev_group = dummy

        while True:
            kth = prev_group

            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            next_group = kth.next

            prev = next_group
            curr = prev_group.next

            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp