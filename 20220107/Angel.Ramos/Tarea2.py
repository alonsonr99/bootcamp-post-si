import random

resultado=list()

y1=int(input("ingerse el numero de filas de la matriz 1\n"))
x1=int(input("ingrese el numero de columnas de la matriz 1\n"))
y2=x1
x2=int(input("ingrese el numero de columnas de la matriz 2\n"))

matriz1=list()
matriz2=list()

matriz1=[[random.randrange(1,3) for columna in range(x1)] for fila in range (y1)]
matriz2=[[random.randrange(1,3) for columna in range(x2)] for fila in range (y2)]


# Imprimir la matriz 1 y 2
print("matriz1")
for fila in range(y1):
    print("[", end=" ")
    for columna in range(x1):
        print("{:3d} ".format(matriz1[fila][columna]), end="")
    print("]")
print("\n")
print("matriz2")
for fila in range(y2):
    print("[", end=" ")
    for columna in range(x2):
        print("{:3d} ".format(matriz2[fila][columna]), end="")
    print("]")
resultadofila=int()

for linea in range(y1):
   
    for fila in range(y1):
        resultado.append([])
        
        for columna in range (x2): 
            resultadofila=resultadofila + matriz1[linea][columna]*matriz2[columna][fila]
            
        resultado[linea].append(resultadofila)           
        resultadofila=0
print("matriz resultante")
for fila in range(y1):
    print("[", end=" ")
    for columna in range(x2):
        print("{:3d} ".format(resultado[fila][columna]), end="")
    print("]")

