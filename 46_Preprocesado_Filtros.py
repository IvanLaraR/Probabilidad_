# Definición de una lista de datos
datos = [10, 15, 20, 25, 30, 35, 40]

# Función para aplicar un filtro a los datos
def aplicar_filtro(lista_datos, filtro):
    # Crear una nueva lista para almacenar los datos filtrados
    datos_filtrados = []
    
    # Recorrer la lista de datos y aplicar el filtro
    for dato in lista_datos:
        if filtro(dato):  # Verificar si el dato cumple con el filtro
            datos_filtrados.append(dato)  # Agregar el dato a la lista de datos filtrados
            
    return datos_filtrados

# Definición de un filtro para mantener solo los datos mayores que 20
def filtro_mayor_que_20(dato):
    return dato > 20

# Llamar a la función para aplicar el filtro
datos_filtrados = aplicar_filtro(datos, filtro_mayor_que_20)

# Mostrar los datos originales y los datos filtrados
print("Datos originales:", datos)
print("Datos filtrados (mayores que 20):", datos_filtrados)
