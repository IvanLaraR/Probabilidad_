# Definir una matriz que representa una imagen en escala de grises
imagen = [
    [100, 120, 110, 90, 80],
    [110, 130, 120, 100, 85],
    [120, 140, 130, 110, 90],
    [130, 150, 140, 120, 95],
    [140, 160, 150, 130, 100]
]

# Definir una función para detectar texturas en una imagen
def detectar_texturas(imagen):
    texturas = []
    for fila in imagen:
        textura_fila = []
        for pixel in fila:
            if pixel < 100:
                textura_fila.append('Áspero')  # Textura áspera
            elif pixel >= 100 and pixel < 130:
                textura_fila.append('Normal')  # Textura normal
            else:
                textura_fila.append('Suave')   # Textura suave
        texturas.append(textura_fila)
    return texturas

# Detectar texturas en la imagen
texturas_imagen = detectar_texturas(imagen)

# Imprimir las texturas detectadas
print("Texturas en la imagen:")
for fila in texturas_imagen:
    print(fila)

# Definir una función para detectar sombras en una imagen
def detectar_sombras(imagen):
    sombras = []
    for fila in imagen:
        sombra_fila = []
        for pixel in fila:
            if pixel < 100:
                sombra_fila.append('Sombreado')  # Sombra
            else:
                sombra_fila.append('No sombreado')  # No sombra
        sombras.append(sombra_fila)
    return sombras

# Detectar sombras en la imagen
sombras_imagen = detectar_sombras(imagen)

# Imprimir las sombras detectadas
print("\nSombras en la imagen:")
for fila in sombras_imagen:
    print(fila)
