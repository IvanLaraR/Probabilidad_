# IvanL - Código para Localización Utilizando el Método de Monte Carlo

# Definición de las variables para la localización
posicion_actual = "Sala de estar"  # Posición inicial del robot
mapa = {
    "Sala de estar": ["Cocina", "Dormitorio", "Baño"],
    "Cocina": ["Sala de estar"],
    "Dormitorio": ["Sala de estar", "Baño"],
    "Baño": ["Sala de estar", "Dormitorio"]
}  # Mapa del entorno

# Función para mover el robot a una nueva posición
def mover_robot(destino):
    global posicion_actual
    if destino in mapa[posicion_actual]:
        posicion_actual = destino
        print("El robot se ha movido a", destino)
    else:
        print("No se puede mover a", destino, "desde", posicion_actual)

# Simulación de la localización del robot
print("El robot está en la", posicion_actual)

# Movimientos del robot basados en instrucciones
mover_robot("Cocina")
mover_robot("Baño")
mover_robot("Sala de estar")
mover_robot("Cocina")
