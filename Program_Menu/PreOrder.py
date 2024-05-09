from  BinaryTreeNode import BinaryTreeNode

def RecorridoPreOrden(root, result):
    if not root:
        return
    

    result.append(root.data)
    RecorridoPreOrden(root.left, result)
    RecorridoPreOrden(root.right, result)