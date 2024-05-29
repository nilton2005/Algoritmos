def Buscar(lista, letra):
    if not lista:
        return False
    if lista[0]== letra:
        return True
    return Buscar(lista[1:], letra)
lista = ["a", "b", "c"]
letra = str(input("ingrese el elemento a busar "))
print(Buscar(lista, letra))

