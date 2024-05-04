import random

# Número de caras en el dado
total_caras = 6

# Inicializamos un diccionario para almacenar la distribución de probabilidad
distribucion_probabilidad = {}

# Simulamos el lanzamiento del dado y contamos cuántas veces aparece cada resultado
for resultado in range(1, total_caras + 1):
    # Supongamos que lanzamos el dado 1000 veces para obtener una muestra significativa
    cantidad_resultado = 0
    for _ in range(1000):
        # Simulamos el lanzamiento del dado
        lanzamiento = random.randint(1, total_caras)
        # Contamos cuántas veces aparece el resultado actual
        if lanzamiento == resultado:
            cantidad_resultado += 1
    # Calculamos la probabilidad de obtener el resultado actual
    probabilidad_resultado = cantidad_resultado / 1000
    # Almacenamos la probabilidad en el diccionario de distribución de probabilidad
    distribucion_probabilidad[resultado] = probabilidad_resultado

# Imprimimos la distribución de probabilidad
print("Distribución de probabilidad de lanzar un dado:")
for resultado, probabilidad in distribucion_probabilidad.items():
    print(f"Resultado: {resultado}, Probabilidad: {probabilidad:.2f}")
