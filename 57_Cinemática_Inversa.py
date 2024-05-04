# IvanL - Código para Cinemática Inversa
import math
# Definición de las variables para el brazo robótico
longitud_brazo1 = 10  # Longitud del primer eslabón del brazo robótico
longitud_brazo2 = 7   # Longitud del segundo eslabón del brazo robótico

# Función para calcular la cinemática inversa y encontrar los ángulos de los eslabones
def calcular_angulos_cinemática_inversa(x, y):
    # Calcula la distancia desde el origen al punto final
    distancia = (x ** 2 + y ** 2) ** 0.5
    
    # Calcula el ángulo entre la hipotenusa y la horizontal
    angulo_theta2 = math.acos((longitud_brazo1 ** 2 + longitud_brazo2 ** 2 - distancia ** 2) / (2 * longitud_brazo1 * longitud_brazo2))
    
    # Calcula el ángulo entre la horizontal y la línea hacia el punto final
    angulo_theta1 = math.atan2(y, x) - math.atan2((longitud_brazo2 * math.sin(angulo_theta2)), (longitud_brazo1 + longitud_brazo2 * math.cos(angulo_theta2)))
    
    # Convierte los ángulos de radianes a grados
    angulo_theta1_grados = math.degrees(angulo_theta1)
    angulo_theta2_grados = math.degrees(angulo_theta2)
    
    return angulo_theta1_grados, angulo_theta2_grados

# Posición deseada del extremo del brazo robótico
posicion_final_x = 8
posicion_final_y = 5

# Calcular los ángulos necesarios para llegar a la posición deseada
angulo1, angulo2 = calcular_angulos_cinemática_inversa(posicion_final_x, posicion_final_y)

# Mostrar los ángulos calculados
print("Ángulo del primer eslabón:", angulo1, "grados")
print("Ángulo del segundo eslabón:", angulo2, "grados")
