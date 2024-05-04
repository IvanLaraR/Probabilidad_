# Supongamos que queremos simular el proceso de lanzar una moneda y determinar la probabilidad de obtener cara o cruz.

import random

# Definimos una función para realizar el muestreo directo
def muestreo_directo():
    # Lanzamos la moneda una vez
    resultado = random.choice(["Cara", "Cruz"])
    return resultado

# Definimos una función para realizar el muestreo por rechazo
def muestreo_por_rechazo():
    while True:
        # Lanzamos la moneda dos veces
        resultado1 = random.choice(["Cara", "Cruz"])
        resultado2 = random.choice(["Cara", "Cruz"])
        
        # Si los resultados son iguales, rechazamos y lanzamos de nuevo
        if resultado1 == resultado2:
            continue
        else:
            # Si los resultados son diferentes, devolvemos uno de los resultados
            return resultado1

# Realizamos el muestreo directo
resultado_directo = muestreo_directo()

# Realizamos el muestreo por rechazo
resultado_rechazo = muestreo_por_rechazo()

# Imprimimos los resultados
print("Resultado del muestreo directo:", resultado_directo)
print("Resultado del muestreo por rechazo:", resultado_rechazo)
