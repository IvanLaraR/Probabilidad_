# IvanL - Código para Etiquetado de Líneas

# Definición de la línea con etiquetas
linea_etiquetada = [
    {"coordenada_x": 10, "coordenada_y": 20, "etiqueta": "Inicio"},
    {"coordenada_x": 50, "coordenada_y": 60, "etiqueta": "Medio"},
    {"coordenada_x": 100, "coordenada_y": 120, "etiqueta": "Fin"}
]

# Función para imprimir las etiquetas de la línea
def imprimir_etiquetas_linea(linea):
    print("Etiquetas de la línea:")
    for punto in linea:
        print(f"Coordenadas ({punto['coordenada_x']}, {punto['coordenada_y']}): {punto['etiqueta']}")

# Llamada a la función para imprimir las etiquetas de la línea
imprimir_etiquetas_linea(linea_etiquetada)
