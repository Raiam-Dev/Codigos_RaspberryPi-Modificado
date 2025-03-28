from Callbacks import callback_mqtt_connect 
from Json_response.json_response_erro import json_error_message
import json

def callback_publicar(topico,msg):
    try:
        callback_mqtt_connect.client.publish(topico,json.dumps(msg, indent=4))
    except Exception as error:
        json_error_message.update({"erro":str(error),"details":"Falha ao enviar"})
        callback_mqtt_connect.client.publish(json_error_message["topico"],json_error_message)