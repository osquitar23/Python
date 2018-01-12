print("Hola")
unidades=15
precio=7.5
total=unidades%precio
print(total)
#Trabajando con caracteres
mensaje="En un lugar de la mancha"
print(mensaje[0])
print(mensaje[5:])
print(len(mensaje))
#Arrays en python
precios=[7,25,30.2]
print(precios)
print(precios[1])
print(precios[-1])
precios.append(10)
print(precios)
precios.append("Madrid")
print(precios)
#ejercicio de Array
alumnos=['Juan','Maria','Luis']
quimica=[8,7,10]
notas=[alumnos,quimica]
print(notas)
print(notas[0])
print(notas[0][0])
print(notas[1][1])


#Si la facturacion es <1500 me sacas un mensaje sin comision,
#en cambio si yo facturo una comision entre 1500 y 4000 me sacas un mensaje un mensaje(La comision es 12,5)
facturacion=5000
if (facturacion<1500):
    print("sin comision")
elif(1500<facturacion<4000):
    print("La comision es del 12.5")
else:
    print("La comision es del 15%")

