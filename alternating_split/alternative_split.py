
class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError
    f = head
    s = head.next
    f_cur = f
    s_cur = s
    while True:
        f_cur.next = s_cur.next
        if s_cur.next is None:
            break
        if s_cur.next.next is None:
            f_cur.next.next = None
            s_cur.next = None
            break
        s_cur.next = s_cur.next.next
        f_cur, s_cur = f_cur.next, s_cur.next
    return Context(f, s)
a = alternating_split(Node(1, Node(2, Node(3))))
print(a.first.data, a.first.next.data)
print(a.second.data)
