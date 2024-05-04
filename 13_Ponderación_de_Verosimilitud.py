# Supongamos que queremos determinar la probabilidad de que una persona obtenga un resultado positivo en una prueba de detección de una enfermedad, dados los resultados de las pruebas anteriores.

# Definimos una función para calcular la probabilidad de obtener un resultado positivo en la prueba de detección, dado el resultado de las pruebas anteriores
def ponderacion_verosimilitud(resultados_anteriores):
    # Contamos el número de veces que se obtuvo un resultado positivo en las pruebas anteriores
    positivos = resultados_anteriores.count('Positivo')
    
    # Contamos el número total de pruebas anteriores realizadas
    total_pruebas = len(resultados_anteriores)
    
    # Calculamos la probabilidad de obtener un resultado positivo en la próxima prueba basándonos en las pruebas anteriores
    probabilidad_positivo = positivos / total_pruebas
    
    return probabilidad_positivo

# Resultados de las pruebas anteriores
resultados_anteriores = ['Negativo', 'Positivo', 'Negativo', 'Negativo', 'Positivo']

# Calculamos la probabilidad de obtener un resultado positivo en la próxima prueba basándonos en las pruebas anteriores
probabilidad_positivo_proxima_prueba = ponderacion_verosimilitud(resultados_anteriores)

# Imprimimos el resultado
print("La probabilidad de obtener un resultado positivo en la próxima prueba es:", probabilidad_positivo_proxima_prueba)
