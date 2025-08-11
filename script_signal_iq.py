from iqoptionapi.stable_api import IQ_Option
import time
import logging
import requests

# --- CONFIGURACIÓN ---
IQ_EMAIL = "yoelaguilar27.Ya@outlook.com"
IQ_PASSWORD = "Aguilar27"
TELEGRAM_TOKEN = "8250445329:AAEoEqJg8oGoFPFzKvs0wXpsh-2dCe4fm2Q"
TELEGRAM_CHAT_ID = "562640811"
PAR = "EURUSD-OTC"
TIMEFRAME = 1  # Minutos
PROBABILIDAD_MINIMA = 100  # %
# ----------------------

# Desactivar mensajes de log de iqoptionapi
logging.basicConfig(level=logging.ERROR)

# Conexión a IQ Option
API = IQ_Option(IQ_EMAIL, IQ_PASSWORD)
API.connect()
while not API.check_connect():
    print("🔄 Conectando a IQ Option...")
    time.sleep(1)
print("✅ Conectado a IQ Option")

# Función para enviar mensaje a Telegram
def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": mensaje}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"⚠️ Error enviando mensaje: {e}")

# Simulación de detección de señal (debes poner tu lógica real)
def detectar_senal():
    # Ejemplo simple: obtiene velas y genera señal alea
