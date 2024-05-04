# IvanL - Código de Reconocimiento de Escritura

# Definir una matriz que representa una imagen binaria (0 para fondo, 1 para escritura)
imagen = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

# Función para reconocer caracteres en la imagen
def reconocer_escritura(imagen):
    caracteres = []
    for fila in imagen:
        for pixel in fila:
            if pixel == 1:  # Si el píxel representa escritura
                caracteres.append('\u2588')  # Agregar un bloque Unicode para indicar escritura
            else:
                caracteres.append(' ')  # Agregar espacio para indicar fondo
        caracteres.append('\n')  # Nueva línea al final de cada fila
    return ''.join(caracteres)

# Presentación visual del texto reconocido
print("Reconocimiento de Escritura:")
print("---------------------------")
print(reconocer_escritura(imagen))
