from datetime import datetime
import time
import requests
import pytz
import random  # Para simular una probabilidad aleatoria

# 🔐 CONFIGURACIÓN TELEGRAM
BOT_TOKEN = '8250445329:AAEoEqJg8oGoFPFzKvs0wXpsh-2dCe4fm2Q'
CHAT_ID = '562640811'

# 🕒 ZONA HORARIA PERÚ
zona_peru = pytz.timezone('America/Lima')

# ✅ ENVIAR MENSAJE A TELEGRAM
def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': mensaje}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"❌ Error enviando mensaje a Telegram: {e}")

# 🔍 DETECCIÓN DE SEÑAL + PROBABILIDAD
def detectar_senal():
    segundo_actual = datetime.now().second
    hora_actual = datetime.now(zona_peru).strftime("%H:%M")

    # Simula la señal (alternancia simple)
    accion = "CALL" if segundo_actual % 2 == 0 else "PUT"

    # Simula una probabilidad aleatoria entre 80 y 100%
    probabilidad = random.randint(80, 100)

    return accion, hora_actual, probabilidad

# 🔁 BUCLE PRINCIPAL
while True:
    accion, hora, probabilidad = detectar_senal()
    par = "EURUSD"

    if probabilidad >= 95:
        mensaje = f"""{"🟢" if accion == "CALL" else "🔴"} Señal Detectada
Par: {par}
Acción: {accion}
Hora: {hora}
Estrategia: Análisis de Velas
✅ Probabilidad: {probabilidad}%
"""
        enviar_telegram(mensaje)
        print("📤 Señal enviada:\n", mensaje)
    else:
        print(f"⏳ Señal ignorada (solo {probabilidad}%)")

    time.sleep(60)
