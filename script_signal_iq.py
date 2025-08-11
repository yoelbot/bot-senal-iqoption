from iqoptionapi.stable_api import IQ_Option
import time
import datetime
import requests

# ===== CONFIGURACIÓN =====
IQ_EMAIL = "yoelaguilar27.Ya@outlook.com"
IQ_PASSWORD = "Aguilar27"
TELEGRAM_TOKEN = "8250445329:AAEoEqJg8oGoFPFzKvs0wXpsh-2dCe4fm2Q"
TELEGRAM_CHAT_ID = "562640811"
PAR = "EURUSD"  # Par que quieres analizar
TIEMPO_EXPIRACION = 1  # minutos
UMBRAL_PROBABILIDAD = 1.0  # 1.0 = 100%

# ===== FUNCIÓN PARA ENVIAR MENSAJES A TELEGRAM =====
def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": mensaje})

# ===== CONEXIÓN A IQ OPTION =====
I_want_money = IQ_Option(IQ_EMAIL, IQ_PASSWORD)
I_want_money.connect()

if I_want_money.check_connect():
    print("✅ Conectado a IQ Option")
else:
    print("❌ Error al conectar")
    exit()

# ===== LOOP PRINCIPAL =====
while True:
    ahora = datetime.datetime.now()
    if ahora.second == 59:  # Espera al cierre de vela
        velas = I_want_money.get_candles(PAR, 60, 3, time.time())
        
        # Ejemplo de cálculo ficticio de probabilidad
        probabilidad = 1.0 if velas[-1]['close'] > velas[-1]['open'] else 0.0
        
        if probabilidad >= UMBRAL_PROBABILIDAD:
            hora_str = ahora.strftime("%H:%M:%S")
            tipo = "CALL" if velas[-1]['close'] > velas[-1]['open'] else "PUT"
            mensaje = f"📊 Señal {tipo} | {PAR} | {hora_str} | Prob: {probabilidad*100:.0f}%"
            enviar_telegram(mensaje)
            print(mensaje)
        time.sleep(2)
    time.sleep(0.5)
