import random

# Función para inicializar los pesos de una capa de la red neuronal
def inicializar_pesos_aleatorios(num_entradas):
    return [random.uniform(-1, 1) for _ in range(num_entradas)]

# Función para calcular la salida de una capa de la red neuronal
def calcular_salida_capa(entradas, pesos):
    dot_product = sum(entrada * peso for entrada, peso in zip(entradas, pesos))
    return dot_product

# Función para calcular la salida de la red neuronal
def calcular_salida_red_neuronal(entradas, pesos_capa_oculta, pesos_capa_salida):
    salida_capa_oculta = calcular_salida_capa(entradas, pesos_capa_oculta)
    salida_capa_salida = calcular_salida_capa([salida_capa_oculta], pesos_capa_salida)  # Corrección aquí
    return salida_capa_salida

# Ejemplo de uso
entradas = [0.5, 0.3, 0.2]
pesos_capa_oculta = inicializar_pesos_aleatorios(len(entradas))
pesos_capa_salida = inicializar_pesos_aleatorios(len(entradas))

salida_red_neuronal = calcular_salida_red_neuronal(entradas, pesos_capa_oculta, pesos_capa_salida)
print("Salida de la red neuronal:", salida_red_neuronal)
