class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head

    casual = Node(0)
    casual.next = head
    prev = casual
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return casual.next
a = swap_pairs(Node(1, Node(2, Node(3, Node(4)))))
print(a.data, a.next.data, a.next.next.data, a.next.next.next.data)