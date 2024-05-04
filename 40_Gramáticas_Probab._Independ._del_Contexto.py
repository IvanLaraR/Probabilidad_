import random

# Definición de la gramática probabilística
gramatica = {
    "S": [("NP", "VP")],
    "NP": [("Det", "N"), ("Det", "N", "PP")],
    "VP": [("V", "NP"), ("V", "NP", "PP")],
    "PP": [("P", "NP")],
    "Det": ["el", "la", "los", "las", "un", "una", "unos", "unas"],
    "N": ["perro", "gato", "casa", "árbol", "auto", "niño", "niña"],
    "V": ["corre", "salta", "camina", "come", "bebe"],
    "P": ["en", "sobre", "bajo", "junto a", "cerca de"]
}

# Función para generar una oración aleatoria
def generar_oracion(gramatica, simbolo_inicial):
    if simbolo_inicial not in gramatica:
        return simbolo_inicial
    reglas = random.choice(gramatica[simbolo_inicial])
    oracion_generada = ""
    for simbolo in reglas:
        oracion_generada += generar_oracion(gramatica, simbolo) + " "
    return oracion_generada.strip()

# Generar una oración aleatoria utilizando la gramática
oracion_generada = generar_oracion(gramatica, "S")
print("Oración generada:", oracion_generada)
