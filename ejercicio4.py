# Algoritmo que lea tres números distintos y nos diga cual de ellos es el mayor
#(recuerda usar la estructura condicional Si y los operadores lógicos).

print("Ingrese el primer numero")
a = int(input())
print("Ingrese el segundo numero")
b = int(input())
print("Ingrese el tercer numero")
c= int(input())

if(a>b and a>c):
    print("El numero mayor es: ",a)
elif(b>a and b>c):
    print("El numero mayor es: ",b)
elif(c>a and c>b):
    print("El numero mayor es: ",c)
else:
    print("Algunos de los numeros son iguales")

    
