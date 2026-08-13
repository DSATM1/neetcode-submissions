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
        # Hash map to map original nodes to their corresponding copy nodes
        # Base case: mapping None to None handles null pointers gracefully
        old_to_copy = {None: None}

        # First pass: Create a copy of each node and store in hash map
        curr = head
        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: Connect next and random pointers using the hash map
        curr = head
        while curr:
            copy_node = old_to_copy[curr]
            copy_node.next = old_to_copy[curr.next]
            copy_node.random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]