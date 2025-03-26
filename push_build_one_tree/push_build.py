class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def push(head, data):
    return Node(data, head)


def build_one_two_three():
    head = None
    for node in range(3, 0, -1):
        head = Node(node, head)
    return head
