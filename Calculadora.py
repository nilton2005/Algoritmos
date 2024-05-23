import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def eval(self):
        if self.right is not None and self.left is not None:
            if self.value == '+':
                return self.left.eval() + self.right.eval()
            elif self.value == '*':
                return self.left.eval() * self.right.eval()
            elif self.value == '-':
                return self.left.eval() - self.right.eval()
            elif self.value == '/':
                return self.left.eval() / self.right.eval()
            elif self.value == '^':
                return self.left.eval() ** self.right.eval()
        else:
            return float(self.value)

operatorPrecedence = {
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '^' : 3
}

def parserPostfixToBinaryTree(postfix):
    stack = []
    for char in postfix:
        if char not in operatorPrecedence:
            node = Node(char)
            stack.append(node)
        else:
            node = Node(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack.pop()

def postfixConvert(infix):
    stack = []
    postfix = [] 
    number = ""
         
    for char in infix:
        # Manejo de dígitos
        if char.isdigit() or char == '.':
            number += char
        elif char in operatorPrecedence:
            if number:
                postfix.append(number)
                number = ""
            if char == '(':
                stack.append(char)
            elif char == ')':
                while stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()  
            else:
                while (stack and stack[-1] != '(' and 
                       operatorPrecedence[char] <= operatorPrecedence.get(stack[-1], 0)):
                    postfix.append(stack.pop())
                stack.append(char)
    
    if number:
        postfix.append(number)
    
    while stack:
        postfix.append(stack.pop())
        
 
    return postfix

def calcular():
    formula = entrada_formula.get()
    try:
        postfix = postfixConvert(formula)
        rootNode = parserPostfixToBinaryTree(postfix)
        resultado = rootNode.eval()
        etiqueta_resultado.config(text="Resultado: " + str(resultado))
    except Exception as e:
        messagebox.showerror("Error", "Error en la fórmula: " + str(e))


ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x300")  # Tamaño de la ventana

def agregar_caracter(caracter):
    entrada_formula.insert(tk.INSERT, caracter)

font_style = ("Helvetica", 12)


button_style = {"font": font_style, "width": 5, "height": 2, }


entrada_formula = tk.Entry(ventana, font=font_style)
entrada_formula.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


for i in range(10):
    tk.Button(ventana, text=str(i), command=lambda i=i: agregar_caracter(str(i)), **button_style).grid(row=(i//3)+1, column=i%3, padx=5, pady=5)


operadores = ["+", "-", "*"]
for i, operador in enumerate(operadores):
    tk.Button(ventana, text=operador, command=lambda operador=operador: agregar_caracter(operador), **button_style).grid(row=i+1, column=3, padx=5, pady=5)
tk.Button(ventana, text="/", command=lambda: agregar_caracter("/"), **button_style).grid(row=4, column=2, padx=5, pady=5)

tk.Button(ventana, text="^", command=lambda: agregar_caracter("^"), **button_style).grid(row=4, column=1, padx=5, pady=5)

tk.Button(ventana, text="=", command=calcular, **button_style).grid(row=4, column=3, padx=5, pady=5)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, font=font_style)
etiqueta_resultado.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()