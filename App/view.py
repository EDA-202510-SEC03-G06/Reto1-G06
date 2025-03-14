from gettext import Catalog
import sys
import App.logic as logic

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def new_logic():
    """
        Se crea una instancia del controlador
    """
    catalog = {"data": [], "headers": []}
    return catalog
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    archivo = input("Ingrese el nombre del archivo CSV: ")
    catalog = logic.load_data(control, archivo)
    print("")
    print("Carga completada")
    print("Archivo procesado:", archivo)
    print("Total de registros cargados:", len(catalog["data"]))
    print("Columnas detectadas:", ", ".join(catalog["headers"]))


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    id = input("Ingrese el ID a buscar: ")
    registro = logic.get_data(control ,id)
    if registro:
        print("Registro encontrado:", registro)
    else:
        print("Registro no encontrado.")
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    anio = input("ingrese el año a consultar (YYYY): ")
    resultado, total, tiempo = logic.req_1(control, anio)
    print("")
    print("Requerimiento 1- resultados:")
    print("Año consultado: ",anio)
    print("Total de registros encontrados: ", total)
    print("Tiempo de ejecución en milisegundos: ",tiempo)
    resultado = resultado["ultimo_registro"]
    print("")   
    print("Registro más reciente:")
    print("Año de recopilación:", resultado["year"])
    print("Fecha de carga:", resultado["fecha_carga"])
    print("Fuente:", resultado["fuente"])
    print("Frecuencia:", resultado["frecuencia"])
    print("Departamento:", resultado["departamento"])
    print("Producto:", resultado["producto"])
    print("Unidad:", resultado["unidad"])
    print("Valor:", resultado["valor"])
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    
    departamento = input("\n Ingrese el nombre del departamento a consultar: ").upper()
    resultado, total, tiempo = logic.req_2(control, departamento)

    if resultado:
        print("\n• Requerimiento 2 - resultados:")
        print(f"Año de recopilación: {resultado['year']}")
        print(f"Fecha de carga: {resultado['fecha_carga']}")  
        print(f"Tipo de fuente/origen: {resultado['fuente']}")
        print(f"Frecuencia de la recopilación: {resultado['frecuencia']}")
        print(f"Nombre del departamento: {resultado['departamento']}")
        print(f"Tipo del producto: {resultado['producto']}")
        print(f"Unidad de medición: {resultado['unidad']}")
        print(f"Valor de la medición: {resultado['valor']}")
    else:
        print("⚠️ No se encontraron registros para ese departamento.")
    
    print(f"\n Total registros encontrados: {total}")
    print(f" Tiempo de ejecución: {tiempo:.2f} ms")

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    
    departamento = input("\nIngrese el nombre del departamento a consultar: ").upper()
    anio_inicial = int(input("Ingrese el año inicial del periodo a consultar: "))
    anio_final = int(input("Ingrese el año final del periodo a consultar: "))

    registros, total, total_survey, total_census, tiempo = logic.req_3(control, departamento, anio_inicial, anio_final)

    print("\n• Requerimiento 3 - resultados:")
    print(f"Total registros encontrados: {total}")
    print(f"Registros con fuente SURVEY: {total_survey}")
    print(f"Registros con fuente CENSUS: {total_census}")
    print(f"Tiempo de ejecución: {tiempo:.2f} ms\n")

    if total > 20:
        registros_a_mostrar = registros[:5] + registros[-5:] 
    else:
        registros_a_mostrar = registros

    for r in registros_a_mostrar:
        print(f"\nTipo de fuente/origen: {r[0]}")
        print(f"Año de recopilación: {r[6]}")
        print(f"Fecha de carga: {r[9][:10]}")
        print(f"Frecuencia de la recopilación: {r[7]}")
        print(f"Tipo del producto: {r[1]}")
        print(f"Unidad de medición: {r[3]}")

    if total == 0:
        print("⚠️ No se encontraron registros para el departamento en el rango de años especificado.")


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    tipo_producto = input("\nIngrese el tipo de producto a consultar: ").upper()
    anio_inicial = int(input("Ingrese el año inicial del periodo a consultar: "))
    anio_final = int(input("Ingrese el año final del periodo a consultar: "))
    registros, total, total_survey, total_census, tiempo = logic.req_4(control, tipo_producto, anio_inicial, anio_final)
    print("\n• Requerimiento 4 - resultados:")
    print(f"Total registros encontrados: {total}")
    print(f"Registros con fuente SURVEY: {total_survey}")
    print(f"Registros con fuente CENSUS: {total_census}")
    print(f"Tiempo de ejecución: {tiempo:.2f} ms\n")
    if total > 20:
        registros_a_mostrar = registros[:5] + registros[-5:] 
    else:
        registros_a_mostrar = registros
    for r in registros_a_mostrar:
        print(f"\nTipo de fuente/origen: {r[0]}")
        print(f"Año de recopilación: {r[6]}")
        print(f"Fecha de carga: {r[9][:10]}")
        print(f"Frecuencia de la recopilación: {r[7]}")
        print(f"Tipo del producto: {r[1]}")
        print(f"Unidad de medición: {r[3]}")
    if total == 0:
        print("⚠️ No se encontraron registros para el tipo de producto en el rango de años especificado.")


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    categoria = input("Ingrese la categoría estadística a consultar (por ejemplo: INVENTORY, SALES, etc): ").strip().upper()
    anio_inicio = input("Ingrese el año inicial (YYYY): ").strip()
    anio_final = input("Ingrese el año final (YYYY): ").strip()
    
    resultado= logic.req_5(control, categoria, anio_inicio, anio_final)
    
    print("")
    print("Categoria consultada: "+categoria)
    print("Periodo consultado: "+ anio_inicio + "-" + anio_final)
    print("Tiempo de ejecucion (ms): " + str(resultado["tiempo_ms"]))
    print("Total de registros: " +  str(resultado["total_registros"]))
    print("Total de registros SURVEY: "+ str(resultado["total_survey"]))
    print("Total de registris CENSUS: "+ str(resultado["total_census"]))
    
    if resultado["total_registros"] == 0:
        print("")
        print("No se encontraron registros para el criterio dado.")
    else:
        print("")
        print("Listado de registros:")

        if resultado["total_registros"] > 20:
            print("(Mostrando primeros 5 y últimos 5 registros)")
            print("")
        
        for reg in resultado["registros"]:
            print("Fuente: " + reg['source'] + " Año: " + reg['year'] + " Fecha de carga: " + reg['fecha_carga'])
            print("Frecuencia: " + reg['frecuencia'] + " Departamento: " + reg['departamento'])
            print("Unidad: " + reg['unidad'] + " Producto: " + reg['producto'])
            print("")
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    
    departamento = input("\nIngrese el nombre del departamento a consultar: ").upper()
    fecha_inicio = input("Ingrese la fecha de inicio del periodo a consultar (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin del periodo a consultar (YYYY-MM-DD): ")

    resultado = logic.req_6(control, departamento, fecha_inicio, fecha_fin)

    print("\nResultados de la consulta:")
    print(f"Tiempo de ejecución: {resultado['execution_time']:.2f} ms")
    print(f"Total de registros encontrados: {resultado['total_registros']}")
    print(f"Total de registros con fuente 'SURVEY': {resultado['total_survey']}")
    print(f"Total de registros con fuente 'CENSUS': {resultado['total_census']}")

    print("\nRegistros encontrados:")
    if resultado['total_registros'] > 20:
        registros_mostrados = resultado['registros_mostrados']
        print("(Mostrando primeros 5 y últimos 5 registros)")
    else:
        registros_mostrados = resultado['registros_mostrados']
    
    for registro in registros_mostrados:
        print("-" * 80)
        print(f"Fuente: {registro[0]}")
        print(f"Año de recopilación: {registro[6]}")
        print(f"Fecha de carga: {registro[9][:10]}")
        print(f"Frecuencia: {registro[8]}")
        print(f"Departamento: {registro[5]}")
        print(f"Unidad de medición: {registro[3]}")
        print(f"Producto: {registro[1]}")
        print("-" * 80)


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    departamento = input("Ingrese el nombre del departamento: ").upper()
    anio_inicio = input("Ingrese el año a consultar (YYYY): ")
    anio_fin = input("Ingrese el año final (YYYY): ")
    resultado, total, tiempo = logic.req_7(control, departamento, anio_inicio, anio_fin)
    print("\nRequerimiento 7 - Resultados:")
    print(f"Año consultado: {anio_inicio}")
    print(f"Departamento consultado: {departamento}")
    print(f"Total de registros encontrados: {total}")
    print(f"Tiempo de ejecución: {tiempo:.2f} ms\n")
    if resultado:
        print("Registro con menor valor:")
        print(f"Año de recopilación: {resultado['year']}")
        print(f"Fecha de carga: {resultado['fecha_carga']}")
        print(f"Fuente: {resultado['fuente']}")
        print(f"Frecuencia: {resultado['frecuencia']}")
        print(f"Departamento: {resultado['departamento']}")
        print(f"Producto: {resultado['producto']}")
        print(f"Unidad: {resultado['unidad']}")
        print(f"Valor: {resultado['valor']}")
    else:
        print("⚠️ No se encontraron registros para ese año y departamento.")



def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print("Total de registros:", control["total_reg"])
    print("Total de encuestas:", control["total_sur"])
    print("Total de censos:", control["total_cen"])
    print("Tiempo de ejecución (ms):", control["execution_time"])
    print("\nRegistros:")
    
    for reg in control["registros"]:
        print("Fuente:", reg["source"])
        print("Fecha de carga:", reg["fecha_carga"])
        print("Unidad:", reg["unidad"])
        print("Producto:", reg["producto"])
        print("Departamento:", reg["departamento"])
        print("-" * 40)


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
