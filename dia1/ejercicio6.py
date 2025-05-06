# ####################
# ##### EJERCICIO 6###
# ####################

print ("Bienvenido a nuestro pgrogrma quieres saber si su numero es par o impar")

num1=int(input("porfa ingrese el numero que deseas saber: "))
primo=2
resul=num1 % primo
if resul==0:
    print("El numero es par")
else:
    print("el numero es impar")