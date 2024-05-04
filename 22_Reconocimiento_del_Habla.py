# Definimos las posibles palabras que el sistema puede reconocer
palabras_posibles = ["hola", "adiós", "gracias"]

# Función para simular el reconocimiento de habla
def reconocimiento_habla(audio_entrada):
    # Convertimos el audio a texto (en este ejemplo, asumimos que ya se ha hecho la conversión)
    texto = audio_entrada.lower()  # Convertimos a minúsculas para facilitar la comparación
    
    # Inicializamos la palabra reconocida como None
    palabra_reconocida = None
    
    # Comparamos el texto de entrada con las palabras posibles
    for palabra in palabras_posibles:
        if palabra in texto:
            palabra_reconocida = palabra
            break
    
    return palabra_reconocida

# Simulamos el reconocimiento de habla con diferentes audios de entrada
audio_1 = "Hola, ¿cómo estás?"
audio_2 = "Gracias por tu ayuda."
audio_3 = "No te preocupes, nos vemos luego."

# Realizamos el reconocimiento de habla para cada audio de entrada
palabra_reconocida_1 = reconocimiento_habla(audio_1)
palabra_reconocida_2 = reconocimiento_habla(audio_2)
palabra_reconocida_3 = reconocimiento_habla(audio_3)

# Mostramos las palabras reconocidas
print("Palabra reconocida en el primer audio:", palabra_reconocida_1)
print("Palabra reconocida en el segundo audio:", palabra_reconocida_2)
print("Palabra reconocida en el tercer audio:", palabra_reconocida_3)
