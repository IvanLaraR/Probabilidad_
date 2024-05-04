
import math
# Redes Neuronales: Retropropagación del Error

# Definición de la función de activación (sigmoid)
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Definición de la derivada de la función de activación (sigmoid)
def sigmoid_derivada(x):
    return x * (1 - x)

# Inicialización de los pesos de la capa oculta y de salida
pesos_oculta = [[0.1, 0.2], [0.3, 0.4]]
pesos_salida = [0.5, 0.6]

# Datos de entrada y salida esperada
inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
targets = [0, 1, 1, 0]

# Entrenamiento de la red neuronal
for epoch in range(1000):
    for input_data, target in zip(inputs, targets):
        # Forward pass
        hidden_input = [sum(input_data[i] * pesos_oculta[j][i] for i in range(len(input_data))) for j in range(len(pesos_oculta))]
        hidden_output = [sigmoid(x) for x in hidden_input]
        output = sum(hidden_output[j] * pesos_salida[j] for j in range(len(hidden_output)))
        
        # Cálculo del error
        error = target - output
        
        # Backpropagation
        delta_salida = error * sigmoid_derivada(output)
        delta_oculta = [delta_salida * pesos_salida[j] * sigmoid_derivada(hidden_output[j]) for j in range(len(hidden_output))]
        
        # Actualización de pesos
        for j in range(len(pesos_salida)):
            pesos_salida[j] += delta_salida * hidden_output[j]
        for j in range(len(pesos_oculta)):
            for i in range(len(input_data)):
                pesos_oculta[j][i] += delta_oculta[j] * input_data[i]

# Imprimir los pesos actualizados
print("Pesos de la capa oculta después del entrenamiento:", pesos_oculta)
print("Pesos de la capa de salida después del entrenamiento:", pesos_salida)
