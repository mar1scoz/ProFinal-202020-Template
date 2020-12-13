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


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config
from DISClib.DataStructures import listiterator as it
from DISClib.ADT import list as lt

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________
# 
# archivo_taxis= 'archivoprueba.csv'
archivo_taxis='taxi-trips-wrvz-psew-subset-small.csv' #archivo small
# archivo_taxis='taxi-trips-wrvz-psew-subset-medium.csv' #archivo mediano
# archivo_taxis='taxi-trips-wrvz-psew-subset-large.csv' #archivo grande




def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de taxis...")
    print("3- Compañias con al menos un taxi")
    print("4- Ranking Taxis Afiliados")
    print("5- Ranking Servicios Prestados")
    print("0- Salir")
    print("*******************************************")

def CargarDatos(): #CARGAR INFORMACION
    print("\nCargando información....")
    controller.loadData(cont, archivo_taxis)
    total_taxis= controller.Totaltaxis(cont)
    total_servicios= controller.TotalCarreras(cont)
    total_companias= controller.TotalCompanias(cont)
    print("\nNUMERO DE TAXIS:"+ str(total_taxis))
    print('NUMERO DE SERVICIOS:'+ str(total_servicios))
    print("NUMERO DE COMPAÑIAS: "+ str(total_companias-1))
    # print(controller.ServiciosPorCompania(cont))
    # print(cont)



def CompaniasConTaxi():
    Companias= controller.CompaniasConTaxi(cont)
    print("\nCOMPAÑIAS")
    print("---------------------------")
    i=1
    iter=it.newIterator(Companias)
    while it.hasNext(iter):
        compania= it.next(iter)
        iter2=it.newIterator(compania)
        while i<lt.size(compania):
            nombre_compania=lt.getElement(compania, i)
            print(nombre_compania)
            i+=1
    print("\nNUMERO DE COMPAÑIAS: "+ str(i-1))

def RankingTaxis():
    topM= int(input("INGRESE EL NUMERO DE COMPANIAS PARA EL RANKING: "+"\n"))
    Ranking= controller.RankingTaxis(cont, topM)
    i=1
    print("PUESTO"+"\t"+"COMPANIAS"+"\t"+"\t"+"\t"+"NUM TAXIS")
    print("---------------------------------------------------")
    iter=it.newIterator(Ranking)
    while it.hasNext(iter):
        cada_compania=it.next(iter)
        # print(cada_compania)
        nombre_compania= str(cada_compania['value'])
        numero_taxis=str(cada_compania['key'])
        print("{:<4}\t{:<25.25}\t{:<20.20}".format(i, nombre_compania, numero_taxis))
        i+=1

def RankingServicios():
    topN= int(input("INGRESE EL NUMERO DE COMPANIAS PARA EL RANKING: "+"\n"))
    Ranking= controller.RankingServicios(cont, topN)
    i=1
    print("PUESTO"+"\t"+"COMPANIAS"+"\t"+"\t"+"\t"+"NUM SERVICIOS")
    print("------------------------------------------------------")
    iter=it.newIterator(Ranking)
    while it.hasNext(iter):
        cada_compania=it.next(iter)
        # print(cada_compania)
        nombre_compania= str(cada_compania['value'])
        numero_servicios=str(cada_compania['key'])
        print("{:<1}\t{:<25.25}\t{:<20.20}".format(i, nombre_compania, numero_servicios))
        i+=1
   

    

        
        # print('Crimenes cargados: ' + str(controller.AccidentsSize(cont)))
        # print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        # print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        # print('Menor Llave: ' + str(controller.minKey(cont)))
        # print('Mayor Llave: ' + str(controller.maxKey(cont)))  

# ___________________________________________________
#  Menu principal
# ___________________________________________________

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        executiontime = timeit.timeit(CargarDatos, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    
    elif int(inputs[0]) == 3:
        executiontime = timeit.timeit(CompaniasConTaxi, number=1)
        print("\nTiempo de ejecución: " + str(executiontime))
    
    elif int(inputs[0]) == 4:
        executiontime = timeit.timeit(RankingTaxis, number=1)
        print("\nTiempo de ejecución: " + str(executiontime))
    
    elif int(inputs[0]) == 5:
        executiontime = timeit.timeit(RankingServicios, number=1)
        print("\nTiempo de ejecución: " + str(executiontime))
   
    else:
        sys.exit(0)
sys.exit(0)


