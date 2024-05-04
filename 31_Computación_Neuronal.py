# Función de activación sigmoidal
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivada de la función de activación sigmoidal
def sigmoid_derivada(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Clase para la red neuronal
class RedNeuronal:
    def __init__(self, num_entradas, num_ocultas, num_salidas):
        self.num_entradas = num_entradas
        self.num_ocultas = num_ocultas
        self.num_salidas = num_salidas

        # Inicialización de los pesos
        self.pesos_entrada_oculta = [[random.uniform(-1, 1) for _ in range(num_entradas + 1)] for _ in range(num_ocultas)]
        self.pesos_oculta_salida = [[random.uniform(-1, 1) for _ in range(num_ocultas + 1)] for _ in range(num_salidas)]

    # Método para realizar una predicción
    def predecir(self, entrada):
        # Calcular la salida de la capa oculta
        salida_oculta = [0] * self.num_ocultas
        for j in range(self.num_ocultas):
            suma_ponderada = sum(entrada[i] * self.pesos_entrada_oculta[j][i] for i in range(self.num_entradas))
            suma_ponderada += self.pesos_entrada_oculta[j][-1]  # Bias
            salida_oculta[j] = sigmoid(suma_ponderada)

        # Calcular la salida final
        salida_final = [0] * self.num_salidas
        for k in range(self.num_salidas):
            suma_ponderada = sum(salida_oculta[j] * self.pesos_oculta_salida[k][j] for j in range(self.num_ocultas))
            suma_ponderada += self.pesos_oculta_salida[k][-1]  # Bias
            salida_final[k] = sigmoid(suma_ponderada)

        return salida_final

    # Método para entrenar la red neuronal utilizando backpropagation
    def entrenar(self, entradas, salidas, tasa_aprendizaje, epocas):
        for _ in range(epocas):
            for entrada, salida in zip(entradas, salidas):
                # Paso forward
                salida_oculta = [0] * self.num_ocultas
                for j in range(self.num_ocultas):
                    suma_ponderada = sum(entrada[i] * self.pesos_entrada_oculta[j][i] for i in range(self.num_entradas))
                    suma_ponderada += self.pesos_entrada_oculta[j][-1]  # Bias
                    salida_oculta[j] = sigmoid(suma_ponderada)

                salida_final = [0] * self.num_salidas
                for k in range(self.num_salidas):
                    suma_ponderada = sum(salida_oculta[j] * self.pesos_oculta_salida[k][j] for j in range(self.num_ocultas))
                    suma_ponderada += self.pesos_oculta_salida[k][-1]  # Bias
                    salida_final[k] = sigmoid(suma_ponderada)

                # Paso backward
                errores_salida = [0] * self.num_salidas
                for k in range(self.num_salidas):
                    errores_salida[k] = (salida[k] - salida_final[k]) * sigmoid_derivada(salida_final[k])

                errores_oculta = [0] * self.num_ocultas
                for j in range(self.num_ocultas):
                    errores_oculta[j] = sum(errores_salida[k] * self.pesos_oculta_salida[k][j] for k in range(self.num_salidas)) * sigmoid_derivada(salida_oculta[j])

                # Actualizar pesos
                for j in range(self.num_ocultas):
                    for i in range(self.num_entradas):
                        self.pesos_entrada_oculta[j][i] += tasa_aprendizaje * errores_oculta[j] * entrada[i]
                    self.pesos_entrada_oculta[j][-1] += tasa_aprendizaje * errores_oculta[j]  # Bias

                for k in range(self.num_salidas):
                    for j in range(self.num_ocultas):
                        self.pesos_oculta_salida[k][j] += tasa_aprendizaje * errores_salida[k] * salida_oculta[j]
                    self.pesos_oculta_salida[k][-1] += tasa_aprendizaje * errores_salida[k]  # Bias

# Ejemplo de uso
import random
import math

# Datos de entrada y salida para la compuerta lógica XOR
entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
salidas = [[0], [1], [1], [0]]

# Creación de la red neuronal
red_neuronal = RedNeuronal(num_entradas=2, num_ocultas=2, num_salidas=1)

# Entrenamiento de la red neuronal
red_neuronal.entrenar(entradas, salidas, tasa_aprendizaje=0.1, epocas=10000)

# Prueba de la red neuronal entrenada
print("Predicciones después del entrenamiento:")
for entrada in entradas:
    print(entrada, red_neuronal.predecir(entrada))
