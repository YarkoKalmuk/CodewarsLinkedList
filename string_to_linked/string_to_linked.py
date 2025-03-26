class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    nodes = s.split(" -> ")
    nodes = [int(node) if node != "None" else None for node in nodes]

    head = None
    for node in reversed(nodes):
        if node is not None:
            head = Node(node, head)
    return head
