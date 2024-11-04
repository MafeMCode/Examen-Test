import random

#Parte 1

## 1.1

def cargar_lista(nombreArchivo):
    retList={}
    with open(nombreArchivo, "r") as fichero:
        for linea in fichero:
            cancion, artista = linea.strip().split(" - ")
            retList[cancion]=artista
    return retList

## 1.2

def agregar_cancion(listaAUsar, nombreCancion, nombreArtista):
    listaAUsar[nombreCancion]=nombreArtista

## 1.3

def eliminar_cancion(listaAUsar, nombreCancion):
    if nombreCancion in listaAUsar:
        del listaAUsar[nombreCancion]
        
# Parte 2

## 2.1

def contar_canciones(listaAUsar):
    return int(len(listaAUsar))

## 2.2

def buscar_por_artista(listaAUsar, nombreArtista):
    retList=[]  
    for instance in listaAUsar:
        if listaAUsar[instance] == nombreArtista:
            retList.append(instance)
    return retList

## 2.3

def ordenar_alfabeticamente(listaAUsar):
    retList=[]
    for cancion in listaAUsar:
        cancionTupla=[cancion, listaAUsar[cancion]]
        retList.append(cancionTupla)
    return sorted(retList)

# Parte 3

## 3.1

def crear_lista_aleatoria(listaAUsar, numeroN):
    retlist=[]
    try:
        retlist = random.sample(list(listaAUsar.items()), numeroN)  
    except ValueError:
        print("El numero seleccionado no puede ser negativo ni mayor del numero de canciones en la lista original.")
        print("El numero de canciones en la lista es: " + str(contar_canciones(listaAUsar)))
    return retlist

## 3.2

def guardar_lista(listaAUsar, nombreArchivo):
    with open(nombreArchivo, "w") as fichero:
        for cancion in listaAUsar:
            fichero.write(cancion + " - " + listaAUsar[cancion] + "\n")
        fichero.close

# Funciones Adicionales (Cosa mia)

def imprimir(listaAUsar, nombreLista):
    print(str(nombreLista))
    print("-----------------------")
    for cancion in listaAUsar:
        print(cancion + " - " + listaAUsar[cancion])
        
def imprimirLista(listaAUsar, nombre):
    print(str(nombre))
    print("-----------------------")
    for item in listaAUsar:
        print(item)

def menu():
    print("-------------------------------")
    print("      Menu de Examen Test      ")
    print("-------------------------------")
    funcionando = 1
    while(funcionando):
        print("-------------------------------")
        print("Seleccione una opcion:")
        print("1. Cargar Lista")
        print("2. Añadir Cancion")
        print("3. Borrar Cancion")
        print("4. Contar Canciones")
        print("5. Crear lista alfabética")
        print("6. Crear lista aleatoria")
        print("7. Guardar Lista")
        print("0. Cerrar Programa")
        print("-------------------------------")

        opcion=int(input())
        
        match opcion:
            case 1:
                print("Introduzca el archivo a cargar:")
                fichero=input()
                listaCanciones=cargar_lista(fichero)
            case 2:
                print("Introduzca el nombre de la canción a añadir:")
                nombreCancion=input()
                print("Introduzca el autor:")
                nombreAutor=input()
                agregar_cancion(listaCanciones, nombreCancion, nombreAutor)
            case 3:
                print("Introduzca el nombre de la cancion a eliminar:")
                nombreCancion=input()
                eliminar_cancion(listaCanciones, nombreCancion)
            case 4:
                print("La lista tiene " + str(contar_canciones(listaCanciones)) + " canciones.")   
            case 5:
                listaAlfabetica=ordenar_alfabeticamente(listaCanciones)
                imprimirLista(listaAlfabetica, "Lista Alfabética")
            case 6:
                print("Introduzca un número de canciones a añadir entre 1 y " + str(len(listaCanciones)) + ":")
                numeroN = int(input())
                listaAleatoria=crear_lista_aleatoria(listaCanciones, numeroN)
                imprimirLista(listaAleatoria, "Lista Aleatoria")
            case 7:
                guardar_lista(listaCanciones, "playlist.txt")
            case 0:
                funcionando=0
                continue

listaCanciones = {}
menu()