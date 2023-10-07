import questiondb 

class Question:
    def __init__(self,contexto,pregunta,opciones,respuesta):
        self.contexto = contexto
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta = respuesta
cont,preg,opc,res = questiondb.obtener_pregunta_aleatoria()
Pregunta = Question(cont,preg,opc,res)
print(f"Pregunta: {Pregunta.pregunta}")
print(f"Opciones aleatorias: {', '.join(Pregunta.opciones)}")
print(f"Respuesta Correcta: {Pregunta.respuesta}")