import time
from datetime import datetime
import pytz
import random
import requests

# == CONFIGURACIÓN DE TELEGRAM ==
TOKEN = "8250445329:AAEoEqJg8oGoFPFzKvs0wXpsh-2dCe4fm2Q"
ID_CHAT = "562640811"

# == ZONA HORARIA DE PERÚ ==
zona_horaria_peru = pytz.timezone("America/Lima")

# == FUNCIÓN PARA ENVIAR MENSAJE A TELEGRAM ==
def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": ID_CHAT,
        "text": mensaje
    }
    requests.post(url, data=data)

# == FUNCIÓN PRINCIPAL DEL BOT ==
def analizar_mercado():
    pares = ["EURUSD", "GBPUSD", "USDJPY"]  # Puedes añadir más pares
    while True:
        for par in pares:
            accion = random.choice(["CALL", "PUT"])
            probabilidad = random.randint(90, 100)  # Simulación de probabilidad

            if probabilidad >= 95:
                hora_actual = datetime.now(zona_horaria_peru).strftime("%H:%M")
                mensaje = f"""🟢 Señal Detectada
Par: {par}
Acción: {accion}
Hora: {hora_actual}
Estrategia: Análisis de Velas
✅ Probabilidad: {probabilidad}%
⏱️ Temporalidad: 1 Minuto (M1)
"""
                enviar_telegram(mensaje)
        time.sleep(30)  # Espera 30 segundos antes de volver a analizar

# == EJECUCIÓN ==
analizar_mercado()
