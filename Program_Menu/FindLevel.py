def FindLevel(root, element, level=1):

    if root is None:
        return -1

    if root.data == element:
        return level

    left_level = FindLevel(root.left, element, level + 1)
    if left_level != -1:
        return left_level

    right_level = FindLevel(root.right, element, level + 1)
    return right_level
