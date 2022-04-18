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
    def removeNthFromEnd(self, head, n):
        
        depth = 0
        node_depth = dict()
        while head:
            node_depth[depth] = head
            
            depth += 1
            head = head.next

        if depth-n > 0:
            # given node, point prior node to posterior node (skipping it)
            node_depth[depth-n-1].next = node_depth[depth-n+1] if depth-n+1 in node_depth else None
        elif depth-n == 0:
            # node is first, so start the chain at 1 instead
            node_depth[0] = node_depth[1] if 1 in node_depth else None
        else:
            # no nodes remaining
            return None
        
        return node_depth[0]