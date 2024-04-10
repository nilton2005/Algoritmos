class Node:
     def __init__(self):
          self.data = None
          self.next = None
     def setData(self, data):
          self.data = data
     def getData(self):
          return self.data

     def setNext(self, nodo):
          self.next = nodo
     def getNext(self):
          return self.next
     def hasNext(self):
          return self.next is not None
     
     

class LinkedList:
     def __init__(self):
          self.head = None
          self.length = 0
     def print(self, nodo):
          nodo = self.head

          while nodo != None:
               print(nodo.getData(), end="=>")
               nodo = nodo.getNext()

          print("null")


    #AQUI LE AGREGAS LOS METODOS QUE DE DICE