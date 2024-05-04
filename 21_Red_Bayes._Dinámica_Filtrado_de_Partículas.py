import random

# Definimos la representación del laberinto como una matriz
laberinto = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0]
]

# Definimos la cantidad de partículas (representaciones del robot) que usaremos en el filtrado
num_particulas = 100

# Función para generar partículas aleatorias dentro del laberinto
def generar_particulas():
    particulas = []
    for _ in range(num_particulas):
        fila = random.randint(0, len(laberinto) - 1)
        columna = random.randint(0, len(laberinto[0]) - 1)
        particulas.append((fila, columna))
    return particulas

# Función para mover las partículas basadas en el movimiento del robot
def mover_particulas(particulas):
    nuevas_particulas = []
    for fila, columna in particulas:
        # Simulamos el movimiento del robot permitiendo movimientos arriba, abajo, izquierda y derecha
        direccion = random.choice(['arriba', 'abajo', 'izquierda', 'derecha'])
        if direccion == 'arriba' and fila > 0 and laberinto[fila - 1][columna] == 0:
            nuevas_particulas.append((fila - 1, columna))
        elif direccion == 'abajo' and fila < len(laberinto) - 1 and laberinto[fila + 1][columna] == 0:
            nuevas_particulas.append((fila + 1, columna))
        elif direccion == 'izquierda' and columna > 0 and laberinto[fila][columna - 1] == 0:
            nuevas_particulas.append((fila, columna - 1))
        elif direccion == 'derecha' and columna < len(laberinto[0]) - 1 and laberinto[fila][columna + 1] == 0:
            nuevas_particulas.append((fila, columna + 1))
        else:
            # Si el movimiento no es posible, mantenemos la posición actual
            nuevas_particulas.append((fila, columna))
    return nuevas_particulas

# Simulamos el movimiento del robot y el filtrado de partículas
particulas = generar_particulas()
for _ in range(5):  # Simulamos 5 pasos de tiempo
    print("Estado actual del laberinto:")
    for fila in laberinto:
        print(fila)
    print("Posición estimada del robot (basada en las partículas):", particulas)
    print()
    particulas = mover_particulas(particulas)
