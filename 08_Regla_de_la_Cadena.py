# Creamos un escenario cotidiano para explicar la regla de la cadena
# Supongamos que queremos calcular la probabilidad de que un estudiante apruebe un curso basándonos en dos factores: estudiar y asistir a clases.

# Probabilidad de aprobar el curso si el estudiante estudia
prob_aprobar_dado_estudiar = 0.8

# Probabilidad de aprobar el curso si el estudiante no estudia
prob_aprobar_dado_no_estudiar = 0.3

# Probabilidad de estudiar
prob_estudiar = 0.7

# Probabilidad de no estudiar
prob_no_estudiar = 0.3

# Calculamos la probabilidad de aprobar el curso utilizando la regla de la cadena
# P(aprobar) = P(aprobar|estudiar) * P(estudiar) + P(aprobar|no_estudiar) * P(no_estudiar)
prob_aprobar_curso = (prob_aprobar_dado_estudiar * prob_estudiar) + (prob_aprobar_dado_no_estudiar * prob_no_estudiar)

# Imprimimos el resultado
print("La probabilidad de aprobar el curso es:", prob_aprobar_curso)
