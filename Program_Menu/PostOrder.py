def PostOrder(root, lista):
    if not root:
        return
    PostOrder(root.left, lista)
    PostOrder(root.right, lista) 
    lista.append(root.data)