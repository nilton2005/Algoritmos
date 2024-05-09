def InOrder (root, lista):
    if not root:
        return
    InOrder(root.left, lista)
    lista.append(root.data)
    InOrder(root.right, lista)
    