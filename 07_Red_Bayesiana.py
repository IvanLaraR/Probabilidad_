# Creamos un diccionario que represente la red bayesiana
red_bayesiana = {
    'Pronóstico del clima': {
        'Soleado': 0.7,  # Probabilidad de que el pronóstico sea soleado
        'Lluvioso': 0.3   # Probabilidad de que el pronóstico sea lluvioso
    },
    'Humedad': {
        'Alta|Soleado': 0.1,  # Probabilidad de alta humedad dado que el pronóstico es soleado
        'Normal|Soleado': 0.9, # Probabilidad de humedad normal dado que el pronóstico es soleado
        'Alta|Lluvioso': 0.8,  # Probabilidad de alta humedad dado que el pronóstico es lluvioso
        'Normal|Lluvioso': 0.2 # Probabilidad de humedad normal dado que el pronóstico es lluvioso
    }
}

# Función para calcular la probabilidad de un evento dado una evidencia
def calcular_probabilidad(evidencia, evento, red):
    probabilidad = red[evento][evidencia]
    return probabilidad

# Calculamos la probabilidad de tener humedad alta dado que el pronóstico del clima es lluvioso
prob_humedad_alta = calcular_probabilidad('Alta|Lluvioso', 'Humedad', red_bayesiana)

# Imprimimos el resultado
print("La probabilidad de tener humedad alta dado que el pronóstico del clima es lluvioso es:", prob_humedad_alta)
