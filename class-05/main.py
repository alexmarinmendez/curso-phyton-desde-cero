import computadora

c1 = computadora.Computadora("Acer", 8, 125, 2600, 100)
c2 = computadora.Computadora("Asus", 16, 256, 5200, 20, 10)

print(c1)
print(c2)

c1.set_stock(5) #ingresan 5 computadoras al stock
print(f"El stock es {c1.stock}") #verificamos que el stock ahora es 105
c1.set_stock(-10) #se vendieron 10 computadoras
print(f"El stock es {c1.stock}") #verificamos que el stock ahora es 95

print(f"El descuento es: {c1.dscto}")   #verificamos que el descuento es de 0%
print(f"El descuento es: {c2.dscto}")   #verificamos que el descuento es de 10%

#Averiguamos el precio con descuento :(
print(c2.calcular_precio())
