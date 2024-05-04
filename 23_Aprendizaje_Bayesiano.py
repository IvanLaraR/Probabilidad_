# Supongamos que tenemos un conjunto de correos electrónicos, donde cada correo se representa como una lista de palabras
# Cada correo está etiquetado como spam (1) o no spam (0)
correos_electronicos = [
    (["oferta", "imperdible", "descuento"], 1),  # Spam
    (["hola", "amigo", "te", "envío", "mi", "informe"], 0),  # No spam
    (["ganador", "sorteo", "millonario"], 1),  # Spam
    (["reunión", "importante", "mañana"], 0),  # No spam
    (["última", "oportunidad", "descuento"], 1),  # Spam
]

# Contadores para las palabras en correos clasificados como spam y no spam
conteo_palabras_spam = {}
conteo_palabras_no_spam = {}
total_palabras_spam = 0
total_palabras_no_spam = 0

# Recorremos los correos electrónicos para contar las palabras según la clasificación
for correo, es_spam in correos_electronicos:
    for palabra in correo:
        if es_spam:
            conteo_palabras_spam[palabra] = conteo_palabras_spam.get(palabra, 0) + 1
            total_palabras_spam += 1
        else:
            conteo_palabras_no_spam[palabra] = conteo_palabras_no_spam.get(palabra, 0) + 1
            total_palabras_no_spam += 1

# Calculamos las probabilidades de las palabras dadas las clases (spam y no spam)
probabilidad_palabras_spam = {palabra: conteo / total_palabras_spam for palabra, conteo in conteo_palabras_spam.items()}
probabilidad_palabras_no_spam = {palabra: conteo / total_palabras_no_spam for palabra, conteo in conteo_palabras_no_spam.items()}

# Simulamos la clasificación de un nuevo correo electrónico
nuevo_correo = ["oferta", "imperdible", "aprovecha", "descuento"]
probabilidad_spam = 1.0
probabilidad_no_spam = 1.0

# Calculamos la probabilidad de que el nuevo correo sea spam o no spam utilizando el teorema de Bayes
for palabra in nuevo_correo:
    if palabra in probabilidad_palabras_spam:
        probabilidad_spam *= probabilidad_palabras_spam[palabra]
    if palabra in probabilidad_palabras_no_spam:
        probabilidad_no_spam *= probabilidad_palabras_no_spam[palabra]

# Aplicamos la regla de Bayes para determinar si el nuevo correo es spam o no spam
probabilidad_spam *= len(correos_electronicos) / (len(correos_electronicos) + 1)  # Laplace smoothing
probabilidad_no_spam *= len(correos_electronicos) / (len(correos_electronicos) + 1)  # Laplace smoothing

# Mostramos el resultado
if probabilidad_spam > probabilidad_no_spam:
    print("El nuevo correo es clasificado como SPAM.")
else:
    print("El nuevo correo es clasificado como NO SPAM.")
