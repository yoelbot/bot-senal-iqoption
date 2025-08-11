from iqoptionapi.stable_api import IQ_Option
import time, logging, os

logging.basicConfig(level=logging.ERROR)

email = os.getenv("yoelaguilar27.Ya@outlook.com")
password = os.getenv("Aguilar27")

I_want_money = IQ_Option(email, password)

def conectar():
    while True:
        print("🔌 Conectando a IQ Option...")
        check, reason = I_want_money.connect()
        if check:
            print("✅ Conectado con éxito")
            break
        else:
            print(f"❌ Error de conexión: {reason}. Reintentando...")
            time.sleep(5)

conectar()

while True:
    try:
        velas = I_want_money.get_candles("EURUSD-OTC", 60, 1, time.time())
        print("📊 Última vela:", velas[-1])
        time.sleep(1)
    except Exception as e:
        print("⚠️ Error, intentando reconectar:", e)
        conectar()
