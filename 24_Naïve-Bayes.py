# Supongamos que tenemos un conjunto de mensajes de texto, donde cada mensaje se representa como una lista de palabras
# Cada mensaje está etiquetado como spam (1) o no spam (0)
mensajes_texto = [
    (["oferta", "imperdible", "descuento"], 1),  # Spam
    (["hola", "amigo", "te", "envío", "mi", "informe"], 0),  # No spam
    (["ganador", "sorteo", "millonario"], 1),  # Spam
    (["reunión", "importante", "mañana"], 0),  # No spam
    (["última", "oportunidad", "descuento"], 1),  # Spam
]

# Contadores para las palabras en mensajes clasificados como spam y no spam
conteo_palabras_spam = {}
conteo_palabras_no_spam = {}
total_palabras_spam = 0
total_palabras_no_spam = 0

# Recorremos los mensajes de texto para contar las palabras según la clasificación
for mensaje, es_spam in mensajes_texto:
    for palabra in mensaje:
        if es_spam:
            conteo_palabras_spam[palabra] = conteo_palabras_spam.get(palabra, 0) + 1
            total_palabras_spam += 1
        else:
            conteo_palabras_no_spam[palabra] = conteo_palabras_no_spam.get(palabra, 0) + 1
            total_palabras_no_spam += 1

# Calculamos las probabilidades de las palabras dadas las clases (spam y no spam)
probabilidad_palabras_spam = {palabra: conteo / total_palabras_spam for palabra, conteo in conteo_palabras_spam.items()}
probabilidad_palabras_no_spam = {palabra: conteo / total_palabras_no_spam for palabra, conteo in conteo_palabras_no_spam.items()}

# Función para predecir si un nuevo mensaje es spam o no spam
def predecir_spam(mensaje):
    probabilidad_spam = 1.0
    probabilidad_no_spam = 1.0
    
    # Calculamos la probabilidad de que el mensaje sea spam o no spam utilizando el teorema de Bayes
    for palabra in mensaje:
        if palabra in probabilidad_palabras_spam:
            probabilidad_spam *= probabilidad_palabras_spam[palabra]
        if palabra in probabilidad_palabras_no_spam:
            probabilidad_no_spam *= probabilidad_palabras_no_spam[palabra]
    
    # Aplicamos la regla de Bayes para determinar si el mensaje es spam o no spam
    probabilidad_spam *= len(mensajes_texto) / (len(mensajes_texto) + 1)  # Laplace smoothing
    probabilidad_no_spam *= len(mensajes_texto) / (len(mensajes_texto) + 1)  # Laplace smoothing
    
    # Devolvemos la clasificación
    return probabilidad_spam > probabilidad_no_spam

# Ejemplo de clasificación de un nuevo mensaje
nuevo_mensaje = ["última", "oportunidad", "ganador", "descuento"]
es_spam = predecir_spam(nuevo_mensaje)

# Mostramos el resultado
if es_spam:
    print("El nuevo mensaje es clasificado como SPAM.")
else:
    print("El nuevo mensaje es clasificado como NO SPAM.")
