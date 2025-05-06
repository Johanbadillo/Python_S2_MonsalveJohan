# ####################
# ##### EJERCICIO 3###
# ####################

print ("Bienvenidos a nuestro programa de identificar el numero mayor")

num1 = int (input("Porfa ingrese el primer numero que desees compararar "))   
num2 = int (input("porfa ingrese el segundo numero"))
num3 = int (input("ingrese el ultimo numero de la comparacion"))

if num1<num2:
    if num1<num3:
        print("el numero mayor es: "+str(num3))
    else:
        print("el mayor es: " +str( num1))
else:
    if num2<num3:
        print("el numero mayor es: "+str(num3))
    else:
        print("El mayor es: " +str (num2))