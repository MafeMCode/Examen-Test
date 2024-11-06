import json

#Parte 1

## 1
def cargar_lista(nombreArchivo):
    retList=[]
    try:
        with open(nombreArchivo, "r") as fichero:
            for linea in fichero:
                dicTemp = {}
                Valores = linea.strip().split(" - ")
                if len(Valores)==3:
                    dicTemp["cancion"]=Valores.pop(0)
                    dicTemp["artista"]=Valores.pop(0)
                    dicTemp["genero"]=Valores.pop(0)
                    retList.append(dicTemp)
                else:
                    raise Exception("El número de datos es incorrecto")
    except(FileNotFoundError):
        print("La ruta del fichero no ha encontrado nada")
    except(Exception):
        print(Exception.__annotations__)        
    return retList

def cargar_json(nombreArchivo):
    with open(nombreArchivo, "r") as fichero:
        return json.load(fichero)
        
## 2

def agregar_cancion(listaCanciones, nombreCancion, nombreArtista, nombreGenero):
    if buscar_cancion(listaCanciones, nombreCancion) == 0:
        dicTemp={}
        dicTemp["cancion"]=nombreCancion
        dicTemp["artista"]=nombreArtista
        dicTemp["genero"]=nombreGenero
        listaCanciones.append(dicTemp)
    else:
        print(f"La canción {nombreCancion} ya existe en la lista.")
    
## 2.2

def buscar_por_artista(listaCanciones, nombreArtista):
    retList=[]  
    for each in listaCanciones:
        if each["artista"] == nombreArtista:
            retList.append(each)
    return retList

def buscar_cancion(listaCanciones, nombreCancion):
    MrBoolean=False
    for each in listaCanciones:
        if each["cancion"] == nombreCancion:
            MrBoolean=True
            break
    return MrBoolean

## 3

def eliminar_cancion(listaCanciones, nombreCancion):
    for each in listaCanciones:
        if each["cancion"]==nombreCancion:
            listaCanciones.remove(each)
        
# 4

def guardar_lista(listaCanciones, nombreArchivo):
    with open(nombreArchivo, "w") as fichero:
        for elemento in listaCanciones:
            fichero.write(elemento["cancion"] + " - " + elemento["artista"] + " - " + elemento["genero"] + "\n")

def guardar_json(listaCanciones, nombreArchivo):
    with open("playlistJson.json") as Jason:
        json.dump(listaCanciones, Jason)
        
print("---------------------------------")

# listaTemporal = cargar_lista("playlist2.txt")

listaTemporal = cargar_json("playlistJson.json")

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

# def imprimir(listaCanciones, nombreLista):
#     print(str(nombreLista))
#     print("-----------------------")
#     for cancion in listaCanciones:
#         print(cancion + " - " + listaCanciones[cancion])
        
# def imprimirLista(listaCanciones, nombre):
#     print(str(nombre))
#     print("-----------------------")
#     for item in listaCanciones:
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