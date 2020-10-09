"""Un colegio desea saber qué porcentaje de niños y qué porcentaje de niñas hay en el
curso actual. Diseñar un algoritmo para este propósito (recuerda que para calcular el
porcentaje puedes hacer una regla de 3)."""

print("Ingrese la cantidad de niños de la clase")
niños=int(input())
print("ingrese la cantidad de niñas de la clase")
niñas=int(input())

total=niños+niñas
porceniños=(niños/total)*100
porceniñas=(niñas/total)*100

print("el porcentaje de niños en la clase es: ",porceniños,"%")
print("el porcentaje de niñas en la clase es: ",porceniñas,"%")