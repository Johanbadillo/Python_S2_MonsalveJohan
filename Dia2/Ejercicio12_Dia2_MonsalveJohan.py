# #####################
# ##### EJERCICIO 12###
# #####################

print("Bienvenido a nuestro programa para crear la serie de finobacci")
a=0
b=1
sumaT=1
num1=int(input("Porfa ingrese hasta que numero de la serie deseas conocer"))

for i in range(num1-2):
    final=a+b
    a=b
    b=final
    sumaT=final+sumaT
print("el valor que se encuentra en esa posición de la serie es"+str(final))
print("Y la sumatoria de la serie seria"+str(sumaT))

