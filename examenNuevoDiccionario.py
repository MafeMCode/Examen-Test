#Parte 1

## 1

def cargar_lista(nombreArchivo):
    retList=[]
    with open(nombreArchivo, "r") as fichero:
        for linea in fichero:
            dicTemp = {}
            nombreCancion, nombreArtista, nombreGenero = linea.strip().split(" - ")
            dicTemp["cancion"]=nombreCancion
            dicTemp["artista"]=nombreArtista
            dicTemp["genero"]=nombreGenero
            retList.append(dicTemp)
    return retList

## 2

def agregar_cancion(listaAUsar, nombreCancion, nombreArtista, nombreGenero):
    dicTemp={}
    dicTemp["cancion"]=nombreCancion
    dicTemp["artista"]=nombreArtista
    dicTemp["genero"]=nombreGenero
    listaAUsar.append(dicTemp)
    
## 2.2

def buscar_por_artista(listaAUsar, nombreArtista):
    retList=[]  
    for each in listaAUsar:
        if each["artista"] == nombreArtista:
            retList.append(each)
    return retList

## 3

def eliminar_cancion(listaAUsar, nombreCancion):
    for each in listaAUsar:
        if each["cancion"]==nombreCancion:
            listaAUsar.remove(each)
        
# 4

def guardar_lista(listaAUsar, nombreArchivo):
    with open(nombreArchivo, "w") as fichero:
        for elemento in listaAUsar:
            fichero.write(elemento["cancion"] + " - " + elemento["artista"] + " - " + elemento["genero"] + "\n")

print("---------------------------------")

listaTemporal = cargar_lista("playlist2.txt")

print(listaTemporal)

print("---------------------------------")

for each in listaTemporal:
    print(each["cancion"] + " - " + each["artista"] + " - " + each["genero"] + "\n")
   
print("---------------------------------")
    
agregar_cancion(listaTemporal, "Heavensent", "Apocalypta", "Power Metal")

listaApoca=buscar_por_artista(listaTemporal, "Apocalypta")

print(listaApoca)

print("---------------------------------")

print(listaTemporal)

print("---------------------------------")

print(listaTemporal[len(listaTemporal)-1])

print("---------------------------------")

eliminar_cancion(listaTemporal, "Heavensent")

guardar_lista(listaTemporal, "playlist2.txt")
















# # Funciones Adicionales (Cosa mia)

# def imprimir(listaAUsar, nombreLista):
#     print(str(nombreLista))
#     print("-----------------------")
#     for cancion in listaAUsar:
#         print(cancion + " - " + listaAUsar[cancion])
        
# def imprimirLista(listaAUsar, nombre):
#     print(str(nombre))
#     print("-----------------------")
#     for item in listaAUsar:
#         print(item)

# def menu():
#     print("-------------------------------")
#     print("      Menu de Examen Test      ")
#     print("-------------------------------")
#     funcionando = 1
#     while(funcionando):
#         print("-------------------------------")
#         print("Seleccione una opcion:")
#         print("1. Cargar Lista")
#         print("2. Añadir Cancion")
#         print("3. Borrar Cancion")
#         print("4. Contar Canciones")
#         print("5. Crear lista alfabética")
#         print("6. Crear lista aleatoria")
#         print("7. Guardar Lista")
#         print("0. Cerrar Programa")
#         print("-------------------------------")

#         opcion=int(input())
        
#         match opcion:
#             case 1:
#                 print("Introduzca el archivo a cargar:")
#                 fichero=input()
#                 listaCanciones=cargar_lista(fichero)
#             case 2:
#                 print("Introduzca el nombre de la canción a añadir:")
#                 nombreCancion=input()
#                 print("Introduzca el autor:")
#                 nombreAutor=input()
#                 agregar_cancion(listaCanciones, nombreCancion, nombreAutor)
#             case 3:
#                 print("Introduzca el nombre de la cancion a eliminar:")
#                 nombreCancion=input()
#                 eliminar_cancion(listaCanciones, nombreCancion)
#             case 4:
#                 print("La lista tiene " + str(contar_canciones(listaCanciones)) + " canciones.")   
#             case 5:
#                 listaAlfabetica=ordenar_alfabeticamente(listaCanciones)
#                 imprimirLista(listaAlfabetica, "Lista Alfabética")
#             case 6:
#                 print("Introduzca un número de canciones a añadir entre 1 y " + str(len(listaCanciones)) + ":")
#                 numeroN = int(input())
#                 listaAleatoria=crear_lista_aleatoria(listaCanciones, numeroN)
#                 imprimirLista(listaAleatoria, "Lista Aleatoria")
#             case 7:
#                 guardar_lista(listaCanciones, "playlist.txt")
#             case 0:
#                 funcionando=0
#                 continue

# listaCanciones = {}
# menu()