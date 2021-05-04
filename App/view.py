"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

import sys 

default_limit = 1000 
sys.setrecursionlimit(default_limit*10) 


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""



def printMenu():
    print("Bienvenido")
    print("Inicializar el diccionario")
    print("2- Cargar información en el catálogo")
    print("3- Analisis de datos(Cantidad de registros de eventos, autores,pistas")
    print("4- Requerimiento 1")
    print("5- Requerimiento 2")
    print("6- Requerimiento 3")
    print("7- Requerimiento 4")
    print("8- Requerimiento 5")


crimesfile="context_content_features-small.csv"
user_track="user_track_hashtag_timestamp-small.csv"


# arreglar esto 
dicci = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        dicci=controller.init()
        info = controller.init2()
        diccio = controller.init3()
        print(dicci)
        print(info)
        print(diccio)

    elif int(inputs[0]) == 2:
        controller.loadData(dicci,crimesfile) #arboles por caracteristicas de evento
        t = controller.loadData2(info,crimesfile) # arbol organizado por tempo
        f = controller.loadData3(diccio,user_track) #arbol organizado por fecha
        print('Crimenes cargados: ' + str(controller.loadHeight(dicci)))
        print('Crimenes cargados: ' + str(controller.loadSize(dicci)))
    
    
    elif int(inputs[0]) == 3:

        o = controller.loadparte2(info)

        print("El total de registros de eventos de escucha cargados son: ",o[0])
        print("La altura del arbol es: ",o[1])
        print("El total de artistas es: ",o[2])
        print("El total de pistas de audio son: ",o[3])

    elif int(inputs[0]) == 4:

        nombre = str(input("Ingrese el nombre de la caracteristica de contenido: "))
        num1 = float(input("Ingrese el limite inferior: "))
        num2 = float(input("Ingrese el limite superior: "))

        i = controller.loadrequerimiento1(dicci,nombre,num1,num2)

        print("El numero de reproducciones de piezas musicales que tiene ",str(nombre),"son ",i[0])
        print("El numero de artistas unicos(sin repeticiones): ", i[1])

        print("Tiempo [ms]: ", f"{i[2]:.3f}", " || ",
        "Memoria [kB]: ", f"{i[3]:.3f}")

    elif int(inputs[0]) == 5:

        d1=float(input("INGRESE D1: "))
        d2=float(input("INGRESE D2: "))
        e1=float(input("INGRESE E1: "))
        e2=float(input ("INGRESE E2: "))
        otu= controller.loadrequerimiento2(dicci,d1,d2,e1,e2)
        
        print("Tiempo [ms]: ", f"{otu[1]:.3f}", " || ",
        "Memoria [kB]: ", f"{otu[2]:.3f}")

        print(" El numero total de pistas es: ", otu[0])

    elif int(inputs[0]) == 6:

        i1=float(input("INGRESE I1: "))
        i2=float(input("INGRESE I2: "))
        t1=float(input("INGRESE T1: "))
        t2=float(input ("INGRESE T2: "))

        panaca=controller.loadrequerimiento3(dicci,i1,i2,t1,t2) 

        print("Tiempo [ms]: ", f"{panaca[1]:.3f}", " || ",
        "Memoria [kB]: ", f"{panaca[2]:.3f}")

        print(panaca[0])

        
    elif int(inputs[0]) == 7:

        nom1 = str(input("Ingrese el genero que desea: "))
        nom2 = str(input("Ingrese el genero que desea: "))
        nom3 = str(input("Ingrese el genero que desea: "))

        nom4 = ""
        des1 = ""
        des2 = ""

        deseo = str(input("¿Desea agregar un nuevo genero? " ))
        if deseo == "si":
            nom4 = str(input("Ingrese el nombre de el nuevo genero: "))
            des1 = int(input("Ingrese el limite inferior: "))
            des2 = int(input("Ingrese el limite superior: "))

        else:
            print("vale perfecto no hay nuevo genero para agregar")
           
        tempo = controller.loadrequerimiento4(info,nom1,nom2,nom3,nom4,des1,des2)

        print("El numero total de reproducciones es ",tempo[3])

        print("-"*50)
        print("-"*50)

        print("El numero de reproducciones de ",nom1," es ",tempo[0]," con ", tempo[5]," artistas diferentes")

        print("Los 10 primeros artistas de ",nom1,"son: ")

        print("Artista 1",lt.getElement(tempo[9],0))
        print("Artista 2",lt.getElement(tempo[9],1))
        print("Artista 3",lt.getElement(tempo[9],2))
        print("Artista 4",lt.getElement(tempo[9],3))
        print("Artista 5",lt.getElement(tempo[9],4))
        print("Artista 6",lt.getElement(tempo[9],5))
        print("Artista 7",lt.getElement(tempo[9],6))
        print("Artista 8",lt.getElement(tempo[9],7))
        print("Artista 9",lt.getElement(tempo[9],8))
        print("Artista 10",lt.getElement(tempo[9],9))


        print("-"*100)

        print("El numero de reproducciones de ",nom2," es ",tempo[1]," con ", tempo[6]," artistas diferentes")

        print("Los 10 primeros artistas de ",nom2,"son: ")

        print("Artista 1",lt.getElement(tempo[10],0))
        print("Artista 2",lt.getElement(tempo[10],1))
        print("Artista 3",lt.getElement(tempo[10],2))
        print("Artista 4",lt.getElement(tempo[10],3))
        print("Artista 5",lt.getElement(tempo[10],4))
        print("Artista 6",lt.getElement(tempo[10],5))
        print("Artista 7",lt.getElement(tempo[10],6))
        print("Artista 8",lt.getElement(tempo[10],7))
        print("Artista 9",lt.getElement(tempo[10],8))
        print("Artista 10",lt.getElement(tempo[10],9))

        print("-"*100)

        print("El numero de reproducciones de ",nom3," es ",tempo[2]," con ", tempo[7]," artistas diferentes")

        print("Los 10 primeros artistas de ",nom3,"son: ")

        print("Artista 1",lt.getElement(tempo[11],0))
        print("Artista 2",lt.getElement(tempo[11],1))
        print("Artista 3",lt.getElement(tempo[11],2))
        print("Artista 4",lt.getElement(tempo[11],3))
        print("Artista 5",lt.getElement(tempo[11],4))
        print("Artista 6",lt.getElement(tempo[11],5))
        print("Artista 7",lt.getElement(tempo[11],6))
        print("Artista 8",lt.getElement(tempo[11],7))
        print("Artista 9",lt.getElement(tempo[11],8))
        print("Artista 10",lt.getElement(tempo[11],9))

        
    else:
        sys.exit(0)
sys.exit(0)
