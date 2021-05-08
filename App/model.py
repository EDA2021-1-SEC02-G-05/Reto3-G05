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
import random
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

    diccio={"fecha":None}

    diccio["fecha"] =  om.newMap(omaptype='BRT',comparefunction=compareHour)

    return diccio

def orderMapSentimiento():

    diccion={"sentimiento":None}

    diccion["sentimiento"] =  lt.newList()

    return diccion

def addSentimiento(diccion, song3):
    

    lt.addLast(diccion["sentimiento"],song3)

    return diccion

def addFecha(diccio, song2):
    
    fecha = datetime.datetime.strptime(song2["created_at"],"%Y-%m-%d %H:%M:%S")
    quita = fecha.time()
    
    if om.contains(diccio["fecha"],quita):
        jef=om.get(diccio["fecha"],quita)
        lis = me.getValue(jef)
        lt.addLast(lis,song2)

    else:

        lis=lt.newList()
        om.put(diccio["fecha"],quita,lis)
        lt.addLast(lis,song2)

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

    tamano = om.size(info["generos"])
    altura = om.height(info["generos"])

    #numero de autores sin repetirse
    valores = om.values(info["generos"],0,tamano)
    iterador = it.newIterator(valores)
    diccionariototal = mp.newMap()

    while it.hasNext(iterador):

        actual = it.next(iterador)
        
        ite = it.newIterator(actual)

        while it.hasNext(ite):

            actual = it.next(ite)

            if mp.contains(diccionariototal,actual["artist_id"]):

                ola = mp.get(diccionariototal,actual["artist_id"])
                listo = me.getValue(ola)

                lt.addLast(listo,actual)
            else:

                listo = lt.newList()
                mp.put(diccionariototal,actual["artist_id"],listo)
                lt.addLast(listo,actual)

    tamanototal = mp.size(diccionariototal)

    val = om.values(info["generos"],0,tamano)
    iterador = it.newIterator(val)
    x = 0
    while it.hasNext(iterador):

        actual = it.next(iterador)

        x += lt.size(actual)

    return tamano,altura,tamanototal,x

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


def tablageneros(nom):

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

    return x,alejita 

    

def requerimiento2(dicci,d1,d2,e1,e2):


    d = om.values(dicci["danceability"],d1,d2)
    diccionario = mp.newMap()


    iterador = it.newIterator(d)

    while it.hasNext(iterador):

        actual = it.next(iterador)
        
        ite = it.newIterator(actual)


        while it.hasNext(ite):


            actual = it.next(ite)



            if float(actual["energy"]) >= e1 and float(actual["energy"]) <= e2:



                if mp.contains(diccionario,actual["track_id"]):

                    ola = mp.get(diccionario,actual["track_id"])
                    listo = me.getValue(ola)

                    lt.addLast(listo,actual)

                else:


                    listo = lt.newList()
                    mp.put(diccionario,actual["track_id"],listo)
                    lt.addLast(listo,actual)


    alejita = mp.size(diccionario)

    spiderman=mp.valueSet(diccionario)


    jefa=lt.size(spiderman)

    
    besos=random.randint(1,jefa)
    pecas=random.randint(1,jefa)
    bruno=random.randint(1,jefa)
    armando=random.randint(1,jefa)

    jamaica=lt.getElement(spiderman,besos)
    sos=lt.getElement(spiderman,pecas)
    xavi=lt.getElement(spiderman,bruno)
    armando=lt.getElement(spiderman,armando)


    pelea=jamaica["first"]["info"]
    sos=sos["first"]["info"]
    xavi=xavi["first"]["info"]
    armando=armando["first"]["info"]

    pelele=("Track 1: "+str(pelea["track_id"])+" with energy of "+str(pelea["energy"])+"  and danceability of "+str(pelea["danceability"]))
    messi=("Track 1: "+str(sos["track_id"])+" with energy of "+str(sos["energy"])+"  and danceability of "+str(sos["danceability"]))
    xavi=("Track 1: "+str(xavi["track_id"])+" with energy of "+str(xavi["energy"])+"  and danceability of "+str(xavi["danceability"]))
    armando=("Track 1: "+str(armando["track_id"])+" with energy of "+str(armando["energy"])+"  and danceability of "+str(armando["danceability"]))


    pep=(messi,pelele,xavi,armando)
 
    return alejita,pep



