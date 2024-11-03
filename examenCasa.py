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
    return len(listaAUsar)

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

listaCanciones={}
listaCanciones=cargar_lista("playlist.txt")
print("-------------------------------")
agregar_cancion(listaCanciones, "Heavensent", "Apocalypta")
print(listaCanciones)
print("-------------------------------")
eliminar_cancion(listaCanciones, "Heavensent")
print(listaCanciones)
print("-------------------------------")
print(contar_canciones(listaCanciones))
print("-------------------------------")
listQueen = buscar_por_artista(listaCanciones, "Queen")
print(listQueen)
print("-------------------------------")
listaAlfabetica=ordenar_alfabeticamente(listaCanciones)
print(listaAlfabetica)
print("-------------------------------")
listaAleatoria=crear_lista_aleatoria(listaCanciones, 6)
print(listaAleatoria)
print("-------------------------------")
guardar_lista(listaCanciones, "playlist.txt")
print("-------------------------------")
agregar_cancion(listaCanciones, "Heavensent", "Apocalypta")
guardar_lista(listaCanciones, "playlist.txt")
print(listaCanciones)
print("-------------------------------")
eliminar_cancion(listaCanciones, "Heavensent")
guardar_lista(listaCanciones, "playlist.txt")
print(listaCanciones)

