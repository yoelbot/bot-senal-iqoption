from iqoptionapi.stable_api import IQ_Option
import time
import requests

# === CONFIGURACIÓN ===
EMAIL = "yoelaguilar27.Ya@outlook.com"
PASSWORD = "Aguilar27"
TOKEN_TELEGRAM = "8250445329:AAEoEqJg8oGoFPFzKvs0wXpsh-2dCe4fm2Q"
ID_CHAT_TELEGRAM = "562640811"

# === CONEXIÓN A IQ OPTION ===
iq = IQ_Option(EMAIL, PASSWORD)
iq.connect()

if iq.check_connect():
    print("✅ Conectado a IQ Option")
else:
    print("❌ Error al conectar a IQ Option")
    exit()

# === FUNCIÓN PARA ENVIAR MENSAJES A TELEGRAM ===
def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
    data = {"chat_id": ID_CHAT_TELEGRAM, "text": mensaje}
    requests.post(url, data=data)

# === LÓGICA DE ANÁLISIS SIMPLIFICADA ===
def detectar_senal():
    activo = "EURUSD"
    timeframe = 1  # 1 minuto
    velas = iq.get_candles(activo, 60, 5, time.time())

    # Contar velas alcistas y bajistas
    verdes = sum(1 for vela in velas if vela["close"] > vela["open"])
    rojas = sum(1 for vela in velas if vela["close"] < vela["open"])

    if verdes >= 4:
        return f"📈 Señal CALL detectada en {activo}"
    elif rojas >= 4:
        return f"📉 Señal PUT detectada en {activo}"
    else:
        return None

# === BUCLE PRINCIPAL ===
while True:
    senal = detectar_senal()
    if senal:
        print(senal)
        enviar_telegram(senal)
    else:
        print("⏳ Sin señal por ahora")

    time.sleep(60)  # Espera 1 minuto antes de volver a analizar
