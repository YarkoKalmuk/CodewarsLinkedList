def loop_size(node):
    slow = node.next
    fast = node.next.next
    while fast != slow:
        slow = slow.next
        fast = fast.next.next

    count = 1
    fast = fast.next
    while fast != slow:
        fast = fast.next
        count += 1
    return count