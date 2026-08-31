"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        mapping = {}

        curr = head

        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            mapping[curr].next = mapping.get(curr.next)
            mapping[curr].random = mapping.get(curr.random)
            curr = curr.next

        return mapping[head]
        