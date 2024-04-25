from string import Template
import os

def cargar_plantilla():
    path = "templates/plantilla.html"
    contenido_default = """
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Aves de Chile</title>
    <meta charset="UTF-8">
    <meta name="author" content="Carlos Cid Acevedo">
    <meta name="description" content="Lista de aves observables en Chile con nombres en español e inglés y sus respectivas imágenes.">
    <meta name="keywords" content="aves, Chile, ornitología, turismo, naturaleza, biodiversidad">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<h1>Aves observables en Chile</h1>
<ul>
$content
</ul>
</body>
</html>
    """
    # Verifica si el archivo existe
    if not os.path.exists(path):
        # Si no existe, crea el directorio si es necesario y escribe el contenido predeterminado
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding='utf-8') as file:
            file.write(contenido_default)

    
    with open(path, "r", encoding='utf-8') as file:
        return Template(file.read())

def aplicar_plantilla(aves, template):
    elementos_lista = ""
    for ave in aves:
        elementos_lista += f'<li>{ave["name"]["spanish"]} ({ave["name"]["english"]})<br><img src="{ave["images"]["main"]}" alt="{ave["name"]["spanish"]}"></li>\n'
    return template.substitute(content=elementos_lista)
