# Supongamos que queremos calcular la probabilidad de que un estudiante apruebe un examen basándonos en tres factores: 
# la cantidad de horas de estudio, la calidad del material de estudio y la asistencia a clases.

# Definimos los posibles estados para cada factor
estudio_poco = 'Poco'
estudio_medio = 'Medio'
estudio_mucho = 'Mucho'

material_malo = 'Malo'
material_regular = 'Regular'
material_bueno = 'Bueno'

asistencia_baja = 'Baja'
asistencia_alta = 'Alta'

# Definimos las probabilidades de aprobar el examen según los diferentes estados
probabilidad_aprobacion = {
    (estudio_poco, material_malo, asistencia_baja): 0.1,
    (estudio_poco, material_regular, asistencia_baja): 0.2,
    (estudio_poco, material_bueno, asistencia_baja): 0.3,
    (estudio_poco, material_malo, asistencia_alta): 0.2,
    (estudio_poco, material_regular, asistencia_alta): 0.3,
    (estudio_poco, material_bueno, asistencia_alta): 0.4,
    (estudio_medio, material_malo, asistencia_baja): 0.2,
    (estudio_medio, material_regular, asistencia_baja): 0.3,
    (estudio_medio, material_bueno, asistencia_baja): 0.4,
    (estudio_medio, material_malo, asistencia_alta): 0.3,
    (estudio_medio, material_regular, asistencia_alta): 0.4,
    (estudio_medio, material_bueno, asistencia_alta): 0.5,
    (estudio_mucho, material_malo, asistencia_baja): 0.3,
    (estudio_mucho, material_regular, asistencia_baja): 0.4,
    (estudio_mucho, material_bueno, asistencia_baja): 0.5,
    (estudio_mucho, material_malo, asistencia_alta): 0.4,
    (estudio_mucho, material_regular, asistencia_alta): 0.5,
    (estudio_mucho, material_bueno, asistencia_alta): 0.6
}

# Función para calcular la probabilidad de aprobación del examen eliminando una variable
def calcular_probabilidad_aprobacion_elim_var(estudio, material, asistencia, probabilidad):
    prob_aprobacion_total = 0
    for asist in [asistencia_baja, asistencia_alta]:
        for mat in [material_malo, material_regular, material_bueno]:
            prob_aprobacion_total += probabilidad[(estudio, mat, asist)]
    return prob_aprobacion_total

# Calculamos la probabilidad de aprobación del examen eliminando la variable de asistencia
prob_aprobacion_sin_asistencia = calcular_probabilidad_aprobacion_elim_var(estudio_medio, material_bueno, None, probabilidad_aprobacion)

# Imprimimos el resultado
print("La probabilidad de que el estudiante apruebe el examen estudiando medio tiempo, utilizando material de buena calidad y sin considerar la asistencia es:", prob_aprobacion_sin_asistencia)
