import os
import requests
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la API Key desde las variables de entorno
api_key = os.getenv("CODEGPT_API_KEY")

def generar_seccion_why(topic, product_title, intro_text, cta):
    # URL del endpoint de CodeGPT
    url = "https://api.codegpt.co/api/v1/chat/completions"
    
    # Datos para la solicitud POST
    data = {
        "agentId": "f6cbb8c8-d301-488b-98be-4183b2b8849d",  # Reemplaza con el ID del agente
        "stream": False,
        "format": "json",
        "messages": [
            {
                "content": f"Topic: {topic}\nProduct Title: {product_title}\nIntro Text: {intro_text}\nCTA: {cta}",
                "role": "user"
            }
        ]
    }
    
    # Encabezados para la solicitud
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Realizar la solicitud POST al endpoint de CodeGPT
    response = requests.post(url, json=data, headers=headers)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtener los datos JSON de la respuesta
        result = response.json()
        seccion_why_html = result.get("choices", [{}])[0].get("message", {}).get("completion", "No se pudo generar la sección Why.")
        # Eliminar etiquetas de bloque de código si están presentes
        return seccion_why_html
    else:
        return "No se pudo generar la sección Why."

# Ejemplo de uso
# topic = "Python"
# product_title = "Python AI Assistant by CodeGPT"
# intro_text = "Python AI Assistant by CodeGPT helps you streamline your development process with intelligent code suggestions and optimizations."
# cta = "Try Python AI Assistant Now"
# seccion_why_html = generar_seccion_why(topic, product_title, intro_text, cta)
# print(seccion_why_html)