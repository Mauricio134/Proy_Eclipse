import questiondb 

class Question:
    def __init__(self,pregunta,opciones,respuesta):
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta = respuesta
preg,opc,res = questiondb.obtener_pregunta_aleatoria()
Pregunta = Question(preg,opc,res)
print(f"Pregunta: {Pregunta.pregunta}")
print(f"Opciones aleatorias: {', '.join(Pregunta.opciones)}")
print(f"Respuesta Correcta: {Pregunta.respuesta}")