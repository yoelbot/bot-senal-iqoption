import time
from datetime import datetime
import pytz
import random
import requests

# ================== CONFIGURACIÓN ==================
TOKEN = '8250445329:AAEoEqJg8oGoFPFzKvs0wXpsh-2dCe4fm2Q'
ID_CHAT = '562640811'

PARES_MONEDA = ["EURUSD", "USDJPY", "GBPUSD"]
TEMPORALIDAD = "1 Minuto (M1)"
ZONA_HORARIA = pytz.timezone("America/Lima")  # Hora de Perú

# ================ FUNCIÓN TELEGRAM =================
def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": ID_CHAT,
        "text": mensaje,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Error al enviar mensaje a Telegram: {e}")

# ================ SIMULADOR DE ANÁLISIS ================
def analizar_mercado(par):
    """
    Simula el análisis de velas y retorna probabilidad y dirección
    """
    probabilidad = random.randint(80, 100)
    accion = random.choice(["CALL", "PUT"])
    return probabilidad, accion

# ================ LOOP PRINCIPAL =================
print("⏳ Bot de señales iniciado correctamente...")

while True:
    for par in PARES_MONEDA:
        probabilidad, accion = analizar_mercado(par)

        if probabilidad == 100:
            hora_actual = datetime.now(ZONA_HORARIA).strftime("%H:%M")

            mensaje = f"""🟢 <b>Señal Detectada</b>
Par: <b>{par}</b>
Acción: <b>{accion}</b>
Hora: <b>{hora_actual}</b>
Estrategia: <b>Análisis de Velas</b>
✅ <b>Probabilidad: {probabilidad}%</b>
⏱️ <b>Temporalidad: {TEMPORALIDAD}</b>
"""
            print(f"[{hora_actual}] Señal enviada: {par} - {accion} - {probabilidad}%")
            enviar_telegram(mensaje)
        
        time.sleep(2)  # Breve espera entre pares

    time.sleep(10)  # Espera corta antes de volver a analizar
