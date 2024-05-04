# Supongamos que queremos calcular la probabilidad de que un estudiante apruebe un examen basándonos en dos factores: 
# la cantidad de horas de estudio y la calidad del material de estudio.

# Definimos los posibles estados para la cantidad de horas de estudio y la calidad del material de estudio
estudio_bajo = 'Bajo'
estudio_medio = 'Medio'
estudio_alto = 'Alto'

material_malo = 'Malo'
material_regular = 'Regular'
material_bueno = 'Bueno'

# Definimos las probabilidades de aprobar el examen según los diferentes estados
probabilidad_aprobacion = {
    (estudio_bajo, material_malo): 0.1,
    (estudio_bajo, material_regular): 0.3,
    (estudio_bajo, material_bueno): 0.5,
    (estudio_medio, material_malo): 0.3,
    (estudio_medio, material_regular): 0.5,
    (estudio_medio, material_bueno): 0.7,
    (estudio_alto, material_malo): 0.5,
    (estudio_alto, material_regular): 0.7,
    (estudio_alto, material_bueno): 0.9
}

# Función para calcular la probabilidad de aprobación del examen dado los estados de estudio y material
def calcular_probabilidad_aprobacion(estudio, material, probabilidad):
    return probabilidad[(estudio, material)]

# Probabilidad de que el estudiante estudie medio tiempo y utilice material de calidad regular
probabilidad_aprobacion_medio_regular = calcular_probabilidad_aprobacion(estudio_medio, material_regular, probabilidad_aprobacion)

# Imprimimos el resultado
print("La probabilidad de que el estudiante apruebe el examen estudiando medio tiempo y utilizando material de calidad regular es:", probabilidad_aprobacion_medio_regular)
