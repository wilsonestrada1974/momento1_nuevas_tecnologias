""" Algoritmo que nos diga si una persona puede acceder a cursar un ciclo formativo
de grado superior o no. Para acceder a un grado superior, si se tiene un titulo de
bachiller, en caso de no tenerlo, se puede acceder si hemos superado una prueba de
acceso"""

print("Tiene titulo de bachillerato? s/n")
bachiller=input()
if(bachiller=="s"):
    print("puede acceder al ciclo formativo")
else:
    print("Ha superado la prueba de acceso?  s/n")
    resp=input()
    if(resp == "s"):
        print("puede acceder al ciclo formativo")
    else:
        print("Lo sentimos.     No puede acceder al ciclo formativo")