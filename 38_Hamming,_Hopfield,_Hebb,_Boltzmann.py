import random
import math

# Función de activación: Función escalón (Step function)
def funcion_activacion(x):
    return 1 if x >= 0 else 0

# Red Neuronal de Hamming
class RedHamming:
    def __init__(self, num_entradas):
        self.num_entradas = num_entradas
        self.pesos = [random.choice([-1, 1]) for _ in range(num_entradas)]

    def calcular_salida(self, entrada):
        suma = sum(w * x for w, x in zip(self.pesos, entrada))
        return funcion_activacion(suma)

# Red Neuronal de Hopfield
class RedHopfield:
    def __init__(self, num_neuronas):
        self.num_neuronas = num_neuronas
        self.pesos = [[0] * num_neuronas for _ in range(num_neuronas)]

    def entrenar(self, patrones):
        for i in range(self.num_neuronas):
            for j in range(self.num_neuronas):
                if i == j:
                    continue
                self.pesos[i][j] = sum(patrones[k][i] * patrones[k][j] for k in range(len(patrones)))

    def calcular_salida(self, entrada):
        salida = entrada[:]
        while True:
            nueva_salida = [funcion_activacion(sum(s * w for s, w in zip(salida, fila))) for fila in self.pesos]
            if nueva_salida == salida:
                break
            salida = nueva_salida
        return salida

# Regla de Hebb
class ReglaHebb:
    def __init__(self, num_entradas):
        self.num_entradas = num_entradas
        self.pesos = [0] * num_entradas

    def aprender(self, entrada):
        for i in range(self.num_entradas):
            self.pesos[i] += entrada[i] * entrada[i]

    def calcular_salida(self, entrada):
        salida = [funcion_activacion(entrada[i] * self.pesos[i]) for i in range(self.num_entradas)]
        return salida

# Red Neuronal de Boltzmann
class RedBoltzmann:
    def __init__(self, num_neuronas):
        self.num_neuronas = num_neuronas
        self.pesos = [[0] * num_neuronas for _ in range(num_neuronas)]

    def entrenar(self, patrones):
        for i in range(self.num_neuronas):
            for j in range(self.num_neuronas):
                if i == j:
                    continue
                self.pesos[i][j] = sum(patrones[k][i] * patrones[k][j] for k in range(len(patrones)))

    def energia(self, entrada):
        suma = sum(entrada[i] * entrada[j] * self.pesos[i][j] for i in range(self.num_neuronas) for j in range(self.num_neuronas))
        return -0.5 * suma

    def probabilidad(self, entrada, temperatura):
        return math.exp(-self.energia(entrada) / temperatura)

    def calcular_salida(self, entrada, temperatura=1.0):
        salida = entrada[:]
        for _ in range(10):
            idx = random.randint(0, self.num_neuronas - 1)
            p_activacion = self.probabilidad(salida, temperatura)
            nueva_salida = salida[:]
            nueva_salida[idx] = 1 - nueva_salida[idx]
            p_nueva_activacion = self.probabilidad(nueva_salida, temperatura)
            if random.random() < p_nueva_activacion / p_activacion:
                salida = nueva_salida
        return salida

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de entrada
    patrones = [
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 1, 1]
    ]
    nueva_entrada = [1, 0, 1, 0]

    # Red Neuronal de Hamming
    red_hamming = RedHamming(len(patrones[0]))
    for patron in patrones:
        print("Salida de Hamming para", patron, ":", red_hamming.calcular_salida(patron))

    # Red Neuronal de Hopfield
    red_hopfield = RedHopfield(len(patrones[0]))
    red_hopfield.entrenar(patrones)
    print("Salida de Hopfield para", nueva_entrada, ":", red_hopfield.calcular_salida(nueva_entrada))

    # Regla de Hebb
    regla_hebb = ReglaHebb(len(patrones[0]))
    for patron in patrones:
        regla_hebb.aprender(patron)
    print("Salida de Hebb para", nueva_entrada, ":", regla_hebb.calcular_salida(nueva_entrada))

    # Red Neuronal de Boltzmann
    red_boltzmann = RedBoltzmann(len(patrones[0]))
    red_boltzmann.entrenar(patrones)
    print("Salida de Boltzmann para", nueva_entrada, ":", red_boltzmann.calcular_salida(nueva_entrada))
