# Supongamos que queremos simular el comportamiento de un jugador que se mueve entre diferentes casillas en un juego de mesa, donde las probabilidades de moverse de una casilla a otra están determinadas por reglas predefinidas.

import random

# Definimos las casillas del juego de mesa como estados de la cadena de Markov
casilla_1 = 'Inicio'
casilla_2 = 'Casilla 2'
casilla_3 = 'Casilla 3'
casilla_4 = 'Casilla 4'
casilla_meta = 'Meta'

# Definimos las probabilidades de transición entre las casillas (estados)
probabilidades_transicion = {
    casilla_1: {casilla_2: 0.3, casilla_3: 0.5, casilla_4: 0.2},
    casilla_2: {casilla_3: 0.4, casilla_4: 0.6},
    casilla_3: {casilla_meta: 1.0},
    casilla_4: {casilla_2: 0.5, casilla_3: 0.2, casilla_meta: 0.3},
    casilla_meta: {}  # La casilla meta es un estado absorbente
}

# Función para simular el movimiento del jugador usando Monte Carlo
def simular_movimiento_jugador(probabilidades_transicion):
    # Comenzamos en la casilla inicial
    casilla_actual = casilla_1
    
    # Simulamos el movimiento hasta llegar a la casilla meta
    while casilla_actual != casilla_meta:
        # Elegimos aleatoriamente la próxima casilla basándonos en las probabilidades de transición
        casillas_siguientes = list(probabilidades_transicion[casilla_actual].keys())
        probabilidades = list(probabilidades_transicion[casilla_actual].values())
        casilla_actual = random.choices(casillas_siguientes, weights=probabilidades)[0]
        
        # Imprimimos el movimiento del jugador
        print("El jugador se mueve a la casilla:", casilla_actual)

# Simulamos el movimiento del jugador usando Monte Carlo
print("Simulación del movimiento del jugador:")
simular_movimiento_jugador(probabilidades_transicion)