def requerimiento3(dicci,i1,i2,t1,t2):

    d = om.values(dicci["instrumentalness"],i1,i2)
    diccionario = mp.newMap()


    iterador = it.newIterator(d)

    while it.hasNext(iterador):

        actual = it.next(iterador)
        
        ite = it.newIterator(actual)


        while it.hasNext(ite):


            actual = it.next(ite)



            if float(actual["tempo"]) >= t1 and float(actual["tempo"]) <= t2:



                if mp.contains(diccionario,actual["track_id"]):

                    ola = mp.get(diccionario,actual["track_id"])
                    listo = me.getValue(ola)

                    lt.addLast(listo,actual)

                else:


                    listo = lt.newList()
                    mp.put(diccionario,actual["track_id"],listo)
                    lt.addLast(listo,actual)


    alejita = mp.size(diccionario)

    spiderman=mp.valueSet(diccionario)


    jefa=lt.size(spiderman)

    
    besos=random.randint(1,jefa)
    pecas=random.randint(1,jefa)
    bruno=random.randint(1,jefa)
    armando=random.randint(1,jefa)



    jamaica=lt.getElement(spiderman,besos)
    sos=lt.getElement(spiderman,pecas)
    xavi=lt.getElement(spiderman,bruno)
    armando=lt.getElement(spiderman,armando)


    pelea=jamaica["first"]["info"]
    sos=sos["first"]["info"]
    xavi=xavi["first"]["info"]
    armando=armando["first"]["info"]

    pelele=("Track 1: "+str(pelea["track_id"])+" with instrumentalness of "+str(pelea["instrumentalness"])+"  and tempo of "+str(pelea["tempo"]))
    messi=("Track 1: "+str(sos["track_id"])+" with instrumentalness of "+str(sos["instrumentalness"])+"  and tempo of "+str(sos["tempo"]))
    xavi=("Track 1: "+str(xavi["track_id"])+" with instrumentalness of "+str(xavi["instrumentalness"])+"  and tempo of "+str(xavi["tempo"]))
    armando=("Track 1: "+str(armando["track_id"])+" with instrumentalness of "+str(armando["instrumentalness"])+"  and tempo of "+str(armando["tempo"]))


    pep=(messi,pelele,xavi,armando)

    return alejita,pep


def requerimiento4(info,nom1,nom2,nom3,nom4,des1,des2):
    
    gene1 = tablageneros(nom1)
    llave = mp.get(gene1,nom1)#Da la llave y el valor de la tabla de hash 
    valor = me.getValue(llave)# El valor de la llave del genero 
    rango1 = om.values(info["generos"],valor[0],valor[1])

    diccionario = mp.newMap()
    diccionarionuevo = mp.newMap()
    iterador = it.newIterator(rango1)
    suma1 = 0
    
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
    
    gene2 = tablageneros(nom2)
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


    gene3 = tablageneros(nom3)
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


