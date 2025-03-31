from Sensores.sensor_pressao import leitura_sensor
from Json_response.json_response_erro import json_error_message
from Sensores.sensor_utrassonico import sensor_utrassonico
from Valvulas.valvula_position import leitura_valvula_position
from Sensores.sensor_boia import sensor_boia
from Callbacks import callback_publicar
import json
import asyncio
from Valvulas_Acionamento.valvula_acionamento_solenoide import valvula_solenoide

def on_message(client, userdata, msg):   
    try:
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
        elif json_msg["dispositivo"] == "valvula-position":
            leitura_valvula_position(client=client,port=json_msg["port"])

        elif json_msg["dispositivo"] == "valvula_acionamento_solenoide":
            valvula_solenoide(json_msg["port"], json_msg["value"])

        elif json_msg["dispositivo"] == "sensor_utrassonico":
            asyncio.run(sensor_utrassonico(
                port_serial=json_msg["port_serial"],
                baud_rate=json_msg["baud_rate"],
                timeout=json_msg["timeout"],
                bytesize=json_msg["bytesize"],
                raio_caixa=json_msg["raio_caixa"],
                altura_caixa=json_msg["altura_caixa"]))
            
        elif json_msg["dispositivo"] == "sensor_boia":
            sensor_boia(json_msg["port"])
            
    except Exception as error:
        json_error_message.update({"erro":str(error),"details":"Erro você enviou um json incorreto"})
        callback_publicar.callback_publicar(json_error_message["topico"],json_error_message)
        
    


