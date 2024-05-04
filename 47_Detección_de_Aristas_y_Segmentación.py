# Importar la imagen
imagen = [
    [120, 150, 130, 140, 160],
    [130, 145, 135, 155, 145],
    [140, 155, 140, 130, 150],
    [150, 140, 150, 145, 135],
    [160, 135, 155, 140, 130]
]

# Definir una función para calcular el gradiente de una imagen en escala de grises
def calcular_gradiente(imagen):
    alto = len(imagen)
    ancho = len(imagen[0])
    gradiente = []
    for i in range(alto - 1):
        fila_gradiente = []
        for j in range(ancho - 1):
            gx = abs(imagen[i][j+1] - imagen[i][j])  # Gradiente en dirección x
            gy = abs(imagen[i+1][j] - imagen[i][j])  # Gradiente en dirección y
            gradiente_punto = gx + gy  # Magnitud del gradiente en el punto
            fila_gradiente.append(gradiente_punto)
        gradiente.append(fila_gradiente)
    return gradiente

# Calcular el gradiente de la imagen
gradiente_imagen = calcular_gradiente(imagen)

# Imprimir el gradiente
print("Gradiente de la imagen:")
for fila in gradiente_imagen:
    print(fila)
