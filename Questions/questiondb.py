import random
preguntas_respuestas = {
    "Contexto1": {
        "pregunta": "¿Cuál es la capital de la luna?",
        "opciones": ["Londres", "París", "Berlín", "Madrid"],
        "respuesta_correcta": "París"
    },
    "Contexto2": {
        "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["Tierra", "Marte", "Júpiter", "Saturno"],
        "respuesta_correcta": "Júpiter"
    },
    "Contexto3": {
        "pregunta": "¿Quién escribió 'Romeo y Julieta'?",
        "opciones": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Homer"],
        "respuesta_correcta": "William Shakespeare"
    },
    "Contexto4": {
        "pregunta": "¿Cuántos lados tiene un triángulo?",
        "opciones": ["3", "4", "5", "6"],
        "respuesta_correcta": "3"
    },
    # Agrega más preguntas con opciones y respuesta común aquí
}
def obtener_pregunta_aleatoria():
    contexto, datos = random.choice(list(preguntas_respuestas.items()))
    pregunta = datos["pregunta"]
    opciones = datos["opciones"]
    respuesta_correcta = datos["respuesta_correcta"]
    random.shuffle(opciones)  # Mezcla las opciones aleatoriamente
    return contexto,pregunta, opciones, respuesta_correcta