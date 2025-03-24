from librpiplc import rpiplc as rp
from Callbacks.callback_mqtt_connect import start_connectMqtt
from Sensores.sensor_pressao import leitura_sensor
import time
import asyncio

async def main_loop():
    rp.init("RPIPLC_V6","RPIPLC_58")
    await start_connectMqtt()
    while True:
        time.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main_loop())
    except:
        print("Codigo encerrado com Sucesso")
