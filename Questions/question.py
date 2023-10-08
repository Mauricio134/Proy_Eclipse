import questiondb2

class Question:
    def __init__(self,contexto,pregunta,opciones,respuesta,mensaje_i, mensaje_c):
        self.contexto = contexto
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta = respuesta
        self.mensaje_i = mensaje_i
        self.mensaje_c = mensaje_c
cont,preg,opc,res, meni,menc = questiondb2.obtener_pregunta_aleatoria()
Pregunta = Question(cont,preg,opc,res, meni, menc)
print(f"Pregunta: {Pregunta.contexto}")
print(f"Pregunta: {Pregunta.pregunta}")
print(f"Opciones aleatorias: {', '.join(Pregunta.opciones)}")
print(f"Mensaje Error: {', '.join(Pregunta.mensaje_i)}")
print(f"Respuesta Correcta: {Pregunta.respuesta}")
print(f"Mensaje Correcto: {Pregunta.mensaje_c}")