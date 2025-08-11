import time
import requests
from iqoptionapi.stable_api import IQ_Option
from datetime import datetime

# ---------------- CONFIGURACIÓN ----------------
IQ_USER = "yoelaguilar27.ya@outlook.com"
IQ_PASS = "Aguilar27"
TELEGRAM_TOKEN = "8250445329:AAEoEqJg8oGoFPFzKvs0wXpsh-2dCe4fm2Q"
TELEGRAM_CHAT_ID = "562640811"
PAR = "EURUSD"  # Par a analizar
TEMPORALIDAD = 1  # en minutos
PROBABILIDAD_OBJETIVO = 100  # %
# -------------------------------------------------

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": mensaje}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Error enviando mensaje a Telegram:", e)

def conectar_iq():
    iq = IQ_Option(IQ_USER, IQ_PASS)
    iq.connect()
    if iq.check_connect():
        print("✅ Conectado a IQ Option")
        return iq
    else:
        print("❌ No se pudo conectar a IQ Option")
        exit()

def analizar_vela(iq):
    velas = iq.get_candles(PAR, TEMPORALIDAD * 60, 10, time.time())
    subidas = sum(1 for v in velas if v['close'] > v['open'])
    bajadas = sum(1 for v in velas if v['close'] < v['open'])

    total = subidas + bajadas
    if total == 0:
        return None

    prob_subida = (subidas / total) * 100
    prob_bajada = (bajadas / total) * 100

    if prob_subida == PROBABILIDAD_OBJETIVO:
        return ("CALL", prob_subida)
    elif prob_bajada == PROBABILIDAD_OBJETIVO:
        return ("PUT", prob_bajada)
    else:
        return None

def main():
    iq = conectar_iq()
    while True:
        señal = analizar_vela(iq)
        if señal:
            tipo, prob = señal
            hora = datetime.now().strftime("%H:%M:%S")
            mensaje = f"📢 Señal detectada {tipo} | {PAR} | Probabilidad: {prob}% | Hora: {datetime.now().strftime('%H:%M:%S')}"
