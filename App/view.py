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
    print("3- Requerimiento 1")
    print("4- Requerimiento 2")
    print("5- Requerimiento 3")
    print("6- Requerimiento 4")
    print("7- Requerimiento 5")




crimesfile="context_content_features-small.csv"


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
        print(dicci)

    elif int(inputs[0]) == 2:
        controller.loadData(dicci,crimesfile)
        print('Crimenes cargados: ' + str(controller.loadHeight(dicci)))
        print('Crimenes cargados: ' + str(controller.loadSize(dicci)))

    elif int(inputs[0]) == 3:

        nombre = str(input("Ingrese el nombre de la caracteristica de contenido: "))
        num1 = float(input("Ingrese el limite inferior: "))
        num2 = float(input("Ingrese el limite superior: "))

        i = controller.loadrequerimiento1(dicci,nombre,num1,num2)

        print("El numero de reproducciones de piezas musicales que tiene ",str(nombre),"son ",i[0])
        print("El numero de artistas unicos(sin repeticiones): ", i[1])

    
        
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        pass
    else:
        sys.exit(0)
sys.exit(0)
