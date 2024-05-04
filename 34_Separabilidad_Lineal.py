# Definición de la función de separabilidad lineal
def is_linearly_separable(data):
    """
    Comprueba si los datos son linealmente separables.
    Args:
        data (list): Una lista de tuplas, donde cada tupla representa un punto con sus coordenadas (x, y).
    Returns:
        bool: True si los datos son linealmente separables, False en caso contrario.
    """
    # Inicialización de variables para los dos grupos de puntos
    group1 = []
    group2 = []
    
    # Separación de los puntos en dos grupos basados en sus coordenadas y
    for point in data:
        x, y = point
        if y >= x:
            group1.append(point)
        else:
            group2.append(point)
    
    # Si uno de los grupos está vacío, los datos son linealmente separables
    return len(group1) > 0 and len(group2) > 0

# Datos de ejemplo
data = [(1, 2), (2, 3), (3, 2), (4, 5), (5, 4)]

# Comprobación de la separabilidad lineal de los datos
separable = is_linearly_separable(data)

# Imprimir el resultado
if separable:
    print("Los datos son linealmente separables.")
else:
    print("Los datos no son linealmente separables.")
