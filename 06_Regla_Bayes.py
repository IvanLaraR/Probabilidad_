# Supongamos que queremos calcular la probabilidad de que una persona tenga una enfermedad, 
# dado que ha dado positivo en una prueba.

# Probabilidad de tener la enfermedad
prob_enfermedad = 0.01  # Supongamos que el 1% de la población tiene la enfermedad

# Probabilidad de que la prueba dé positivo si se tiene la enfermedad (sensibilidad)
prob_positivo_dado_enfermedad = 0.95  # La prueba tiene una sensibilidad del 95%

# Probabilidad de que la prueba dé positivo si no se tiene la enfermedad (falsos positivos)
prob_positivo_dado_no_enfermedad = 0.02  # La prueba tiene un 2% de falsos positivos

# Calculamos la probabilidad de dar positivo en la prueba
prob_positivo = (prob_enfermedad * prob_positivo_dado_enfermedad) + ((1 - prob_enfermedad) * prob_positivo_dado_no_enfermedad)

# Aplicamos la Regla de Bayes para calcular la probabilidad de tener la enfermedad dado que la prueba dio positivo
prob_enfermedad_dado_positivo = (prob_enfermedad * prob_positivo_dado_enfermedad) / prob_positivo

# Imprimimos el resultado
print("La probabilidad de tener la enfermedad dado que la prueba dio positivo es:", prob_enfermedad_dado_positivo)
