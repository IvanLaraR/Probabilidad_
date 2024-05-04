import random
import math

# Función para calcular la distancia euclidiana entre dos vectores
def distancia(vector1, vector2):
    if isinstance(vector1, int):  # Si vector1 es un entero, asumimos que es un índice
        return abs(vector1 - vector2)
    else:
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(vector1, vector2)))

# Función para encontrar la neurona ganadora para un dato de entrada
def neurona_ganadora(entrada, pesos):
    distancias = [distancia(entrada, peso) for peso in pesos]
    return distancias.index(min(distancias))

# Función para actualizar los pesos de las neuronas vecinas a la neurona ganadora
def actualizar_pesos(lr, entrada, ganadora, pesos, radio):
    for i, peso in enumerate(pesos):
        if distancia(ganadora, i) <= radio:
            for j in range(len(peso)):
                peso[j] += lr * (entrada[j] - peso[j])

# Función para entrenar el mapa autoorganizado de Kohonen
def entrenar(entradas, num_neuronas, lr, epochs):
    pesos = [[random.uniform(0, 1) for _ in range(len(entradas[0]))] for _ in range(num_neuronas)]
    
    for _ in range(epochs):
        for entrada in entradas:
            ganadora_idx = neurona_ganadora(entrada, pesos)
            actualizar_pesos(lr, entrada, ganadora_idx, pesos, 1)
    
    return pesos

# Datos de entrada
entradas = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6], [0.7, 0.8], [0.9, 1.0]]

# Entrenamiento del mapa autoorganizado de Kohonen
num_neuronas = 3
lr = 0.1
epochs = 100
pesos_finales = entrenar(entradas, num_neuronas, lr, epochs)

# Imprimir los pesos finales
print("Pesos finales de las neuronas:")
for i, peso in enumerate(pesos_finales):
    print("Neurona", i+1, ":", peso)
