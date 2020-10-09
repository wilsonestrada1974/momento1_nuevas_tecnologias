"""Realizar un algoritmo que lea un número por teclado. En caso de que ese número
sea 0 o menor que 0, se saldrá del programa imprimiendo antes un mensaje de error.
Si es mayor que 0, se deberá calcular su cuadrado y la raiz cuadrada del mismo,
visualizando el numero que ha tecleado el usuario y su resultado (“Del numero X, su
potencia es X y su raiz X” ). Para calcular la raiz cuadrada se puede usar la función
interna RAIZ(X) o con una potencia de 0,5."""
import math


print("Ingrese el número a calcular")
a = float(input())

if(a<=0):
    print("Error.   No se pueden hacer los calculos con numeros menores o iguales a 0")
else:
    b=a*a
    c=math.sqrt(a)
    print("El cuadrado de ",a," es: ",b, " y su raiz cuadrada es: ",c)