from BinaryTreeNode import BinaryTreeNode
from PreOrder import RecorridoPreOrden
from InOrder import InOrder
from PostOrder import PostOrder
from FindLevel import FindLevel

# AGREGANDO DATOS
# para el 2do nivel
SubArbolIzquierdo_1 = BinaryTreeNode(2)
SubArbolDerecho_2 = BinaryTreeNode(3)

# para el 3er nivel

SubArbolIzquierdo_1_1 = BinaryTreeNode(4)
SubArbolIzquierdo_1_2 = BinaryTreeNode(5)

SubArbolDerecho_2_1 = BinaryTreeNode(6)
SubArbolDerecho_2_2 = BinaryTreeNode(7)

# para el 4to nivel

SubArbolIzquierdo_1_1_1 = BinaryTreeNode(8)
SubArbolIzquierdo_1_1_2 = BinaryTreeNode(9)

SubArbolIzquierdo_1_2_1 = BinaryTreeNode(10)
SubArbolIzquierdo_1_2_2 = BinaryTreeNode(11)


SubArbolDerecho_2_1_1 = BinaryTreeNode(12)
SubArbolDerecho_2_1_2 = BinaryTreeNode(13)

SubArbolDerecho_2_2_1 = BinaryTreeNode(14)
SubArbolDerecho_2_2_2 = BinaryTreeNode(15)

# para el 5to nivel

SubArbolIzquierdo_1_1_1_1 = BinaryTreeNode(16)
SubArbolIzquierdo_1_1_1_2 = BinaryTreeNode(17)

SubArbolIzquierdo_1_1_2_1 = BinaryTreeNode(18)
SubArbolIzquierdo_1_1_2_2 = BinaryTreeNode(19)

SubArbolIzquierdo_1_2_1_1 = BinaryTreeNode(20)
SubArbolIzquierdo_1_2_1_2 = BinaryTreeNode(21)

SubArbolIzquierdo_1_2_2_1 = BinaryTreeNode(22)
SubArbolIzquierdo_1_2_2_2 = BinaryTreeNode(23)

SubArbolDerecho_2_1_1_1 = BinaryTreeNode(24)
SubArbolDerecho_2_1_1_2 = BinaryTreeNode(25)

SubArbolDerecho_2_1_2_1 = BinaryTreeNode(26)
SubArbolDerecho_2_1_2_2 = BinaryTreeNode(27)

SubArbolDerecho_2_2_1_1 = BinaryTreeNode(28)
SubArbolDerecho_2_2_1_2 = BinaryTreeNode(29)

SubArbolDerecho_2_2_2_1 = BinaryTreeNode(30)
SubArbolDerecho_2_2_2_2 = BinaryTreeNode(31)

# Creando el albrol (uniendo nodos)

# hojas para el Sub arbol 2

SubArbolIzquierdo_1.left = SubArbolIzquierdo_1_1

SubArbolIzquierdo_1.right = SubArbolIzquierdo_1_2


# hojas para el Sub arbol 3

SubArbolDerecho_2.left = SubArbolDerecho_2_1

SubArbolDerecho_2.right = SubArbolDerecho_2_2


# hojas para el Sub arbol 4

SubArbolIzquierdo_1_1.left = SubArbolIzquierdo_1_1_1
SubArbolIzquierdo_1_1.right = SubArbolIzquierdo_1_1_2

SubArbolIzquierdo_1_2.left = SubArbolIzquierdo_1_2_1
SubArbolIzquierdo_1_2.right = SubArbolIzquierdo_1_2_2


# hojas para el Sub arbol 5

SubArbolDerecho_2_1.left = SubArbolDerecho_2_1_1
SubArbolDerecho_2_1.right = SubArbolDerecho_2_1_2

SubArbolDerecho_2_2.left = SubArbolDerecho_2_2_1
SubArbolDerecho_2_2.right = SubArbolDerecho_2_2_2


# hojas para el Sub arbol 6

SubArbolIzquierdo_1_1_1.left = SubArbolIzquierdo_1_1_1_1
SubArbolIzquierdo_1_1_1.right = SubArbolIzquierdo_1_1_1_2

SubArbolIzquierdo_1_1_2.left = SubArbolIzquierdo_1_1_2_1
SubArbolIzquierdo_1_1_2.right = SubArbolIzquierdo_1_1_2_2

SubArbolIzquierdo_1_2_1.left = SubArbolIzquierdo_1_2_1_1
SubArbolIzquierdo_1_2_1.right = SubArbolIzquierdo_1_2_1_2

SubArbolIzquierdo_1_2_2.left = SubArbolIzquierdo_1_2_2_1
SubArbolIzquierdo_1_2_2.right = SubArbolIzquierdo_1_2_2_2

# hojas para el Sub arbol 7

SubArbolDerecho_2_1_1.left = SubArbolDerecho_2_1_1_1
SubArbolDerecho_2_1_1.right = SubArbolDerecho_2_1_1_2

SubArbolDerecho_2_1_2.left = SubArbolDerecho_2_1_2_1
SubArbolDerecho_2_1_2.right = SubArbolDerecho_2_1_2_2

SubArbolDerecho_2_2_1.left = SubArbolDerecho_2_2_1_1
SubArbolDerecho_2_2_1.right = SubArbolDerecho_2_2_1_2

SubArbolDerecho_2_2_2.left = SubArbolDerecho_2_2_2_1
SubArbolDerecho_2_2_2.right = SubArbolDerecho_2_2_2_2

# formualario
salir = True
sesion = 0
while salir:
    sesion += 1
    print("-- Arboles, sesion N°", sesion)
    opcion = int(input("Ver Arbol completa: (1)\nVer nivel (2)\nSalir: (3)\n"))
    
    if opcion == 1:
        print("De que forma quisiera visualizarlos")
        forma = int(input("1. Preorden\n2. Inorden\n3. Postorden\n"))
        if forma == 1:
            root = BinaryTreeNode(1, SubArbolIzquierdo_1, SubArbolDerecho_2)
            result = []
            RecorridoPreOrden(root, result)
            print(result)
            
        if forma == 2:
            root = BinaryTreeNode(1, SubArbolIzquierdo_1, SubArbolDerecho_2)
            result = []
            InOrder(root, result)
            print(result) 
        if forma == 3:
            root = BinaryTreeNode(1, SubArbolIzquierdo_1, SubArbolDerecho_2)
            result = []
            PostOrder(root, result)
            print(result)
    elif opcion == 2:
            root = BinaryTreeNode(1, SubArbolIzquierdo_1, SubArbolDerecho_2)
            elemento = int(input("Ingrese el elemento para ver en qué nivel está: "))
            level = FindLevel(root, elemento)
            if level == -1:
                print("El elemento no se encuentra en el árbol.")
            else:
                print("El elemento", elemento, "está en el nivel", level, "del árbol.")
    elif opcion == 3:
        print("Thank you so much, come son")
        salir = False
    else:
        print("Opción inválida")
