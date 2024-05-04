# Total de caras del dado
total_caras = 6

# Números pares en el dado (2, 4, 6)
numeros_pares = 3

# Función para calcular la probabilidad a priori de un evento
def calcular_probabilidad_a_priori(cantidad_favorable, total_posible):
    # La probabilidad se calcula como la proporción de resultados favorables sobre el total de posibles resultados
    probabilidad = cantidad_favorable / total_posible
    # Convertimos la probabilidad a porcentaje para facilitar su comprensión
    probabilidad_porcentaje = probabilidad * 100
    return probabilidad_porcentaje

# Calculamos la probabilidad de obtener un número par al lanzar un dado
probabilidad_numeros_pares = calcular_probabilidad_a_priori(numeros_pares, total_caras)

# Imprimimos el resultado
print(f"Probabilidad de sacar un número par al lanzar un dado: {probabilidad_numeros_pares:.2f}%")
