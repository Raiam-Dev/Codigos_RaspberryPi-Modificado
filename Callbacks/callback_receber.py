from librpiplc import rpiplc as rp
from Sensores.sensor_pressao import leitura_sensor
from Valvulas.valvula_position import leitura_valvula_position
import json

def on_message(client, userdata, msg):
    json_msg = json.loads(msg.payload.decode())    
     
    if json_msg["dispositivo"] == "sensor-pressao":
        leitura_sensor(
            client=client,
            read=json_msg["read"],
            pressaoMax=json_msg["pressaoMax"],
            porta=json_msg["porta"],
            tensao_saida_padrao=json_msg["tensao_saida_padrao"],
            calibracao=json_msg["calibracao"]
        )
    if json_msg["dispositivo"] == "valvula-position":
        leitura_valvula_position(client=client,port=json_msg["port"])
        
    