def requerimiento5(info,diccio,diccion,rangoinf,rangomay):  

    
    diccionarioo = mp.newMap()
    dumar= om.values(diccio["fecha"],rangoinf,rangomay)
    iteradorr = it.newIterator(dumar)
    while it.hasNext(iteradorr):
        act = it.next(iteradorr)
        iterardent = it.newIterator(act)
        while it.hasNext(iterardent):
            actuales = it.next(iterardent)
            id = actuales["created_at"]
            if not mp.contains(diccionarioo,id):
                mp.put(diccionarioo,id,actuales)
                       
    gene = tablageneros("Metal")
    llave = mp.get(gene,"Metal")
    valor = me.getValue(llave)
    rango3 = om.values(info["generos"],valor[0],valor[1])
    iterador = it.newIterator(rango3)
    suma = 0
    while it.hasNext(iterador):
        actu = it.next(iterador)
        iterardentro = it.newIterator(actu)
        while it.hasNext(iterardentro):
            actual = it.next(iterardentro)
            if mp.contains(diccionarioo,actual["created_at"]):
                suma += 1
    gene = tablageneros("Rock")
    llave = mp.get(gene,"Rock")
    valor = me.getValue(llave)
    rango3 = om.values(info["generos"],valor[0],valor[1])
    iterador = it.newIterator(rango3)
    suma2 = 0
    while it.hasNext(iterador):
        actu = it.next(iterador)
        iterardentro = it.newIterator(actu)
        while it.hasNext(iterardentro):
            actual = it.next(iterardentro)
            if mp.contains(diccionarioo,actual["created_at"]):
                suma2 += 1
    
    gene = tablageneros("Pop")
    llave = mp.get(gene,"Pop")
    valor = me.getValue(llave)
    rango3 = om.values(info["generos"],valor[0],valor[1])
    iterador = it.newIterator(rango3)
    suma3 = 0
    while it.hasNext(iterador):
        actu = it.next(iterador)
        iterardentro = it.newIterator(actu)
        while it.hasNext(iterardentro):
            actual = it.next(iterardentro)
            if mp.contains(diccionarioo,actual["created_at"]):
                suma3 += 1
    
    gene = tablageneros("Chill-out")
    llave = mp.get(gene,"Chill-out")
    valor = me.getValue(llave)
    rango3 = om.values(info["generos"],valor[0],valor[1])
    iterador = it.newIterator(rango3)
    suma4 = 0
    while it.hasNext(iterador):
        actu = it.next(iterador)
        iterardentro = it.newIterator(actu)
        while it.hasNext(iterardentro):
            actual = it.next(iterardentro)
            if mp.contains(diccionarioo,actual["created_at"]):
                suma4 += 1

    gene = tablageneros("Hip Hop")
    llave = mp.get(gene,"Hip Hop")
    valor = me.getValue(llave)
    rango3 = om.values(info["generos"],valor[0],valor[1])
    iterador = it.newIterator(rango3)
    suma5 = 0
    while it.hasNext(iterador):
        actu = it.next(iterador)
        iterardentro = it.newIterator(actu)
        while it.hasNext(iterardentro):
            actual = it.next(iterardentro)
            if mp.contains(diccionarioo,actual["created_at"]):
                suma5 += 1
    gene = tablageneros("Down-tempo")
    llave = mp.get(gene,"Down-tempo")
    valor = me.getValue(llave)
    rango3 = om.values(info["generos"],valor[0],valor[1])
    iterador = it.newIterator(rango3)
    suma6 = 0
    while it.hasNext(iterador):
        actu = it.next(iterador)
        iterardentro = it.newIterator(actu)
        while it.hasNext(iterardentro):
            actual = it.next(iterardentro)
            if mp.contains(diccionarioo,actual["created_at"]):
                suma6 += 1
    gene = tablageneros("Reggae")
    llave = mp.get(gene,"Reggae")
    valor = me.getValue(llave)
    rango3 = om.values(info["generos"],valor[0],valor[1])
    iterador = it.newIterator(rango3)
    suma7 = 0
    while it.hasNext(iterador):
        actu = it.next(iterador)
        iterardentro = it.newIterator(actu)
        while it.hasNext(iterardentro):
            actual = it.next(iterardentro)
            if mp.contains(diccionarioo,actual["created_at"]):
                suma7 += 1
    gene = tablageneros("Jazz and Funk")
    llave = mp.get(gene,"Jazz and Funk")
    valor = me.getValue(llave)
    rango3 = om.values(info["generos"],valor[0],valor[1])
    iterador = it.newIterator(rango3)
    suma8 = 0
    while it.hasNext(iterador):
        actu = it.next(iterador)
        iterardentro = it.newIterator(actu)
        while it.hasNext(iterardentro):
            actual = it.next(iterardentro)
            if mp.contains(diccionarioo,actual["created_at"]):
                suma8 += 1
    gene = tablageneros("R&B")
    llave = mp.get(gene,"R&B")
    valor = me.getValue(llave)
    rango3 = om.values(info["generos"],valor[0],valor[1])
    iterador = it.newIterator(rango3)
    suma9 = 0
    while it.hasNext(iterador):
        actu = it.next(iterador)
        iterardentro = it.newIterator(actu)
        while it.hasNext(iterardentro):
            actual = it.next(iterardentro)
            if mp.contains(diccionarioo,actual["created_at"]):
                suma9 += 1

    total = suma+suma2+suma3+suma4+suma5+suma6+suma7+suma8+suma9


    
    return suma,suma2,suma3,suma4,suma5,suma6,suma7,suma8,suma9,total





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

def compareHour (hour1,hour2):
    if (hour1.hour == hour2.hour) and (hour1.minute == hour2.minute):
        return 0
    elif (hour1.hour > hour2.hour):
        return 1 
    else:
        return -1

def compareAvg(avg1, avg2):
 
    if (int(avg1) == int(avg2)):
        return 0
    elif (int(avg1) > int(avg2)):
        return 1
    else:
        return -1