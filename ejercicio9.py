"""Realizar un algoritmo que dado un número entero, visualice en pantalla si es par o
impar. En el caso de ser 0, debe visualizar “el número no es par ni impar” (para que un
numero sea par, se debe dividir entre dos y que su resto sea 0)"""

print("Ingrese el numero a evaluar")
num=int(input())

if(num ==0):
    print("El cero no es par ni impar")
elif((num % 2)==0):
    print("El numero es par")
else:
    print("el numero es impar")

