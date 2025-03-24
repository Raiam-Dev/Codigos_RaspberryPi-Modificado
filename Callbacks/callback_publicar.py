from Callbacks import callback_mqtt_connect 
import json

def callback_publicar(topico,msg):
    callback_mqtt_connect.client.publish(topico,json.dumps(msg, indent=4))