import random

#Puzzle 2
# Lista de seis opciones posibles
opciones_totales_i = ["5 lunares 2 solares", "4 lunares 3 solares", "3 lunares 4 solares", "2 lunares 5 solares", "1 lunar y 6 solares"]
mensajes_error = ["Se nos chispoteo...","Tal vez debamos buscar por otros mares...", "Houston tenemos un problema...", "Es buena la intencion, la respuesta no, pero la intencion está...", "Sabemos que sabes que sabemos ¿verdad?"]
opciones_totales_c = ["7 solares y 3 lunares", "5 lunares y 1 solar", "1 solar y 6 lunares", "8 lunares y 0 solares"]
# Selecciona tres opciones aleatorias como opciones incorrectas
primeros_elementos = [opcion[0] for opcion in opciones_totales_i]
segundos_elementos = [opcion[1] for opcion in opciones_totales_i]

opciones_incorrectas = random.sample(opciones_totales_i, 3)
mensajes_e = random.sample(mensajes_error, 3)
opciones_correctas = random.sample(opciones_totales_c, 1)

# Agrega la respuesta correcta a las opciones incorrectas para tener cuatro opciones en total
opciones_aleatorias = opciones_correctas + opciones_incorrectas

preguntas_respuestas = {
    "Contexto1": {
        "pregunta": "¿Cuál es la capital de la luna?",
        "opciones": ["Londres", "París", "Berlín", "Madrid"],
        "respuesta_correcta": "París",
        "mensaje_i" : "No",
        "mensaje_c": "Correcto"
    },
    "Menos de 2 eclipses no existen por año,\ny tener más de 7 es demasiado raro.\nMínimo 2 eclipses solares encontraremos\ny los demás variarán dependiendo de ello.": {
        "pregunta": "¿Que enunciado es INCORRECTO según la cantidad de eclipses que pueden haber por año?",
        "opciones": opciones_aleatorias,
        "respuesta_correcta": opciones_correctas[0],
        "mensaje_i" : mensajes_e,
        "mensaje_c": "Correcto"
    },
    "Contexto3": {
        "pregunta": "¿Quién escribió 'Romeo y Julieta'?",
        "opciones": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Homer"],
        "respuesta_correcta": "William Shakespeare",
        "mensaje_i" : "No",
        "mensaje_c": "Correcto"
    },
    "Contexto4": {
        "pregunta": "¿Cuántos lados tiene un triángulo?",
        "opciones": ["3", "4", "5", "6"],
        "respuesta_correcta": "3",
        "mensaje_i" : "No",
        "mensaje_c": "Correcto"
    },
    # Agrega más preguntas con opciones y respuesta común aquí
}
def obtener_pregunta_aleatoria():
    contexto, datos = random.choice(list(preguntas_respuestas.items()))
    pregunta = datos["pregunta"]
    opciones = datos["opciones"]
    respuesta_correcta = datos["respuesta_correcta"]
    mensa_i = datos["mensaje_i"]
    mensa_c = datos["mensaje_c"]
    random.shuffle(opciones)  # Mezcla las opciones aleatoriamente
    return contexto,pregunta, opciones, respuesta_correcta, mensa_i, mensa_c