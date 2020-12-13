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

import config as cf
from App import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def loadData(analyzer, archivo_taxis):
    # t1_start = process_time()
    """
    Carga los datos de los archivos CSV en el modelo
    """
    taxisfile = cf.data_dir + archivo_taxis
    input_file = csv.DictReader(open(taxisfile, encoding="utf-8-sig"),
                                delimiter=",")
    for carrera in input_file:
        model.addCarrera(analyzer, carrera)
        # model.addTaxi(analyzer, carrera)
        model.addCompanias(analyzer, carrera)
        
    # t1_stop = process_time() #tiempo final
    # print("Tiempo de ejecución ",t1_stop-t1_start," segundos") 
    return analyzer



# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def TotalCarreras(analyzer):
    """
    Numero de crimenes leidos
    """
    return model.TotalCarreras(analyzer)

def Totaltaxis(analyzer):
    """
    Numero de crimenes leidos
    """
    return model.Totaltaxis(analyzer)

def alturaCompanias(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.alturaCompanias(analyzer)


def TotalCompanias(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.TotalCompanias(analyzer)


def minKey(analyzer):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer)


def maxKey(analyzer):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer)

def CompaniasConTaxi(analyzer):
    return model.CompaniasConTaxi(analyzer)

def TaxisPorCompania(analyzer):
    return model.TaxisPorCompania(analyzer)

def ServiciosPorCompania(analyzer):
    return model.ServiciosPorCompania(analyzer)

def RankingTaxis(analyzer, topM):
    return model.RankingTaxis(analyzer, topM)

def RankingServicios(analyzer, topN):
    return model.RankingServicios(analyzer, topN)