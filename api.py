import json
import requests

def obtener_datos_aves():
    url = 'https://aves.ninjas.cl/api/birds'
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.content.decode('utf-8')  # Decodifica usando UTF-8
        return json.loads(data)  
    except requests.RequestException as e:
        print(f"Error al obtener datos: {e}")
        return []
