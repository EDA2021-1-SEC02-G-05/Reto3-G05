"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
import datetime
import config as cf
import model
import csv




"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    dicci = model.newMapOrdenado()
    return dicci

def init2():

    info1 = model.newOrderMap()

    return info1


def loadData(dicci, crimesfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    mapfile1 = cf.data_dir + "context_content_features-small.csv"
    input_file = csv.DictReader(open(mapfile1, encoding="utf-8"),
                                delimiter=",")

    mapfile2 = cf.data_dir + "user_track_hashtag_timestamp-small.csv"
    input_file2= csv.DictReader(open(mapfile2, encoding="utf-8"),
                                delimiter=",")
    mapfile3 = cf.data_dir + "sentiment_values.csv"
    input_file3= csv.DictReader(open(mapfile3, encoding="utf-8"),
                                delimiter=",")
    
    
    for song in input_file:

        model.addsong(dicci,song)

  
    return dicci


def loadData2(dicci, crimesfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    mapfile1 = cf.data_dir + "context_content_features-small.csv"
    input_file = csv.DictReader(open(mapfile1, encoding="utf-8"),
                                delimiter=",")

    
    for song in input_file:

        model.addCancion(dicci,song)

  
    return dicci


def loadparte2(info):

    return model.parte2(info)

def loadtablageneros(nom,nombre,des1,des2):

    d = model.tablageneros(nom,nombre,des1,des2)

    return d

def loadrequerimiento1(dicci,nombre,num1,num2):

    popo = model.requerimiento1(dicci,nombre,num1,num2)

    return popo


def loadHeight(dicci):

    pepe=model.crimesHeight(dicci)

    return pepe

def loadSize(dicci):

    pepo=model.crimesSize(dicci)

    return pepo

# Funciones para la carga de datos

def loadrequerimiento2():
    pass
def loadrequerimiento3():
    pass
def loadrequerimiento4(info,nom1,nom2,nom3,nom4,des1,des2):
    tempo = model.requerimiento4(info,nom1,nom2,nom3,nom4,des1,des2)
    
    return tempo
def loadrequerimiento5():
    pass

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
