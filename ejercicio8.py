"""Una tienda ofrece un descuento del 15% sobre el total de la compra durante el mes
de octubre. Dado un mes y un importe, calcular cuál es la cantidad que se debe cobrar
al cliente."""

print("favor ingrese al mes a calcular")
mes=input()

print("ingrese el valor total de las compras del mes")
compras=int(input())


if(mes == "octubre"):
    descuento=compras * 0.15
    total=compras-descuento

    print("El total del descuento es de: $",descuento)
    print("el valor total a pagar es: $",total)

else:
    print("para este mes no se genera ningun descuento")