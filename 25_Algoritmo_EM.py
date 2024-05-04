import sys
sys.path.append(r'C:\users\colibecas\appdata\local\packages\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\localcache\local-packages\python312\site-packages')

import numpy as np

# Supongamos que tenemos datos de dos grupos de personas: una con altura media de 160 cm y otra con altura media de 180 cm
datos = np.concatenate([np.random.normal(160, 10, 100), np.random.normal(180, 10, 100)])

# Inicialización de los parámetros: asumimos que hay dos grupos con medias desconocidas y desviaciones estándar iguales
media_1 = np.random.randint(150, 170)
media_2 = np.random.randint(170, 190)
desviacion_estandar = 10
peso_grupo_1 = 0.5
peso_grupo_2 = 0.5

# Algoritmo EM
for iteracion in range(100):
    # Expectation step: calcular las probabilidades de pertenencia a cada grupo para cada dato
    prob_grupo_1 = peso_grupo_1 * (1 / (np.sqrt(2 * np.pi) * desviacion_estandar)) * np.exp(-0.5 * ((datos - media_1) / desviacion_estandar) ** 2)
    prob_grupo_2 = peso_grupo_2 * (1 / (np.sqrt(2 * np.pi) * desviacion_estandar)) * np.exp(-0.5 * ((datos - media_2) / desviacion_estandar) ** 2)
    suma_probs = prob_grupo_1 + prob_grupo_2
    prob_grupo_1 /= suma_probs
    prob_grupo_2 /= suma_probs
    
    # Maximization step: actualizar los parámetros del modelo
    media_1 = np.sum(prob_grupo_1 * datos) / np.sum(prob_grupo_1)
    media_2 = np.sum(prob_grupo_2 * datos) / np.sum(prob_grupo_2)
    peso_grupo_1 = np.mean(prob_grupo_1)
    peso_grupo_2 = np.mean(prob_grupo_2)
    
    # Calcular la desviación estándar común para ambos grupos
    desviacion_estandar = np.sqrt((np.sum(prob_grupo_1 * (datos - media_1) ** 2) + np.sum(prob_grupo_2 * (datos - media_2) ** 2)) / len(datos))

# Mostrar los resultados
print("Media del grupo 1:", round(media_1, 2))
print("Media del grupo 2:", round(media_2, 2))
print("Desviación estándar común:", round(desviacion_estandar, 2))
print("Peso del grupo 1:", round(peso_grupo_1, 2))
print("Peso del grupo 2:", round(peso_grupo_2, 2))
