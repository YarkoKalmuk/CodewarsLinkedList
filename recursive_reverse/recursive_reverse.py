class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverse(head):
    if not head or not head.next:
        return head

    def reverse_helper(node):
        if not node or not node.next:
            return node
        new_head = reverse_helper(node.next)
        node.next.next = node
        node.next = None
        return new_head

    return reverse_helper(head)
