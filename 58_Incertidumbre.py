# IvanL - Código para Manejo de Incertidumbre en Robótica
import random
# Definimos las variables para la posición actual del robot y su incertidumbre
posicion_x = 10   # Posición en el eje x del robot
posicion_y = 5    # Posición en el eje y del robot
incertidumbre_x = 0.2  # Incertidumbre en la posición en el eje x
incertidumbre_y = 0.3  # Incertidumbre en la posición en el eje y

# Función para actualizar la posición del robot con la incertidumbre
def actualizar_posicion_con_incertidumbre(x, y, incertidumbre_x, incertidumbre_y):
    nueva_posicion_x = x + incertidumbre_x * random.uniform(-1, 1)  # Actualiza la posición en el eje x con incertidumbre
    nueva_posicion_y = y + incertidumbre_y * random.uniform(-1, 1)  # Actualiza la posición en el eje y con incertidumbre
    return nueva_posicion_x, nueva_posicion_y

# Simulamos la actualización de la posición del robot con incertidumbre
nueva_posicion_x, nueva_posicion_y = actualizar_posicion_con_incertidumbre(posicion_x, posicion_y, incertidumbre_x, incertidumbre_y)

# Mostramos la nueva posición del robot con incertidumbre
print("La nueva posición del robot con incertidumbre es:", nueva_posicion_x, ",", nueva_posicion_y)
