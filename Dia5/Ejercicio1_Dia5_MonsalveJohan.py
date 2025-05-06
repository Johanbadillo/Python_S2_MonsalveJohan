# #######################################
# ########### Ejercicio Hamburguesas#####
# #######################################


print("Bienvenido a nuestro programa para pedir tus hamburguesas")


cantHam = int(input("Cuantas hamburguesas desea pedir: "))
acumulado=0
for i in range(cantHam):
    tipoPan = int(input("Seleccione el tipo de pan 1.para centeno $1000, 2.para avena $1500: "))
    if tipoPan == 1:
        print("El tipo de pan es centeno")
        acumulado = acumulado + 1000
    elif tipoPan == 2:
        print("El tipo de pan es avena")
        acumulado = acumulado + 1500

    tipoCarne= int(input("que tipo de carne deseas: 1.250gr $5000, 2.300gr $7000: "))
    if tipoCarne ==1:
        print ("seleccionaste carne de 250gr")
        acumulado = acumulado + 5000
    elif tipoCarne ==2:
        print ("Escogiste la carne de 300gr")
        acumulado = acumulado + 7000  

    tipoPollo = int(input(" Que cantidad de pollo deseas. 1.250gr $4500, 2.350gr $5500: "))
    if tipoPollo ==1: 
        print("Seleccionaste pollo de 250gr")
        acumulado = acumulado + 4500
    elif tipoPollo ==2:
        print("Seleccionaste pollo de 350gr")
        acumulado=acumulado+5500

    tipoPolloD = int(input("Selecciona la cantidad de pollo Desmechado, 1.250gr $6500, 2.350gr $7500: "))
    if tipoPolloD==1:
        print("Seleccionaste pollo desmechado de 250gr")
        acumulado = acumulado + 6500
    elif tipoPolloD==2:
        print("Seleccionaste pollo desmechado de 350gr")
        acumulado = acumulado + 7500

    tipoTocineta = int (input("Selecciona la cantidad de tocineta, 1.Una lonja $1500, 2.Dos lonjas $2500: "))
    if tipoTocineta==1:
        print("Seleccionaste una lonja de tocineta")
        acumulado = acumulado + 1500
    elif tipoTocineta==2:
        print("Seleccionaste dos lonjas de tocineta")
        acumulado = acumulado + 2500

    tipoPapa = int(input("Selecciona el tipo de papa: 1.francesa $5000, 2.cascos $6000: "))
    if tipoPapa==1:
        print("Seleccionaste papa francesa")
        acumulado = acumulado + 5000
    elif tipoPapa==2:
        print("Seleccionaste papa en cascos")
        acumulado = acumulado + 6000

    tipoBebida = int (input("Selecciona la bebida 1.Gaseosa $5000, 2.Cerveza club $8000, 3.Naranjada $9000: "))
    if tipoBebida==1:
        print("Seleccionaste gaseosa")
        acumulado = acumulado + 5000
    elif tipoBebida==2:
        print("Seleccionaste cerveza club")
        acumulado = acumulado + 8000
    elif tipoBebida==3:
        print("Seleccionaste naranjada")
        acumulado = acumulado + 9000 
    
    print("El total con Servicio Incluido es: " , int(acumulado+(acumulado*0.1)))

    # Desarrollado por : Johan Monsalve C.C 1097911956