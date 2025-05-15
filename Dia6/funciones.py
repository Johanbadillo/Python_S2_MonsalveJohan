def todosTelefonos(lista,posicion):
    posicion -=1
    for q in range(len(lista[posicion]["telefonos"])):
                print("---------------------------")
                print("Telefono N",q+1,":",lista[posicion]["telefonos"][q]["tipo"])
                print("    - Código:",lista[posicion]["telefonos"][q]["codigo"])
                print("    - Numero:",lista[posicion]["telefonos"][q]["numero"])
                print("---------------------------")
    return lista[posicion["telefonos"]]