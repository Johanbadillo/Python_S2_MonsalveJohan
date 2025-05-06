# ####################
# ##### EJERCICIO 4###
# ####################

print ("Bienvenido a nuestro programa para calcular el factorial de un numero")
factorial = int (input("Numero a factorizar: "))
for i in range (1,factorial):
    factorial = factorial * i
print("")   
print ("El factorial es: " +str(factorial))