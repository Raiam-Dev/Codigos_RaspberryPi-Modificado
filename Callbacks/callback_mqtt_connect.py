from librpiplc.folder_rpiplc.models_v6 import hw
import paho.mqtt.client as mqtt
from Broker.config_broker import broker_config
from Callbacks.callback_receber import on_message
import time
import asyncio

lista = list(hw["RPIPLC_58"].keys())
client = mqtt.Client(client_id=broker_config["client_id"])

def on_connect(client, userdata,flags,rc): 
    if rc == 0:
        for item in lista:
            topico = "request/"+item
            client.subscribe(topic=topico)
        print("✅ Conectado ao Broker com Sucesso")
    else:
        print("Erro ao se Conectar")
    
async def start_connectMqtt():
    client.username_pw_set(username=broker_config["user_name"],password=broker_config["password"])
    client.on_connect = on_connect 
    client.on_message = on_message
    client.connect_async(host=broker_config["server"],port= broker_config["port"],keepalive= broker_config["keepalive"],)
    client.loop_start()
    await asyncio.sleep(0.1)