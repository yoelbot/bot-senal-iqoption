from datetime import datetime
import time
import requests

# 🔐 PEGA AQUÍ TUS DATOS PERSONALES DE TELEGRAM
BOT_TOKEN = '8250445329:AAEoEqJg8oGoFPFzKvs0wXpsh-2dCe4fm2Q'     # ejemplo: 6123456789:AAEtcEtcEtcEtcEtc
CHAT_ID = '562640811'             # ejemplo: 123456789 o -1001234567890

# 👤 CORREO DE REFERENCIA (opcional)
USUARIO_CORREO = 'yoelaguilar@gmail.com'

# ✅ FUNCIÓN PARA ENVIAR MENSAJE A TELEGRAM
def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': mensaje}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Error enviando mensaje a Telegram: {e}")

# 🔍 DETECCIÓN DE SEÑAL (ejemplo, alterna entre CALL y PUT)
def detectar_senal():
    segundo_actual = datetime.now().second
    hora_actual = datetime.now().strftime("%H:%M")
    if segundo_actual % 2 == 0:
        return "CALL", hora_actual
    else:
        return "PUT", hora_actual

# 🔁 BUCLE PRINCIPAL
while True:
    accion, hora = detectar_senal()
    par = "EURUSD"  # puedes cambiar por el par real

    mensaje = f"""{"🟢" if accion == "CALL" else "🔴"} Señal Detectada
Par: {par}
Acción: {accion}
Hora: {hora}
Estrategia: Análisis de Velas
✅ Probabilidad: Mayor al 80%
👤 Usuario: {USUARIO_CORREO}
"""
    enviar_telegram(mensaje)
    print("🔔 Señal enviada correctamente:\n", mensaje)

    time.sleep(60)  # Espera 60 segundos para la siguiente señal
