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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
from DISClib.DataStructures import listiterator as it
import datetime
assert config
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newMapOrdenado():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    dicci = {}

    dicci['instrumentalness'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['acousticness'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['liveness'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['speechiness'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['energy'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['danceability'] = om.newMap(omaptype='BRT',comparefunction=compareDates)


    dicci['valence'] = om.newMap(omaptype='BRT',comparefunction=compareDates)



    return dicci




def addsong(dicci, song):


    if om.contains(dicci["instrumentalness"],float(song["instrumentalness"])):
            jef=om.get(dicci["instrumentalness"],float(song["instrumentalness"]))
            lis = me.getValue(jef)
            lt.addLast(lis,song)

    else:

            lisa=lt.newList()
            om.put(dicci["instrumentalness"],float(song["instrumentalness"]),lisa)
            lt.addLast(lisa,song)


    if om.contains(dicci["acousticness"],float(song["acousticness"])):
            jef=om.get(dicci["acousticness"],float(song["acousticness"]))
            lis = me.getValue(jef)
            lt.addLast(lis,song)

    else:

            lisa=lt.newList()
            lt.addLast(lisa,song)
            om.put(dicci["acousticness"],float(song["acousticness"]),lisa)


    if om.contains(dicci["liveness"],float(song["liveness"])):
            jef=om.get(dicci["liveness"],float(song["liveness"]))
            lis = me.getValue(jef)
            lt.addLast(lis,song)

    else:

            lisa=lt.newList()
            lt.addLast(lisa,song)
            om.put(dicci["liveness"],float(song["liveness"]),lisa)


    if om.contains(dicci["speechiness"],float(song["speechiness"])):
            jef=om.get(dicci["speechiness"],float(song["speechiness"]))
            lis = me.getValue(jef)
            lt.addLast(lis,song)

    else:

            lisa=lt.newList()
            lt.addLast(lisa,song)
            om.put(dicci["speechiness"],float(song["speechiness"]),lisa)



    if om.contains(dicci["energy"],float(song["energy"])):
            jef=om.get(dicci["energy"],float(song["energy"]))
            lis = me.getValue(jef)
            lt.addLast(lis,song)

    else:

            lisa=lt.newList()
            lt.addLast(lisa,song)
            om.put(dicci["energy"],float(song["energy"]),lisa)


    if om.contains(dicci["danceability"],float(song["danceability"])):
            jef=om.get(dicci["danceability"],float(song["danceability"]))
            lis = me.getValue(jef)
            lt.addLast(lis,song)

    else:

            lisa=lt.newList()
            lt.addLast(lisa,song)
            om.put(dicci["danceability"],float(song["danceability"]),lisa)

    if om.contains(dicci["valence"],float(song["valence"])):
            jef=om.get(dicci["valence"],float(song["valence"]))
            lis = me.getValue(jef)
            lt.addLast(lis,song)

    else:
            lisa=lt.newList()
            lt.addLast(lisa,song)
            om.put(dicci["valence"],float(song["valence"]),lisa)

    return dicci


def crimesHeight(dicci):
    """
    Número de crimenes
    """
    return om.height(dicci['instrumentalness']),om.height(dicci['acousticness']),om.height(dicci['liveness']),om.height(dicci['speechiness']),om.height(dicci['energy']),om.height(dicci['danceability']),om.height(dicci['valence'])

def crimesSize(dicci):
    """
    Número de crimenes
    """
    return om.size(dicci['instrumentalness']),om.size(dicci['acousticness']),om.size(dicci['liveness']),om.size(dicci['speechiness']),om.size(dicci['energy']),om.size(dicci['danceability']),om.size(dicci['valence'])






    










    
# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

def requerimiento1(dicci,nombre,num1,num2):

    d = om.values(dicci[nombre],num1,num2)
    iterador = it.newIterator(d)
    diccionario = mp.newMap()
    x = 0
    while it.hasNext(iterador):

        actual = it.next(iterador)

        x += lt.size(actual)

        
        ite = it.newIterator(actual)

        while it.hasNext(ite):

            actual = it.next(ite)

            if mp.contains(diccionario,actual["artist_id"]):

                ola = mp.get(diccionario,actual["artist_id"])
                listo = me.getValue(ola)

                lt.addLast(listo,actual)
            else:

                listo = lt.newList()
                mp.put(diccionario,actual["artist_id"],listo)
                lt.addLast(listo,actual)

    alejita = mp.size(diccionario)

    return x, alejita

    
def requerimiento2():
    pass
def requerimiento3():
    pass
def requerimiento4():
    pass
def requerimiento5():
    pass

# Funciones utilizadas para comparar elementos dentro de una lista

def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1


def compareOffenses(offense1, offense2):
    """
    Compara dos tipos de crimenes
    """
    offense = me.getKey(offense2)
    if (offense1 == offense):
        return 0
    elif (offense1 > offense):
        return 1
    else:
        return -1

# Funciones de ordenamiento
