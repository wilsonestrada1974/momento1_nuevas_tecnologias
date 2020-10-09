#Diseñar un algoritmo que pida por teclado tres números; si el primero es negativo,
#debe imprimir el producto de los tres y si no lo es, imprimirá la suma.

print("Ingrese el primer numero")
a = int(input())
print("Ingrese el segundo numero")
b = int(input())
print("Ingrese el tercer numero")
c= int(input())

if(a<0):
    d=a*b*c
    print("el producto de los numeros es: ",d)
else:
    d=a+b+c
    print("la suma de los numeros es: ",d)
