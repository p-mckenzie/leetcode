class ListNode:
    # credit to https://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"
    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return NotImplemented
        return str(self) == str(other)

class Solution:
    def middleNode(self, head):
        
        depth = 0
        node_depth = dict()
        while head:
            node_depth[depth] = head
            
            depth += 1
            head = head.next

        return node_depth[(depth//2)] if depth%2==0 else node_depth[(depth//2)]
