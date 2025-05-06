# #######################################
# ########### Ejercicio Nomina ##########
# #######################################


print("Bienvenido a la organizacion de nominas")

valorHora = 20000
totalBruto = 0
totalNeto = 0
totalEPS = 0
totalPension = 0  

mayorNeto = 0
menorNeto = 0
nombreMayor = ""
nombreMenor = ""

emple = int(input("Ingrese la cantidad de empleados: "))

for i in range(1, emple+1):
    print("Ingrese el nombre del empleado: ")
    nombre = input()

    print("Ingrese las horas trabajadas del empleado: ")
    horas = int(input())

    sueldoBruto = horas * valorHora
    descuentoEPS = sueldoBruto * 0.04
    descuentoPension = sueldoBruto * 0.04
    sueldoNeto = sueldoBruto - descuentoEPS - descuentoPension

    totalBruto = sueldoBruto+totalBruto
    totalEPS = descuentoEPS+totalEPS
    totalPension = descuentoPension+totalPension
    totalNeto = sueldoNeto+totalNeto

    if sueldoNeto > mayorNeto:
        mayorNeto = sueldoNeto
        nombreMayor = nombre
    
    if sueldoNeto < menorNeto:
        menorNeto = sueldoNeto
        nombreMenor = nombre

    print("-----------------------------")
    print("Empleado:", nombre)
    print("Sueldo Bruto:", sueldoBruto)
    print("Descuento EPS:", descuentoEPS)
    print("Descuento Pensión:", descuentoPension)
    print("Sueldo Neto:", sueldoNeto)
    print("-----------------------------")


promedioBruto = totalBruto / emple
promedioNeto = totalNeto / emple



print("###########################################")
print("Total Sueldos Brutos:", totalBruto)
print("Total Descuento EPS:", totalEPS)
print("Total Descuento Pensión:", totalPension)
print("Total Sueldos Netos:", totalNeto)
print("El empleado que más gana es:", nombreMayor, "con un sueldo neto de:", mayorNeto)
print("El empleado que menos gana es:", nombreMenor, "con un sueldo neto de:", menorNeto)
print("Promedio de Sueldos Brutos:", promedioBruto)
print("Promedio de los Sueldos Netos:", promedioNeto)

# Desarrollado por : Johan Monsalve C.C 1097911956