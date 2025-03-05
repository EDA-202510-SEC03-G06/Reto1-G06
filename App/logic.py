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
    idx_year = headers.index("year_collection")
    idx_load_time = headers.index("load_time")
    idx_source = headers.index("source")
    idx_frequency = headers.index("freq_collection")
    idx_department = headers.index("state_name")
    idx_product = headers.index("commodity")
    idx_unit = headers.index("unit_measurement")
    idx_value = headers.index("value")
    registros_año=[]
    
    for registro in catalog["data"]:
        if registro[idx_year] == anio:
            registros_año.append(registro)
    if not registros_año:
        return{"tiempo_ms": ((time.time() - start_time) * 1000),
               "total_reg":0,
               "ultimo_reg":None}
    ultimo_reg = registros_año[0]
    for registro in registros_año:
        if registro[idx_load_time] > ultimo_reg[idx_load_time]:
            ultimo_reg = registro
    resultado = {
            "tiempo_ms": ((time.time() - start_time) * 1000),
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


def req_2(control, departamento):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    
    start_time = time.time()
    registros = []

    for r in control["data"]:
        if r[5].upper() == departamento.upper():  
            registros.append(r)

    if not registros:
        return None, 0, (time.time() - start_time) * 1000

    
    ultimo_registro = registros[0]
    for r in registros:
        if r[9] > ultimo_registro[9]:  
            ultimo_registro = r

   
    fecha_carga = ultimo_registro[9].split(" ")[0]

    
    resultado = {
        "year": ultimo_registro[6],          
        "fecha_carga": fecha_carga,         
        "fuente": ultimo_registro[0],        
        "frecuencia": ultimo_registro[8],   
        "departamento": ultimo_registro[5],  
        "producto": ultimo_registro[1],      
        "unidad": ultimo_registro[3],        
        "valor": ultimo_registro[10]         
    }

    return resultado, len(registros), (time.time() - start_time) * 1000

def req_3(control, departamento, anio_inicial, anio_final):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = time.time()

    registros = []
    for r in control["data"]:
        if r[4].upper() == departamento.upper() and anio_inicial <= int(r[6]) <= anio_final:
            registros.append(r)

    total_registros = len(registros)
    total_survey = sum(1 for r in registros if r[0] == "SURVEY")
    total_census = sum(1 for r in registros if r[0] == "CENSUS")

    tiempo_ejecucion = (time.time() - start_time) * 1000

    return registros, total_registros, total_survey, total_census, tiempo_ejecucion


def req_4(control, tipo_producto, anio_inicial, anio_final):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    registros = []
    total_survey = 0
    total_census = 0
    tiempo_ejecucion = 0
    start_time = time.time()
    for r in control["data"]:
        if r[1].upper() == tipo_producto.upper() and anio_inicial <= int(r[6]) <= anio_final:
            registros.append(r)
            if r[0] == "SURVEY":
             total_survey += 1
            elif r[0] == "CENSUS":
                total_census += 1
    total_registros = len(registros)
    if total_registros > 20:
        registros = registros[:5] + registros[-5:]
        tiempo_ejecucion = (time.time() - start_time) * 1000
    return registros, total_registros, total_survey, total_census, tiempo_ejecucion


def req_5(catalog, categoria, anio_inicio, anio_fin):
    """
    Retorna el resultado del requerimiento 5
    """
    start_time=time.time()
    headers = catalog["headers"]
    idx_year = headers.index("year_collection")
    idx_load_time = headers.index("load_time")
    idx_source = headers.index("source")
    idx_frequency = headers.index("freq_collection")
    idx_department = headers.index("state_name")
    idx_product = headers.index("commodity")
    idx_unit = headers.index("unit_measurement")
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
                
    tiempo_total = ((time.time() - start_time) * 1000)
    
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

def req_6(catalog, departamento, fecha_inicio, fecha_fin):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    
    start_time = time.time()
    
    registros_filtrados = [
        reg for reg in catalog['data']
        if reg[5].upper() == departamento.upper() and fecha_inicio <= reg[9][:10] <= fecha_fin
    ]
    
    total_registros = len(registros_filtrados)
    total_survey = sum(1 for reg in registros_filtrados if reg[0] == "SURVEY")
    total_census = sum(1 for reg in registros_filtrados if reg[0] == "CENSUS")
    
    if total_registros > 20:
        registros_mostrados = registros_filtrados[:5] + registros_filtrados[-5:]
    else:
        registros_mostrados = registros_filtrados
    
    execution_time = (time.time() - start_time) * 1000  
    
    resultado = {
        "total_registros": total_registros,
        "total_survey": total_survey,
        "total_census": total_census,
        "registros_mostrados": registros_mostrados,
        "execution_time": execution_time
    }
    
    return resultado

def req_7(catalog, departamento, anio_inicio, anio_fin):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time = time.time()
    headers = catalog["headers"]
    print("Encabezados disponibles:", headers)  
    idx_year = headers.index("year_collection")
    idx_department = headers.index('state_name')
    idx_unit = headers.index('unit_measurement')
    idx_value = headers.index('value')
    idx_source = headers.index('source')
    registros = []
    for registro in catalog["data"]:
        year = int(registro[idx_year])
        if (registro[idx_department].upper() == departamento.upper() and 
            anio_inicio <= year <= anio_fin and "$" in registro[idx_unit]):
            registros.append(registro)
    if not registros:
        return {"mensaje": "No hay datos para el departamento y rango de años dados"}
    ingresos_validos = [int(r[idx_value]) for r in registros if r[idx_value].isdigit()]
    if not ingresos_validos:
        return {"mensaje": "No hay valores válidos de ingresos"} 
    max_ingreso = max(ingresos_validos)
    min_ingreso = min(ingresos_validos)
    registros_max = [r for r in registros if r[idx_value].isdigit() and int(r[idx_value]) == max_ingreso]
    registros_min = [r for r in registros if r[idx_value].isdigit() and int(r[idx_value]) == min_ingreso]
    total_survey = sum(1 for r in registros if r[idx_source] == "SURVEY")
    total_census = sum(1 for r in registros if r[idx_source] == "CENSUS")
    tiempo_ms = (time.time() - start_time) * 1000
    return {"tiempo_ms": tiempo_ms,"total_registros": len(registros),
        "mayor_ingreso": {"año": registros_max[0][idx_year],"valor": max_ingreso,"num_registros": len(registros_max)},
        "menor_ingreso": {"año": registros_min[0][idx_year],"valor": min_ingreso,"num_registros": len(registros_min)},
        "total_survey": total_survey,
        "total_census": total_census}

def req_8(catalog, medida, fecha_inicio, fecha_fin):
    tim = time.time()
    header = catalog["headers"]
    idx_dep = header.index("state_name")
    idx_carga = header.index("load_time")
    idx_src = header.index("source")
    idx_unit = header.index("unit_measurement")
    idx_prod = header.index("commodity")
    
    registros = [reg for reg in catalog["data"] if reg[idx_unit].upper() == medida.upper() and fecha_inicio <= reg[idx_carga][:10] <= fecha_fin]
    total_reg = len(registros)
    total_sur = sum(1 for reg in registros if reg[idx_src] == "SURVEY")
    total_cen = sum(1 for reg in registros if reg[idx_src] == "CENSUS")
    registros_most = registros[:5] + registros[-5:] if total_reg > 20 else registros
    registros_res = [{"source": reg[idx_src], "fecha_carga": reg[idx_carga].split(" ")[0], "unidad": reg[idx_unit], "producto": reg[idx_prod], "departamento": reg[idx_dep]} for reg in registros_most]
    execution_time = (time.time() - tim) * 1000  
    return {"total_registros": total_reg, "total_survey": total_sur, "total_census": total_cen, "registros": registros_res, "execution_time": execution_time}

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