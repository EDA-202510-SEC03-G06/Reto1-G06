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
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


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
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


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
