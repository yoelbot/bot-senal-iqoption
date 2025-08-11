from iqoptionapi.stable_api import IQ_Option
import time
import datetime
import requests

# ====== CONFIGURACIÓN ======
IQ_EMAIL = "yoelaguilar27.Ya@outlook.com"
IQ_PASSWORD = "Aguilar27"
TOKEN_TELEGRAM = "8250445329:AAEoEqJg8oGoFPFzKvs0wXpsh-2dCe4fm2Q"
CHAT_ID = "562640811"
ACTIVO = "EURUSD-OTC"  # Cambia si quieres otro par
TIEMPO_EXPIRACION = 1  # Minutos
# ===========================

# Conexión a IQ Option
I_want_money = IQ_Option(IQ_EMAIL, IQ_PASSWORD)
I_want_money.connect()

if I_want_money.check_connect():
    print("✅ Conectado correctamente a IQ Option")
else:
    print("❌ Error de conexión a IQ Option")
    exit()

# Función para enviar mensaje a Telegram
def enviar_telegram(mensaje):
    try:
        url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": mensaje}
        requests.post(url, data=data)
    except Exception as e:
        print(f"Error enviando a Telegram: {e}")

# Función de análisis de velas y señales
def analizar_senales():
    velas = I_want_money.get_candles(ACTIVO, 60, 3, time.time())
    ultima = velas[-1]
    penultima = velas[-2]

    if ultima['close'] > ultima['open'] and penultima['close'] < penultima['open']:
        enviar_telegram(f"📈 Señal CALL detectada en {ACTIVO}")
        print(f"{datetime.datetime.now()} - Señal CALL detectada")
    elif ultima['close'] < ultima['open'] and penultima['close'] > penultima['open']:
        enviar_telegram(f"📉 Señal PUT detectada en {ACTIVO}")
        print(f"{datetime.datetime.now()} - Señal PUT detectada")
    else:
        print(f"{datetime.datetime.now()} - Sin señal")

# Bucle infinito para mantener activo el bot
while True:
    try:
        analizar_senales()
        time.sleep(1)  # Revisa cada segundo
    except Exception as e:
        print(f"Error en bucle: {e}")
        time.sleep(5)
