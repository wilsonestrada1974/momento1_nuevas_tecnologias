""" Modificar el algoritmo anterior, de forma que si se teclea un cero, se vuelva a pedir
el número por teclado (así hasta que se teclee un número mayor que cero) (recuerda
la estructura mientras)."""

print("Ingrese el numero a evaluar")
num=int(input())

while(num <= 0):
    print("Ingrese el numero a evaluar")
    num=int(input())

if((num % 2)==0):
    print("El numero es par")
else:
    print("el numero es impar")