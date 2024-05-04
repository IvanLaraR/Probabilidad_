# Supongamos que queremos simular la temperatura promedio diaria en una ciudad durante un año, donde la temperatura promedio no varía significativamente de un día a otro.

import random

# Definimos una función para simular el proceso estacionario de temperatura
def simular_temperatura_promedio_anual():
    # Definimos la temperatura promedio inicial
    temperatura_actual = 25  # Temperatura en grados Celsius
    
    # Simulamos el cambio de temperatura promedio durante un año (365 días)
    for dia in range(1, 366):
        # Generamos un cambio aleatorio en la temperatura promedio diaria
        cambio_temperatura = random.uniform(-1, 1)  # Cambio aleatorio entre -1 y 1 grados Celsius
        temperatura_actual += cambio_temperatura
        
        # Aseguramos que la temperatura no exceda ciertos límites realistas
        temperatura_actual = max(15, min(35, temperatura_actual))
        
        # Imprimimos la temperatura promedio estimada para el día actual
        print(f"Día {dia}: Temperatura promedio = {temperatura_actual:.2f}°C")

# Simulamos el proceso estacionario de temperatura
print("Simulación del proceso estacionario de temperatura durante un año:")
simular_temperatura_promedio_anual()
