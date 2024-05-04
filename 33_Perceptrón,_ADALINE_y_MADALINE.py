# Definición de la función de activación para el perceptrón y el ADALINE
def step_function(x):
    """
    Función de activación escalón que retorna 0 si x es menor que 0, y 1 en caso contrario.
    """
    return 0 if x < 0 else 1

# Definición de la clase Perceptrón
class Perceptron:
    def __init__(self, num_entradas):
        # Inicialización de los pesos y el sesgo
        self.weights = [0] * num_entradas
        self.bias = 0
    
    def predict(self, inputs):
        # Cálculo del valor de activación
        activation = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        # Aplicación de la función de activación
        return step_function(activation)

# Definición de la clase ADALINE
class Adaline:
    def __init__(self, num_entradas):
        # Inicialización de los pesos y el sesgo
        self.weights = [0] * num_entradas
        self.bias = 0
    
    def predict(self, inputs):
        # Cálculo del valor de activación
        activation = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        return activation

# Definición de la clase MADALINE
class Madaline:
    def __init__(self, num_entradas):
        # Inicialización de los pesos y el sesgo
        self.weights = [0] * num_entradas
        self.bias = 0
    
    def predict(self, inputs):
        # Cálculo del valor de activación
        activation = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        # Aplicación de la función de activación
        return step_function(activation)

# Ejemplo de uso de las clases
perceptron = Perceptron(2)
adaline = Adaline(2)
madaline = Madaline(2)

inputs = [1, 0.5]

print("Predicción del Perceptrón:", perceptron.predict(inputs))
print("Predicción del ADALINE:", adaline.predict(inputs))
print("Predicción del MADALINE:", madaline.predict(inputs))
