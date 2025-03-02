import csv
import os
import time
from DataStructures.List import single_linked_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'
csv.field_size_limit(2147483647) 



# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    catalog["data"]=[]
    filename =  "Data/" + filename
    archivo = open(filename, mode="r", encoding="utf-8")
    lector = csv.reader(archivo)
    encabezados = next(lector)
    catalog["headers"] = encabezados
    for fila in lector:
        catalog["data"].append(fila)
    archivo.close()
    
    # TODO: Realizar la carga de datos
    return catalog
 
# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    for registro in catalog["data"]:
        if registro[0] == id:
            return registro
    return None
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    


def req_1(catalog,anio):
    """
    Retorna el resultado del requerimiento 1
    """
    start_time=time.time()
    headers = catalog["headers"]
    idx_year = headers.index('year_collection')
    idx_load_time = headers.index('load_time')
    idx_source = headers.index('source')
    idx_frequency = headers.index('freq_collection')
    idx_department = headers.index('state_name')
    idx_product = headers.index('commodity')
    idx_unit = headers.index('unit_measurement')
    idx_value = headers.index('value')
    registros_año=[]
    
    for registro in catalog["data"]:
        if registro[idx_year] == anio:
            registros_año.append(registro)
    if not registros_año:
        return{"tiempo_ms": delta_time(start_time, get_time()),
               "total_reg":0,
               "ultimo_reg":None}
    ultimo_reg = registros_año[0]
    for registro in registros_año:
        if registro[idx_load_time] > ultimo_reg[idx_load_time]:
            ultimo_reg = registro
    resultado = {
            "tiempo_ms": delta_time(start_time, get_time()),
            "total_registros": len(registros_año),
            "ultimo_registro": {
            "year": ultimo_reg[idx_year],
            "fecha_carga": ultimo_reg[idx_load_time].split(" ")[0],
            "fuente": ultimo_reg[idx_source],
            "frecuencia": ultimo_reg[idx_frequency],
            "departamento": ultimo_reg[idx_department],
            "producto": ultimo_reg[idx_product],
            "unidad": ultimo_reg[idx_unit],
            "valor": ultimo_reg[idx_value]}}
                                        
    # TODO: Modificar el requerimiento 1
    return resultado, resultado["total_registros"], resultado["tiempo_ms"]


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog, categoria, anio_inicio, anio_fin):
    """
    Retorna el resultado del requerimiento 5
    """
    start_time=time.time()
    headers = catalog["headers"]
    idx_year = headers.index('year_collection')
    idx_load_time = headers.index('load_time')
    idx_source = headers.index('source')
    idx_frequency = headers.index('freq_collection')
    idx_department = headers.index('state_name')
    idx_product = headers.index('commodity')
    idx_unit = headers.index('unit_measurement')
    idx_value = headers.index('value')
    idx_category = headers.index("statical_category")
    registros_fil = []
    total_survey = 0
    total_census = 0
    
    for registro in catalog["data"]:
        anio = registro[idx_year]
        
        if registro[idx_category] == categoria and anio_inicio <= anio <= anio_fin:
            registros_fil.append(registro)
            
            if registro[idx_source] == "SURVEY":
                total_survey += 1
            elif registro[idx_source] == "CENSUS":
                total_census += 1
                
    tiempo_total = delta_time(start_time, get_time())
    
    registros_resultado = []
    if len(registros_fil) > 20:
        registros_most = registros_fil[:5] + registros_fil[-5:]
    else:
        registros_most = registros_fil
    
    for registro in registros_most:
        registros_resultado.append({
            "source": registro[idx_source],
            "year": registro[idx_year],
            "fecha_carga": registro[idx_load_time].split(" ")[0],
            "frecuencia": registro[idx_frequency],
            "departamento": registro[idx_department],
            "unidad": registro[idx_unit],
            "producto": registro[idx_product]
        })
        
    resultado = {
        "tiempo_ms": tiempo_total,
        "total_registros": len(registros_fil),
        "total_survey": total_survey,
        "total_census": total_census,
        "registros": registros_resultado
    }
        
    # TODO: Modificar el requerimiento 5
    return resultado

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed