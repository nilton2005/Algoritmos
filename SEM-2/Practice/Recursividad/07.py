def sumaLista(lista):
    if not lista:
        return 0
    else:
        return lista[0]+ sumaLista(lista[1:])
miLista = [1,2,3,4,5]
print(sumaLista(miLista))