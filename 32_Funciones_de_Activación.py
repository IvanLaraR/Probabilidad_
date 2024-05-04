import math

# Función de activación sigmoidal
def sigmoid(x):
    """
    Función sigmoidal que transforma una entrada en el rango de 0 a 1.
    """
    return 1 / (1 + math.exp(-x))

# Función de activación ReLU (Rectified Linear Unit)
def relu(x):
    """
    Función ReLU que retorna x si x es mayor que 0, y 0 en caso contrario.
    """
    return max(0, x)

# Función de activación tangente hiperbólica
def tanh(x):
    """
    Función tangente hiperbólica que transforma una entrada en el rango de -1 a 1.
    """
    return math.tanh(x)

# Función de activación softmax
def softmax(x):
    """
    Función softmax que transforma un vector de números en un vector de probabilidades.
    """
    exp_values = [math.exp(i) for i in x]
    total = sum(exp_values)
    return [i / total for i in exp_values]

# Ejemplo de uso de las funciones de activación
entrada = 0.5

# Función sigmoidal
salida_sigmoidal = sigmoid(entrada)
print("Salida con función sigmoidal:", salida_sigmoidal)

# Función ReLU
salida_relu = relu(entrada)
print("Salida con función ReLU:", salida_relu)

# Función tangente hiperbólica
salida_tanh = tanh(entrada)
print("Salida con función tangente hiperbólica:", salida_tanh)

# Función softmax
entradas_softmax = [1.0, 2.0, 3.0]
salida_softmax = softmax(entradas_softmax)
print("Salida con función softmax:", salida_softmax)
