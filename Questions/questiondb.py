import random
preguntas_respuestas = {
    "¿Cuál es la capital de la luna?": {
        "opciones": ["Londres", "París", "Berlín", "Madrid"],
        "respuesta_correcta": "París"
    },
    "¿Cuál es el planeta más grande del sistema solar?": {
        "opciones": ["Tierra", "Marte", "Júpiter", "Saturno"],
        "respuesta_correcta": "Júpiter"
    },
    "¿Quién escribió 'Romeo y Julieta'?": {
        "opciones": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Homer"],
        "respuesta_correcta": "William Shakespeare"
    },
    "¿Cuántos lados tiene un triángulo?": {
        "opciones": ["3", "4", "5", "6"],
        "respuesta_correcta": "3"
    },
    # Agrega más preguntas con opciones y respuesta común aquí
}
def obtener_pregunta_aleatoria():
    pregunta, datos = random.choice(list(preguntas_respuestas.items()))
    opciones = datos["opciones"]
    respuesta_correcta = datos["respuesta_correcta"]
    random.shuffle(opciones)  # Mezcla las opciones aleatoriamente
    return pregunta, opciones, respuesta_correcta