"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

# Funciones para agregar informacion al grafo
"""
Analyzer
    {'carreras': [Todas las carreras], 
     'companias':
        {'nombre_compania':
            {‘taxis_afiliados’: [id_taxi, id_taxi, id_taxi…], 
             ‘servicios’:  [trip_id, trip_id, trip_id…]
            }
        }
    }
"""

def newAnalyzer():
    """Inicializa el analizador

    Crea una lista vacia para guardar todas las carreras
    Crea un map ordenado de Companias (llave) y taxis (valor)
    """

    analyzer= {'carreras': None,
                'taxis':None,
                'companias': None
                }
    analyzer['carreras']= lt.newList('SINGLE_LINKED', compareIds)
    analyzer['taxis']= lt.newList('SINGLE_LINKED', compareCompany)
    analyzer['companias'] = om.newMap(omaptype='BST', comparefunction=compareCompany)

    return analyzer

def addCarrera(analyzer, carrera):

    lt.addLast(analyzer['carreras'], carrera)

def addTaxi(analyzer, carrera):
    taxi=carrera['taxi_id']
    if not lt.isPresent(analyzer['taxis'], taxi):
        lt.addLast(analyzer['taxis'], taxi)

def addCompanias(analyzer, carrera):
    
    compania= carrera['company']
    entry=om.get(analyzer['companias'], compania)

    if entry is None:
        entrada_compania= newDataEntry(analyzer, carrera)
        om.put(analyzer['companias'], compania, entrada_compania)

    else:
        entrada_compania=me.getValue(entry)
    # addCompania(analyzer,carrera)
    if not lt.isPresent(entrada_compania['taxis_afiliados'], carrera["taxi_id"]):
        lt.addLast(entrada_compania['taxis_afiliados'], carrera['taxi_id'])
    lt.addLast(entrada_compania['servicios'], carrera['trip_id'])
    
    return analyzer
    

def newDataEntry(analyzer, carrera):
    info_compania= {'taxis_afiliados': None,
                      'servicios': None, 
                      }
    info_compania['taxis_afiliados']= lt.newList(datastructure='SINGLE_LINKED', cmpfunction=compareIds)
    info_compania['servicios']= lt.newList(datastructure='SINGLE_LINKED', cmpfunction=compareIds)
    
    return(info_compania)

# ==============================
# Funciones de consulta
# ==============================

def TotalCarreras(analyzer):
    return lt.size(analyzer['carreras'])

def Totaltaxis(analyzer):
    total_taxis=0
    nombres= om.keySet(analyzer['companias'])
    iter=it.newIterator(nombres)
    while it.hasNext(iter):
        cada_compania=it.next(iter)
        nombre_compania=om.get(analyzer['companias'], cada_compania)
        if nombre_compania['key'] is not None:
            taxis= me.getValue(nombre_compania)['taxis_afiliados']
            if taxis is not None:
                num_taxis=m.size(taxis)
                total_taxis+=num_taxis

    return(total_taxis)
    
    # print("TOTAL TAXIS: "+ str(total_taxis))
    
    return (taxisXCompania)

def alturaCompanias(analyzer):
    return om.height(analyzer['companias'])

def TotalCompanias(analyzer):
    return om.size(analyzer['companias'])

def minKey(analyzer):
    return om.minKey(analyzer['companias'])

def maxKey(analyzer):
    return om.maxKey(analyzer['companias'])



# ==============================
# Funciones requerimiento
# ==============================
        
def CompaniasConTaxi(analyzer):
    lista_companias= lt.newList(datastructure='SINGLE_LINKED', cmpfunction=None)
    cada_compania= om.keySet(analyzer['companias'])
    lt.addLast(lista_companias, cada_compania)
    
    return lista_companias

def TaxisPorCompania(analyzer):
    taxisXCompania=om.newMap(omaptype='RBT', comparefunction=compareIds)
    total_taxis=0
    nombres= om.keySet(analyzer['companias'])
    # print(nombres)
    iter=it.newIterator(nombres)
    while it.hasNext(iter):
        cada_compania=it.next(iter)
        nombre_compania=om.get(analyzer['companias'], cada_compania)
        if nombre_compania['key'] is not None:
            taxis= me.getValue(nombre_compania)['taxis_afiliados']
            # print(taxis)
            if taxis is not None:
                num_taxis=m.size(taxis)
                total_taxis+=num_taxis
                om.put(taxisXCompania, num_taxis, cada_compania)
    

    
    return (taxisXCompania)

        
def ServiciosPorCompania(analyzer):
    ServiciosXCompania=om.newMap(omaptype='RBT', comparefunction=compareIds)
    total_servicios=0
    nombres= om.keySet(analyzer['companias'])
    # print(nombres)
    iter=it.newIterator(nombres)
    while it.hasNext(iter):
        cada_compania=it.next(iter)
        nombre_compania=om.get(analyzer['companias'], cada_compania)
        # print(nombre_compania)
        if nombre_compania['key'] is not None:
            servicios= me.getValue(nombre_compania)['servicios']
            # print(servicios)
            if servicios is not None:
                num_servicios=m.size(servicios)
                total_servicios+=num_servicios
                om.put(ServiciosXCompania, num_servicios, cada_compania)
                # print(nombre_compania['key'], num_servicios)
        # print(taxis)
    # print("TOTAL SERVICIOS: "+ str(total_servicios))
    
    return (ServiciosXCompania)


def RankingTaxis(analyzer, topM):
    
    # print(taxisPorCompania)
    RankingFinal=lt.newList(datastructure='SINGLE_LINKED', cmpfunction=None)
    rangoRanking=0

    taxisPorCompania=TaxisPorCompania(analyzer)
    while rangoRanking<topM:
        if taxisPorCompania is not None:
            MayorValor=om.maxKey(taxisPorCompania)
            nombre_compania=om.get(taxisPorCompania, MayorValor)
            lt.addLast(RankingFinal, nombre_compania)
            if om.contains(taxisPorCompania, MayorValor):
                om.remove(taxisPorCompania, MayorValor)
        
        rangoRanking+=1
   
    return RankingFinal

def RankingServicios(analyzer, topN):
    
    # print(taxisPorCompania)
    RankingFinal=lt.newList(datastructure='SINGLE_LINKED', cmpfunction=None)
    rangoRanking=0

    serviciosPorCompania=ServiciosPorCompania(analyzer)
    while rangoRanking<topN:
        if serviciosPorCompania is not None:
            MayorValor=om.maxKey(serviciosPorCompania)
            nombre_compania=om.get(serviciosPorCompania, MayorValor)
            lt.addLast(RankingFinal, nombre_compania)
            if om.contains(serviciosPorCompania, MayorValor):
                om.remove(serviciosPorCompania, MayorValor)
        
                
        rangoRanking+=1
   
    return RankingFinal

    


# ==============================
# Funciones de Comparacion
# ==============================

def compareIds(id1, id2):
    """
    Compara id de cada carrera carrera['trip ID']
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareCompany(company1, company2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    if (company1 == company2):
        return 0
    elif (company1 > company2):
        return 1
    else:
        return -1