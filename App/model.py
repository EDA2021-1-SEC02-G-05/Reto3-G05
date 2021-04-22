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
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
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
    dicci = {'Instrumentalness': None,'Acousticness': None,"Liveness":None,"Speechiness":None,"Energy":None,"Danceability":None, "Valence":None }

    dicci['Instrumentalness'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['Acousticness'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['Liveness'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['Speechiness'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['Energy'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['Danceability'] = om.newMap(omaptype='BRT',comparefunction=compareDates)


    dicci['Valence'] = om.newMap(omaptype='BRT',comparefunction=compareDates)



    return dicci




def addsong(dicci, song):


    if om.contains(dicci["Instrumentalness"],song["Instrumentalness"]):
            jef=om.get(dicci["Instrumentalness"],song["Instrumentalness"])
            lis = me.getValue(jef)
            lt.addLast(lis,song)

    else:

            lisa=lt.newList()
            lt.addLast(lisa,song)
            om.put(dicci["Instrumentalness"],song["Instrumentalness"],lisa)


    if om.contains(dicci["Acousticness"],song["Acousticness"]):
            jef=om.get(dicci["Acousticness"],song["Acousticness"])
            lis = me.getValue(jef)
            lt.addLast(lis,song)

    else:

            lisa=lt.newList()
            lt.addLast(lisa,song)
            om.put(dicci["Acousticness"],song["Acousticness"],lisa)


    if om.contains(dicci["Liveness"],song["Liveness"]):
            jef=om.get(dicci["Liveness"],song["Liveness"])
            lis = me.getValue(jef)
            lt.addLast(lis,song)

    else:

            lisa=lt.newList()
            lt.addLast(lisa,song)
            om.put(dicci["Liveness"],song["Liveness"],lisa)


    if om.contains(dicci["Speechiness"],song["Speechiness"]):
            jef=om.get(dicci["Speechiness"],song["Speechiness"])
            lis = me.getValue(jef)
            lt.addLast(lis,song)

    else:

            lisa=lt.newList()
            lt.addLast(lisa,song)
            om.put(dicci["Speechiness"],song["Speechiness"],lisa)



    if om.contains(dicci["Energy"],song["Energy"]):
            jef=om.get(dicci["Energy"],song["Energy"])
            lis = me.getValue(jef)
            lt.addLast(lis,song)

    else:

            lisa=lt.newList()
            lt.addLast(lisa,song)
            om.put(dicci["Energy"],song["Energy"],lisa)


    if om.contains(dicci["Danceability"],song["Danceability"]):
            jef=om.get(dicci["Danceability"],song["Danceability"])
            lis = me.getValue(jef)
            lt.addLast(lis,song)

    else:

            lisa=lt.newList()
            lt.addLast(lisa,song)
            om.put(dicci["Danceability"],song["Danceability"],lisa)

    if om.contains(dicci["Valence"],song["Valence"]):
            jef=om.get(dicci["Valence"],song["Valence"])
            lis = me.getValue(jef)
            lt.addLast(lis,song)

    else:
            lisa=lt.newList()
            lt.addLast(lisa,song)
            om.put(dicci["Valence"],song["Valence"],lisa)

    return dicci

def crimesSize(dicci):
    """
    Número de crimenes
    """
    return om.height(dicci['Instrumentalness'])




    










    
# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

def requerimiento1():
    pass
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
