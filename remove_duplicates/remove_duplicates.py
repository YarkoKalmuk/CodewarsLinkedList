class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    if head is None:
        return None
    prev = None
    cur = head
    visited = set()
    while cur is not None:
        if cur.data in visited:
            prev.next = cur.next if cur.next is not None else None
            cur = prev.next
            continue
        visited.add(cur.data)
        prev, cur = cur, cur.next
    return head
