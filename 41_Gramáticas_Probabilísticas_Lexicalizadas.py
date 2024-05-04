import random

# Definición de la gramática probabilística lexicalizada
gramatica = {
    "S": [["NP", "VP"], ["NP", "VP", "PP"]],
    "NP": [["Det", "N"], ["Det", "Adj", "N"]],
    "VP": [["V", "NP"], ["V", "Adv"]],
    "PP": [["P", "NP"]],
    "Det": ["el", "un", "algún"],
    "N": ["perro", "gato", "árbol", "coche"],
    "Adj": ["grande", "pequeño", "negro", "blanco"],
    "V": ["corre", "salta", "duerme", "come"],
    "Adv": ["rápidamente", "silenciosamente", "bien"],
    "P": ["en", "sobre", "bajo", "junto a"]
}

# Función para generar una oración recursivamente
def generar_oracion(gramatica, simbolo):
    if simbolo not in gramatica:
        return simbolo  # Si el símbolo es una palabra terminal, lo devuelve tal cual
    else:
        partes = random.choice(gramatica[simbolo])  # Elige una regla para el símbolo no terminal
        return ' '.join(generar_oracion(gramatica, parte) for parte in partes)

# Generar una oración
oracion_generada = generar_oracion(gramatica, "S")
print("Oración generada:", oracion_generada)
