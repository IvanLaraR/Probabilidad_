# Definición de la base de datos de documentos
documentos = {
    "doc1": "El gato come pescado.",
    "doc2": "El perro juega en el parque.",
    "doc3": "El pájaro canta en el árbol.",
    "doc4": "El gato duerme en el sofá."
}

# Función para calcular la similitud entre dos documentos basada en la frecuencia de palabras
def calcular_similitud(documento_query, documento):
    # Tokenizar los documentos en palabras
    palabras_query = documento_query.split()
    palabras_doc = documento.split()
    
    # Calcular la intersección de palabras entre los dos documentos
    palabras_comunes = set(palabras_query) & set(palabras_doc)
    
    # Calcular la similitud como el número de palabras comunes dividido por la longitud del documento de consulta
    similitud = len(palabras_comunes) / len(palabras_query)
    
    return similitud

# Función para recuperar los documentos más relevantes para una consulta dada
def recuperar_documentos(documentos, consulta, num_documentos):
    # Calcular la similitud de la consulta con cada documento
    similitudes = {doc_id: calcular_similitud(consulta, doc) for doc_id, doc in documentos.items()}
    
    # Ordenar los documentos por similitud descendente
    documentos_ordenados = sorted(similitudes.items(), key=lambda x: x[1], reverse=True)
    
    # Seleccionar los documentos más relevantes
    documentos_recuperados = documentos_ordenados[:num_documentos]
    
    return documentos_recuperados

# Consulta del usuario
consulta_usuario = "gato come"

# Recuperar los documentos más relevantes para la consulta del usuario
documentos_recuperados = recuperar_documentos(documentos, consulta_usuario, 2)

# Mostrar los documentos recuperados
print("Documentos más relevantes para la consulta:", consulta_usuario)
for doc_id, similitud in documentos_recuperados:
    print("Documento:", doc_id, "- Similitud:", similitud)
