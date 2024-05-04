# Supongamos que queremos predecir el clima para los próximos días basándonos en el clima actual.
# Utilizaremos un modelo de Markov simple donde el clima puede ser soleado, nublado o lluvioso.

# Definimos los estados posibles del clima
soleado = 'Soleado'
nublado = 'Nublado'
lluvioso = 'Lluvioso'

# Definimos las probabilidades de transición entre los estados del clima
probabilidades_transicion = {
    soleado: {soleado: 0.6, nublado: 0.3, lluvioso: 0.1},  # Probabilidades de transición desde un día soleado
    nublado: {soleado: 0.4, nublado: 0.4, lluvioso: 0.2},  # Probabilidades de transición desde un día nublado
    lluvioso: {soleado: 0.2, nublado: 0.3, lluvioso: 0.5}  # Probabilidades de transición desde un día lluvioso
}

# Definimos el clima actual
clima_actual = soleado

# Función para predecir el clima para el siguiente día
def predecir_clima(clima_actual, probabilidades_transicion):
    # Obtenemos las probabilidades de transición para el clima actual
    transiciones_posibles = probabilidades_transicion[clima_actual]
    
    # Generamos una lista de estados posibles basados en las probabilidades de transición
    estados_posibles = [estado for estado in transiciones_posibles for _ in range(int(transiciones_posibles[estado] * 100))]
    
    # Seleccionamos aleatoriamente el siguiente estado del clima
    import random
    clima_siguiente = random.choice(estados_posibles)
    
    return clima_siguiente

# Predecimos el clima para el siguiente día
clima_siguiente = predecir_clima(clima_actual, probabilidades_transicion)

# Imprimimos el resultado
print("El clima para el siguiente día será:", clima_siguiente)

