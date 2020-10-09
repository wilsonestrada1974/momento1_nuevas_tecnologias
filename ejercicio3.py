# Algoritmo que lea dos números y nos diga cual de ellos es mayor o bien si son
# iguales (recuerda usar la estructura condicional SI)

print("Ingrese el primer numero")
a = int(input())
print("Ingrese el segundo numero")
b = int(input())

if(a > b):
    print("El primer numero es mayor que el segundo")
elif(a < b):
    print("El segundo numero es mayor que el primero")
else:
    print("Los dos numeros son iguales")
