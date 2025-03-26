
class Node:
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None:
        raise Exception
    current = node
    while current.next is not None and index>0:
        current = current.next
        index -= 1
    if index != 0:
        raise Exception
    return current

linked_list = Node(1, Node(2, Node(3, None)))
print(get_nth(linked_list, 2).data)
