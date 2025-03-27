class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def sorted_insert(head, data):
    if head is None:
        return Node(data, None)
    if head.data > data:
        return Node(data, head)

    prev = None
    current = head
    while current.data <= data:
        if current.next is None:
            current.next = Node(data, None)
            return head
        prev = current
        current = current.next
    prev.next = Node(data, current)
    return head

new = sorted_insert(Node(1, Node(2, Node(3, None))), 3.5)
print(new.next.next.next.data)
