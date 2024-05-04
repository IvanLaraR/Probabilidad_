# Definir una matriz que representa una imagen en escala de grises
imagen = [
    [100, 120, 110, 90, 80],
    [110, 130, 120, 100, 85],
    [120, 140, 130, 110, 90],
    [130, 150, 140, 120, 95],
    [140, 160, 150, 130, 100]
]

# Función para reconocer objetos en la imagen
def reconocer_objetos(imagen):
    objetos = []
    for fila in imagen:
        for pixel in fila:
            if pixel >= 120:  # Si el píxel es lo suficientemente brillante
                objetos.append('Objeto detectado')  # Agregar objeto a la lista
            else:
                objetos.append('Fondo')  # No hay objeto, es el fondo
    return objetos

# Reconocer objetos en la imagen
objetos_detectados = reconocer_objetos(imagen)

# Imprimir los objetos detectados
print("Resultados del reconocimiento de objetos:")
for fila in objetos_detectados:
    print(fila)
