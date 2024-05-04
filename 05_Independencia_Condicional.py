import random

# Definimos las variables para contar los resultados
caras_m1 = 0  # Contador de caras en la primera moneda
caras_m2 = 0  # Contador de caras en la segunda moneda
caras_m1y2 = 0  # Contador de caras en ambas monedas

# Simulamos el lanzamiento de las dos monedas un gran número de veces
num_lanzamientos = 10000
for _ in range(num_lanzamientos):
    # Lanzamos la primera moneda
    resultado_m1 = random.choice(['cara', 'cruz'])
    # Lanzamos la segunda moneda
    resultado_m2 = random.choice(['cara', 'cruz'])
    # Contamos las caras en cada moneda
    if resultado_m1 == 'cara':
        caras_m1 += 1
    if resultado_m2 == 'cara':
        caras_m2 += 1
    # Contamos las caras en ambas monedas
    if resultado_m1 == 'cara' and resultado_m2 == 'cara':
        caras_m1y2 += 1

# Calculamos las probabilidades
prob_cara_m1 = caras_m1 / num_lanzamientos
prob_cara_m2 = caras_m2 / num_lanzamientos
prob_cara_m1y2 = caras_m1y2 / num_lanzamientos

# Verificamos la independencia condicional
independencia_condicional = (prob_cara_m1y2 == prob_cara_m1 * prob_cara_m2)

# Imprimimos los resultados
print("Probabilidad de cara en la primera moneda:", prob_cara_m1)
print("Probabilidad de cara en la segunda moneda:", prob_cara_m2)
print("Probabilidad de cara en ambas monedas:", prob_cara_m1y2)
print("¿Las monedas son independientes condicionalmente?", independencia_condicional)

