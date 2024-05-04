# Variables para contar las canicas de cada color
canicas_rojas = 15
canicas_azules = 10
canicas_verdes = 5
canicas_amarillas = 20

# Calculamos el total de canicas en la bolsa
total_canicas = canicas_rojas + canicas_azules + canicas_verdes + canicas_amarillas

# Función para calcular la probabilidad de sacar una canica de un color específico
def calcular_probabilidad(cantidad_color, total):
    # La probabilidad se calcula como la relación entre el número de canicas de un color y el total de canicas
    probabilidad = cantidad_color / total
    # Convertimos la probabilidad a porcentaje para que sea más fácil de entender
    probabilidad_porcentaje = probabilidad * 100
    return probabilidad_porcentaje

# Calculamos la probabilidad para cada color
probabilidad_rojas = calcular_probabilidad(canicas_rojas, total_canicas)
probabilidad_azules = calcular_probabilidad(canicas_azules, total_canicas)
probabilidad_verdes = calcular_probabilidad(canicas_verdes, total_canicas)
probabilidad_amarillas = calcular_probabilidad(canicas_amarillas, total_canicas)

# Imprimimos los resultados
print(f"Probabilidad de sacar una canica roja: {probabilidad_rojas:.2f}%")
print(f"Probabilidad de sacar una canica azul: {probabilidad_azules:.2f}%")
print(f"Probabilidad de sacar una canica verde: {probabilidad_verdes:.2f}%")
print(f"Probabilidad de sacar una canica amarilla: {probabilidad_amarillas:.2f}%")
