def stringify(node):
    result = ""
    current = node
    while current is not None:
        result += f"{current.data} -> "
        current = current.next
    result += "None"
    return result
