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
def createQuestion():
    modulos_importados[1].obtener_pregunta_aleatoria()

createQuestion()