from librpiplc import rpiplc as rp
from Callbacks.callback_mqtt_connect import start_connectMqtt
from Sensores.sensor_pressao import leitura_sensor
import time
import asyncio

def main_loop():
    rp.init("RPIPLC_V6","RPIPLC_58")
    asyncio.run(start_connectMqtt())
    while True:
        time.sleep(0.5)

if __name__ == "__main__":
    try: 
       asyncio.run(main_loop())
    except:
        print("Codigo encerrado com Sucesso")
