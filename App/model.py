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
    
    dicci = {}

    dicci['instrumentalness'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['acousticness'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['liveness'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['speechiness'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['energy'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['danceability'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    dicci['valence'] = om.newMap(omaptype='BRT',comparefunction=compareDates)

    return dicci 


def newOrderMap():

    info={"generos":None}

    info["generos"] =  om.newMap(omaptype='BRT',comparefunction=compareTempo)

    return info

def newOrderMapSentimiento():

    diccio={"sentimiento":None}

    diccio["sentimiento"] =  om.newMap(omaptype='BRT')

    return diccio

def addFecha(diccio, song2):
    
    fecha = song2["created_at"]
    filtro = fecha[11:19]
    quita =filtro.replace(":","")
    if om.contains(diccio["sentimiento"],quita):
        jef=om.get(diccio["sentimiento"],quita)
        lis = me.getValue(jef)
        lt.addLast(lis,song2)

    else:

        lisa=lt.newList()
        om.put(diccio["sentimiento"],quita,lisa)
        lt.addLast(lisa,song2)

    return diccio


def addCancion(info, song):

    if om.contains(info["generos"],float(song["tempo"])):
        jef=om.get(info["generos"],float(song["tempo"]))
        lis = me.getValue(jef)
        lt.addLast(lis,song)

    else:

        lisa=lt.newList()
        om.put(info["generos"],float(song["tempo"]),lisa)
        lt.addLast(lisa,song)

    return info

def parte2(info):

    tamañodatos = om.size(info["generos"])
   
    return tamañodatos

def tablageneros(nom,des1,des2):

    generos= mp.newMap()
    if nom == "Reggae":
        mp.put(generos,"Reggae",(60,90))
    elif nom == "Down-tempo":
        mp.put(generos,"Down-tempo",(70,100))
    elif nom == "Chill-out":
        mp.put(generos,"Chill-out",(90,120))
    elif nom == "Hip Hop":
        mp.put(generos,"Hip Hop",(85,115))
    elif nom == "Jazz and Funk":
        mp.put(generos,"Jazz and Funk",(120,125))
    elif nom == "Pop":
        mp.put(generos,"Pop",(100,130))
    elif nom == "R&B":
        mp.put(generos,"R&B",(60,80))
    elif nom == "Rock":
        mp.put(generos,"Rock",(110,140))
    elif nom == "Metal":
        mp.put(generos,"Metal",(100,160))
    return generos



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
def requerimiento4(info,nom1,nom2,nom3,nom4,des1,des2):
    

    gene1 = tablageneros(nom1,des1,des2)
    llave = mp.get(gene1,nom1)#Da la llave y el valor de la tabla de hash 
    valor = me.getValue(llave)# El valor de la llave del genero 
    rango1 = om.values(info["generos"],valor[0],valor[1])

    diccionario = mp.newMap()
    diccionarionuevo = mp.newMap()
    iterador = it.newIterator(rango1)
    suma1 =0
    
    while it.hasNext(iterador):

        actu = it.next(iterador)
        suma1 += lt.size(actu)

        iterardentro = it.newIterator(actu)

        while it.hasNext(iterardentro):

            actual = it.next(iterardentro)
            if mp.contains(diccionario,actual["tempo"]):

                ola = mp.get(diccionario,actual["tempo"])
                listo = me.getValue(ola)
                lt.addLast(listo,actual)

            else:

                listo = lt.newList()
                mp.put(diccionario,actual["tempo"],listo)
                lt.addLast(listo,actual)

            if mp.contains(diccionarionuevo,actual["artist_id"]):

                llaves = mp.get(diccionarionuevo,actual["artist_id"])
                valores = me.getValue(llaves)

                lt.addLast(valores,actual)
            else:

                infor = lt.newList()
                mp.put(diccionarionuevo,actual["artist_id"],infor)
                lt.addLast(infor,actual)

    tamano1 = mp.size(diccionarionuevo)
    
    gene2 = tablageneros(nom2,des1,des2)
    llave = mp.get(gene2,nom2)
    valor2 = me.getValue(llave)
    rango2 = om.values(info["generos"],valor2[0],valor2[1])

    diccionario2 = mp.newMap()
    diccionarionuevo2 = mp.newMap()
    iterador = it.newIterator(rango2)
    suma2 = 0
    while it.hasNext(iterador):

        actu = it.next(iterador)
        suma2 += lt.size(actu)

        iterardentro = it.newIterator(actu)

        while it.hasNext(iterardentro):

            actual = it.next(iterardentro)
            if mp.contains(diccionario2,actual["tempo"]):

                ola = mp.get(diccionario2,actual["tempo"])
                listo = me.getValue(ola)

                lt.addLast(listo,actual)
            else:

                listo = lt.newList()
                mp.put(diccionario2,actual["tempo"],listo)
                lt.addLast(listo,actual)
            
            if mp.contains(diccionarionuevo2,actual["artist_id"]):

                llaves = mp.get(diccionarionuevo2,actual["artist_id"])
                valores = me.getValue(llaves)

                lt.addLast(valores,actual)
            else:

                infor = lt.newList()
                mp.put(diccionarionuevo2,actual["artist_id"],infor)
                lt.addLast(infor,actual)

    tamano2 = mp.size(diccionarionuevo2)


    gene3 = tablageneros(nom3,des1,des2)
    llave = mp.get(gene3,nom3)
    valor3 = me.getValue(llave)
    rango3 = om.values(info["generos"],valor3[0],valor3[1])

    diccionario3 = mp.newMap()
    diccionarionuevo3 = mp.newMap()
    iterador = it.newIterator(rango3)

    suma3= 0
    while it.hasNext(iterador):

        actu = it.next(iterador)

        suma3 += lt.size(actu)

        iterardentro = it.newIterator(actu)

        while it.hasNext(iterardentro):

            actual = it.next(iterardentro)
            if mp.contains(diccionario3,actual["tempo"]):

                ola = mp.get(diccionario3,actual["tempo"])
                listo = me.getValue(ola)

                lt.addLast(listo,actual)
            else:

                listo = lt.newList()
                mp.put(diccionario3,actual["tempo"],listo)
                lt.addLast(listo,actual)

            if mp.contains(diccionarionuevo3,actual["artist_id"]):

                llaves = mp.get(diccionarionuevo3,actual["artist_id"])
                valores = me.getValue(llaves)

                lt.addLast(valores,actual)
            else:

                infor = lt.newList()
                mp.put(diccionarionuevo3,actual["artist_id"],infor)
                lt.addLast(infor,actual)

    tamano3 = mp.size(diccionarionuevo3)

    diccionarionuevo4 = mp.newMap()
    total = suma1+suma2+suma3
    suma4= 0
    if nom4 != "":
        
        rango4 = om.values(info["generos"],des1,des2)

        diccionario4 = mp.newMap()
        iterador = it.newIterator(rango4)

        suma4 = 0
        while it.hasNext(iterador):

            actu = it.next(iterador)

            suma4 += lt.size(actu)

            iterardentro = it.newIterator(actu)

            while it.hasNext(iterardentro):

                actual = it.next(iterardentro)
                if mp.contains(diccionario4,actual["tempo"]):

                    ola = mp.get(diccionario4,actual["tempo"])
                    listo = me.getValue(ola)

                    lt.addLast(listo,actual)
                else:

                    listo = lt.newList()
                    mp.put(diccionario4,actual["tempo"],listo)
                    lt.addLast(listo,actual)
                if mp.contains(diccionarionuevo4,actual["artist_id"]):

                    llaves = mp.get(diccionarionuevo4,actual["artist_id"])
                    valores = me.getValue(llaves)

                    lt.addLast(valores,actual)
                else:

                    infor = lt.newList()
                    mp.put(diccionarionuevo4,actual["artist_id"],infor)
                    lt.addLast(infor,actual)

    tamano4 = mp.size(diccionarionuevo4)

    llave1=mp.keySet(diccionarionuevo)
    llave2=mp.keySet(diccionarionuevo2)
    llave3=mp.keySet(diccionarionuevo3)
    

    iterador = it.newIterator(llave1)
    primero = lt.newList()
    while it.hasNext(iterador):

        actu = it.next(iterador)

        lt.addLast(primero,actu)

    artistas1= lt.subList(primero,0,12)



    iterador = it.newIterator(llave2)
    segundo = lt.newList()
    while it.hasNext(iterador):

        actu = it.next(iterador)

        lt.addLast(segundo,actu)

    artistas2= lt.subList(segundo,0,12)


    iterador = it.newIterator(llave3)
    tercero = lt.newList()
    while it.hasNext(iterador):

        actu = it.next(iterador)

        lt.addLast(tercero,actu)

    artistas3= lt.subList(tercero,0,12)

    return suma1,suma2,suma3,total,suma4,tamano1,tamano2,tamano3,tamano4,artistas1,artistas2,artistas3

    
def requerimiento5(diccio,rangoinf,rangomay):

        

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

def compareTempo(tempo1, tempo2):
    """
    Compara dos fechas
    """
    if (tempo1 == tempo2):
        return 0
    elif (tempo1 > tempo2):
        return 1
    else:
        return -1
# Funciones de ordenamiento
