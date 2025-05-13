# ##########################
# #### Clase Dia 6 ######
# ##########################
# Diccionarios
#Un DICccionario  es una colección de elementos , donde cada elementos insertado tiene una llave úntica, 
# la cual va acompañada de un valor 
'''
Pepito es Cool
{
    "nombre":"Pedro",
    "apellido":"Gómez"
}
'''
miPrimerDiccionario={
    "nombre":"Pedro",
    "apellido":"Gómez",
    "edad":25
}
print(miPrimerDiccionario)
print(type(miPrimerDiccionario))

##Para recorrer un DICcionario debes llamar a la llave
print(miPrimerDiccionario["nombre"])
print(type(miPrimerDiccionario["nombre"]))
# Se puede recorrer con puntos en algunos casos
'''
print(miPrimerDiccionario.nombre)
'''
##Para reemplazar un valor del diccionario
miPrimerDiccionario["nombre"]="Pedro"
nombre = miPrimerDiccionario["nombre"]
apellido= miPrimerDiccionario["apellido"]
print(miPrimerDiccionario["nombre"]+" "+miPrimerDiccionario["apellido"])

miPrimerDiccionario["ciudadNacimiento"]="Monteria"

print(miPrimerDiccionario)
miPrimerDiccionario["ciudadNacimiento"]="Bucaramanga"

print(miPrimerDiccionario)
#Un objeto tiene varios atributos, 
# que pertenecen al mismo objeto. 
listaPersonas=[]
listaPersonas.append(miPrimerDiccionario)
print("")
print("")
print(listaPersonas)
listaPersonas.append({
    "nombre":"Corpus",
    "apellido":"Bejarano",
    "edad":27
})
print("")
print("")
print(listaPersonas)
print("")
print("")
print(listaPersonas[1])
print(type(listaPersonas[1]))
print(listaPersonas[0]["edad"])

#Recorrer listas con diccionarios
for i in range(len(listaPersonas)):
    print("------------------------------")
    print("#  Persona n.",i+1,)
    print("-------------------------------")
    print("Nombre: ",listaPersonas[i]["nombre"])
    print("Apllido:",listaPersonas[i]["apellido"])
    print("Edad:   ",listaPersonas[i]["edad"])
    print("")

##Diccionario con listas
diccionarioRobusto={
    "id":1,
    "nombre":"Pedro",
    "apellido":"Gómez",
    "edad":25,
    "telefonos":[{"codigo":57,"numero":3023019865,"tipo":"trabajo"}
                 ,{"codigo":1,"numero":3983054625,"tipo":"personal"}]
}
diccionarioRobusto2={
    "id":2,
    "nombre":"Corpus",
    "apellido":"Bejarano",
    "edad":27,
    "telefonos":[{"codigo":58,"numero":2323057565,"tipo":"trabajo"}
                 ,{"codigo":22,"numero":6857493658,"tipo":"personal"}]
}
listaRobusta=[]
listaRobusta.append(diccionarioRobusto)
listaRobusta.append(diccionarioRobusto2)
print("")
print("")
print(listaRobusta)
print("")
print("")
#print(listaRobusta[0]["telefonos"][1]['numero'])

for i in range(len(listaRobusta[0]["telefonos"])):
    if(listaRobusta[0]["telefonos"][i]['tipo']=="trabajo"):
        print(listaRobusta[0]["telefonos"][i]['numero'])
