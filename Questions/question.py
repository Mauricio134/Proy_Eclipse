import os
import importlib
ruta_directorio = os.path.abspath(os.path.join(os.path.dirname(__file__), "DB"))
archivos_en_directorio = os.listdir(ruta_directorio)
archivos_py = [archivo for archivo in archivos_en_directorio if archivo.endswith(".py")]

modulos_importados = []
for archivo in archivos_py:
    nombre_modulo = os.path.splitext(archivo)[0]
    modulo = importlib.import_module(f"DB.{nombre_modulo}")
    modulos_importados.append(modulo)

class Question:
    def __init__(self,contexto,pregunta,opciones,respuesta,mensaje_i, mensaje_c):
        self.contexto = contexto
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta = respuesta
        self.mensaje_i = mensaje_i
        self.mensaje_c = mensaje_c
cont,preg,opc,res, meni,menc = modulos_importados[1].obtener_pregunta_aleatoria()
Pregunta = Question(cont,preg,opc,res, meni, menc)
print(f"Pregunta: {Pregunta.contexto}")
print(f"Pregunta: {Pregunta.pregunta}")
print(f"Opciones aleatorias: {', '.join(Pregunta.opciones)}")
print(f"Mensaje Error: {', '.join(Pregunta.mensaje_i)}")
print(f"Respuesta Correcta: {Pregunta.respuesta}")
print(f"Mensaje Correcto: {Pregunta.mensaje_c}")