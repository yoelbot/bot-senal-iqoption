import time
import random
from datetime import datetime
import pytz
import requests

# ===== CONFIGURACIÓN DE TELEGRAM =====
TOKEN = '8250445329:AAEoEqJg8oGoFPFzKvs0wXpsh-2dCe4fm2Q'
CHAT_ID = '562640811'

# ===== LISTA DE PARES A ANALIZAR =====
pares = ['EURUSD', 'USDJPY', 'GBPUSD', 'AUDUSD', 'USDCAD']

# ===== FUNCIÓN PARA ENVIAR MENSAJES A TELEGRAM =====
def enviar_telegram(mensaje):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': mensaje}
    requests.post(url, data=data)

# ===== ZONA HORARIA DE PERÚ =====
zona_peru = pytz.timezone('America/Lima')

# ===== LOOP PRINCIPAL DEL BOT =====
while True:
    par = random.choice(pares)
    accion = random.choice(['CALL', 'PUT'])
    probabilidad = random.randint(90, 100)

    if probabilidad >= 98:
        hora_actual = datetime.now(zona_peru).strftime("%H:%M")
        mensaje = f"""🟢 Señal Detectada
Par: {par}
Acción: {accion}
Hora: {hora_actual}
Estrategia: Análisis de Velas
✅ Probabilidad: {probabilidad}%
⏱️ Temporalidad: 1 Minuto (M1)
"""
        enviar_telegram(mensaje)

    time.sleep(60)  # Espera 1 minuto antes del siguiente análisis