print("")
print("")
numeroPrimeraPersona=listaRobusta[0]["telefonos"][1]['numero']
tipoNumeroPP=listaRobusta[0]["telefonos"][1]['tipo']
print(str(numeroPrimeraPersona)+ tipoNumeroPP)
print(" ")
booleanito = True
while(booleanito):
    print("*********************************")
    print("***** Librería de personas ******")
    print("*********************************")
    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opción (Numérica):"))
    if(opcionUsuario==1):
        print("_____________________________")
        print("-----  Crear Persona  -------")
        print("_____________________________")
        diccionarioVacio={}
        diccionarioVacio["id"] = (listaRobusta[len(listaRobusta)-1]["id"])+1,
        diccionarioVacio["nombre"] = input("Nombre: ")
        diccionarioVacio["apellido"] = input("Apellido: ")
        diccionarioVacio["edad"] = int(input("Edad: "))
        diccionarioVacio["telefonos"] = []
        cantidadTelefonos = int(input("¿Cuántos teléfonos desea agregar?: "))
        for i in range(cantidadTelefonos):
            telefono = {}
            telefono["codigo"] = int(input("Código del teléfono: "))
            telefono["numero"] = int(input("Número del teléfono: "))
            telefono["tipo"] = input("Tipo de teléfono (personal/trabajo): ")
            diccionarioVacio["telefonos"].append(telefono)
        listaRobusta.append(diccionarioVacio)
        print("Persona creada exitosamente.")
    elif(opcionUsuario==2):
        for i in range(len(listaRobusta)):
            print("___________________________")
            print("-----  Persona N.",i+1," ------")
            print("___________________________")
            print("ID:       ", listaRobusta[i]["id"])
            print("Nombre:   ",listaRobusta[i]["nombre"])
            print("Apellido: ",listaRobusta[i]["apellido"])
            print("Edad:     ",listaRobusta[i]["edad"])
            
            for q in range(len(listaRobusta[i]["telefonos"])):
                print("---------------------------")
                print("Telefono N.",q+1,":",listaRobusta[i]["telefonos"][q]["tipo"])
                print("    - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                print("    - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                print("---------------------------")
    elif(opcionUsuario==3):
        print("_________________________________________________")
        print("--------  Busuqeda de Persona Inidivual  --------")
        print("_________________________________________________")
        personaIndividual=int(input("Porfa ingresar el ID de la persona"))
        print("ID:       ", listaRobusta[-1]["id"])
        print("Nombre:   ",listaRobusta[-1]["nombre"])
        print("Apellido: ",listaRobusta[-1]["apellido"])
        print("Edad:     ",listaRobusta[-1]["edad"])
        for q in range(len(listaRobusta[i]["telefonos"])):
                print("---------------------------")
                print("Telefono N",q+1,":",listaRobusta[i]["telefonos"][q]["tipo"])
                print("    - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                print("    - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                print("---------------------------")
        print("---------------------------")
    elif(opcionUsuario==4):
        print("____________________________________________________")
        personaActualizar=int(str(input("Porfa ingresar el ID de la persona")))
        datoNuevo=str((input("Ingrese el nombre de nuevo")))
        listaRobusta[personaActualizar-1]["nombre"]=datoNuevo
        datoNuevo=str((input("Ingrese el apellido: ")))
        listaRobusta[personaActualizar-1]["apellido"]=datoNuevo
        datoNuevo=int(input("Ingrese la edad: "))
        listaRobusta[personaActualizar-1]["edad"]=datoNuevo
        datoNuevo=str(input("Ingrese el codgio del numero: "))
        listaRobusta[personaActualizar-1]["telefonos"][0]["codigo"]=datoNuevo
        datoNuevo=int(input("Ingrese el numero de trabajo: "))
        listaRobusta[personaActualizar-1]["telefonos"][0]["numero"]=datoNuevo
        datoNuevo=str(input("Ingrese el codgio del numero: "))
        listaRobusta[personaActualizar-1]["telefonos"][1]["codigo"]=datoNuevo
        datoNuevo=int(input("Ingrese el numero de personal: "))
        listaRobusta[personaActualizar-1]["telefonos"][1]["numero"]=datoNuevo
        print("____________________________________________________")
    elif(opcionUsuario==5):
        eliminaUsuario=int(input("Ingrese el Id del usuario que deseas eliminar"))
        del listaRobusta[eliminaUsuario-1]
    elif(opcionUsuario==6):
        print("Chaousssss")
        booleanito=False
    else:
        print("No es una opción válida")

    
    
    
#Desarrollado por Pedro Felipe Gómez : C.C-1.555.444.333