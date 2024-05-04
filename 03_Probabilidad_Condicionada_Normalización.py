# Número total de cartas en la baraja
total_cartas = 52

# Número de cartas rojas en la baraja
cartas_rojas = 26

# Número de diamantes en la baraja
diamantes = 13

# Función para calcular la probabilidad condicionada
def calcular_probabilidad_condicionada(favorable_a, dado_b):
    # La probabilidad condicionada se calcula como la probabilidad de A y B dividida por la probabilidad de B
    probabilidad_condicionada = favorable_a / dado_b
    return probabilidad_condicionada

# Calculamos la probabilidad de sacar un diamante
probabilidad_diamante = diamantes / total_cartas

# Calculamos la probabilidad de sacar una carta roja y un diamante
probabilidad_roja_y_diamante = cartas_rojas / total_cartas

# Calculamos la probabilidad condicionada de sacar una carta roja sabiendo que es un diamante
probabilidad_roja_dado_diamante = calcular_probabilidad_condicionada(probabilidad_roja_y_diamante, probabilidad_diamante)

# Imprimimos el resultado
print(f"Probabilidad de sacar una carta roja sabiendo que es un diamante: {probabilidad_roja_dado_diamante:.2f}")
