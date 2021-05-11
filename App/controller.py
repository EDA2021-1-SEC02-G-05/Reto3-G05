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
import time
import datetime
import tracemalloc





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

def init3():

    info2 = model.newOrderMapSentimiento()

    return info2

def init4():

    info3 = model.orderMapSentimiento()

    return info3


def loadData(dicci, crimesfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    mapfile1 = cf.data_dir + "context_content_features-small.csv"
    input_file = csv.DictReader(open(mapfile1, encoding="utf-8"),
                                delimiter=",")
    
    for song in input_file:

        model.addsong(dicci,song)
        model.requerimientoo(dicci,song)


  
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

def loadData3(diccio, crimesfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """

    mapfile2 = cf.data_dir + "context_content_features-small.csv"
    input_file2= csv.DictReader(open(mapfile2, encoding="utf-8"),
                                delimiter=",")


    
    for song2 in input_file2:

        model.addFecha(diccio,song2)

  
    return diccio

def loadData4(diccio, crimesfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    mapfile3 = cf.data_dir + "user_track_hashtag_timestamp-small.csv"
    input_file3= csv.DictReader(open(mapfile3, encoding="utf-8"),
                                delimiter=",")

    
    for song2 in input_file3:

        model.addFecha(diccio,song2)
        model.requi(dicci,jit)

      

  
    return diccio

def loadData5(diccion, crimesfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    mapfile4 = cf.data_dir + "sentiment_values.csv"
    input_file4= csv.DictReader(open(mapfile4, encoding="utf-8"),
                                delimiter=",")

    
    for song3 in input_file4:

        model.addSentimiento(diccion,song3)

  
    return diccion

def loadparte2(info):

    return model.parte2(info)

def loadrequerimiento1(dicci,nombre,num1,num2):

    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    popo = model.requerimiento1(dicci,nombre,num1,num2)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return popo[0],popo[1],delta_time,delta_memory

def loadrequerimiento2(dicci,d1,d2,e1,e2):

    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    lupita=model.requerimiento2(dicci,d1,d2,e1,e2)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return lupita[0],lupita[1],delta_time,delta_memory

def loadrequerimiento3(dicci,i1,i2,t1,t2):

    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()


    pepeelgruillo=model.requerimiento3(dicci,i1,i2,t1,t2)


    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return  pepeelgruillo[0],pepeelgruillo[1],delta_time,delta_memory

def loadrequerimiento4(info,nom1,nom2,nom3,nom4,des1,des2):

    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()


    tempo = model.requerimiento4(info,nom1,nom2,nom3,nom4,des1,des2)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    
    return tempo[0],tempo[1],tempo[2],tempo[3],tempo[4],tempo[5],tempo[6],tempo[7],tempo[8],tempo[9],tempo[10],tempo[11],delta_time,delta_memory



def loadrequerimiento5(info,diccio,diccion,rangoinf,rangomay):
     
    rangoinf = datetime.datetime.strptime(rangoinf,"%H:%M:%S")
    rangomay = datetime.datetime.strptime(rangomay,"%H:%M:%S")

    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    ivandu = model.requerimiento5(info,diccio,diccion,rangoinf,rangomay)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return ivandu[0],ivandu[1],ivandu[2],ivandu[3],ivandu[4],ivandu[5],ivandu[6],ivandu[7],ivandu[8],ivandu[9]
    

def loadHeight(dicci):

    pepe=model.crimesHeight(dicci)

    return pepe

def loadSize(dicci):

    pepo=model.crimesSize(dicci)

    return pepo

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory


