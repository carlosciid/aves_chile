from template_manager import cargar_plantilla, aplicar_plantilla
from api import obtener_datos_aves

def crear_html():
    aves = obtener_datos_aves()
    if aves:
        template = cargar_plantilla()
        contenido_html = aplicar_plantilla(aves, template)
        with open("output/Aves_de_Chile.html", "w", encoding='utf-8') as archivo:
            archivo.write(contenido_html)
    else:
        print("No se pudo obtener datos de aves.")

if __name__ == "__main__":
    crear_html()
