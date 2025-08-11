from iqoptionapi.stable_api import IQ_Option
import time
import logging
import requests
from datetime import datetime

# --- CONFIGURACIÓN ---
IQ_EMAIL = "yoelaguilar27.Ya@outlook.com"
IQ_PASSWORD = "Aguilar27"
TELEGRAM_TOKEN = "8250445329:AAEoEqJg8oGoFPFzKvs0wXpsh-2dCe4fm2Q"
TELEGRAM_CHAT_ID = "562640811"
PAR = "EURUSD-OTC"
TIMEFRAME = 1  # Minutos
PROBABILIDAD_MINIMA = 100  # %
# ----------------------

logging.basicConfig(level=logging.ERROR)

API = IQ_Option(IQ_EMAIL, IQ_PASSWORD)
API.connect()
while not API.check_connect():
    print("🔄 Conectando a IQ Option...")
    time.sleep(1)
print("✅ Conectado a IQ Option")

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": mensaje}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"⚠️ Error enviando mensaje: {e}")

def detectar_senal_cierre():
    velas = API.get_candles(PAR, 60, 2, time.time())
    ultima_vela = velas[-2]
    if ultima_vela['close'] > ultima_vela['open']:
        return "CALL"
    elif ultima_vela['close'] < ultima_vela['open']:
        return "PUT"
    else:
        return None

ultima_hora_analizada = None

while True:
    try:
        ahora = datetime.now()
        hora_actual = ahora.strftime("%H:%M")
        segundos_restantes = 60 - ahora.second  # Cuenta regresiva hasta la próxima vela
        
        if hora_actual != ultima_hora_analizada and segundos_restantes == 60:
            senal = detectar_senal_cierre()
            if senal:
                mensaje = (
                    f"📊 Señal detectada\n"
                    f"⏰ Hora: {hora_actual}\n"
                    f"💱 Par: {PAR}\n"
                    f"📈 Tipo: {senal}\n"
                    f"🎯 Probabilidad: {PROBABILIDAD_MINIMA}%\n"
                    f"⏳ Próxima vela en {segundos_restantes} segundos\n"
                    f"⚡ Entrada inmediata al cierre de vela"
                )
                enviar_telegram(mensaje)
                print(mensaje)
            ultima_hora_analizada = hora_actual

        time.sleep(1)

    except Exception as e:
        print(f"⚠️ Error en el bucle: {e}")
        time.sleep(2)
