# Definición del corpus de texto
corpus_texto = """
En un lugar de la Mancha, de cuyo nombre no quiero acordarme,
no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,
adarga antigua, rocín flaco y galgo corredor.
"""

# Función para limpiar el texto y dividirlo en palabras
def limpiar_texto(texto):
    texto = texto.lower()  # Convertir todo a minúsculas
    texto_limpio = ""
    for char in texto:
        if char.isalpha() or char.isspace():  # Conservar solo letras y espacios
            texto_limpio += char
    palabras = texto_limpio.split()  # Dividir el texto en palabras
    return palabras

# Función para calcular las probabilidades de ocurrencia de cada palabra en el corpus
def calcular_probabilidades(palabras):
    frecuencias = {}
    total_palabras = len(palabras)
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    probabilidades = {palabra: frecuencia / total_palabras for palabra, frecuencia in frecuencias.items()}
    return probabilidades

# Función para predecir la siguiente palabra dado un contexto
def predecir_siguiente_palabra(contexto, probabilidades):
    contexto = contexto.lower()
    palabras_contexto = limpiar_texto(contexto)
    max_probabilidad = 0
    palabra_predicha = ""
    for palabra, probabilidad in probabilidades.items():
        if palabras_contexto[-1] == palabra:
            if probabilidad > max_probabilidad:
                max_probabilidad = probabilidad
                palabra_predicha = palabra
    return palabra_predicha

# Limpieza del texto y cálculo de probabilidades
palabras_corpus = limpiar_texto(corpus_texto)
probabilidades_palabras = calcular_probabilidades(palabras_corpus)

# Ejemplo de uso
contexto = "vivía un"
siguiente_palabra = predecir_siguiente_palabra(contexto, probabilidades_palabras)
print("La palabra más probable después de '{}'' es '{}'".format(contexto, siguiente_palabra))
