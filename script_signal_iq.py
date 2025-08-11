from iqoptionapi.stable_api import IQ_Option
import time
import requests
from datetime import datetime

# ======= CONFIGURACIÓN =======
IQ_EMAIL = "yoelaguilar27.Ya@outlook.com"
IQ_PASSWORD = "Aguilar27"

TELEGRAM_TOKEN = "AAEoEqJg8oGoFPFzKvs0wXpsh-2dCe4fm2Q"
TELEGRAM_CHAT_ID = "562640811"

TIEMPO_VELA = 60  # 1 minuto
PROBABILIDAD_MIN = 98  # porcentaje mínimo para enviar señal

# ======= FUNCIÓN TELEGRAM =======
def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": mensaje}
    requests.post(url, data=data)

# ======= CONEXIÓN IQ OPTION =======
I_want_money = IQ_Option(IQ_EMAIL, IQ_PASSWORD)
I_want_money.connect()

if I_want_money.check_connect():
    print("✅ Conectado a IQ Option")
    enviar_telegram("✅ Bot conectado a IQ Option")
else:
    print("❌ Error de conexión a IQ Option")
    enviar_telegram("❌ Error de conexión a IQ Option")
    exit()

# ======= LISTA DE PARES OTC =======
pares_otc = [
    "EURUSD-OTC", "GBPUSD-OTC", "USDJPY-OTC",
    "AUDUSD-OTC", "EURJPY-OTC", "GBPJPY-OTC",
    "EURGBP-OTC", "NZDUSD-OTC"
]

# ======= CONTROL DE SEÑAL REPETIDA =======
ultima_senal = None  # (par, tendencia)

# ======= BUCLE PRINCIPAL =======
while True:
    mejor_senal = None
    mejor_prob = 0

    for par in pares_otc:
        velas = I_want_money.get_candles(par, TIEMPO_VELA, 10, time.time())

        verdes = sum(1 for v in velas if v['close'] > v['open'])
        rojas = len(velas) - verdes
        probabilidad = (max(verdes, rojas) / len(velas)) * 100

        if velas[-1]['close'] > velas[-1]['open']:
            tendencia = "CALL"
        else:
            tendencia = "PUT"

        if probabilidad > mejor_prob:
            mejor_prob = probabilidad
            mejor_senal = (par, tendencia, probabilidad)

    if mejor_senal and mejor_prob >= PROBABILIDAD_MIN:
        if ultima_senal != (mejor_senal[0], mejor_senal[1]):
            hora_actual = datetime.now().strftime("%H:%M:%S")
            mensaje = (
                f"📊 Señal {mejor_senal[1]}\n"
                f"💱 Par: {mejor_senal[0]}\n"
                f"🕒 Hora: {hora_actual}\n"
                f"📈 Probabilidad: {mejor_senal[2]:.2f}%"
            )
            enviar_telegram(mensaje)
            print(mensaje)
            ultima_senal = (mejor_senal[0], mejor_senal[1])

    time.sleep(TIEMPO_VELA)
