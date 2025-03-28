from librpiplc import rpiplc as rp
from Json_response.json_response import json_sensor_boia
from Callbacks.callback_publicar import callback_publicar

def sensor_boia(port):
    rp.pin_mode(port,rp.INPUT)
    valor_boia = rp.digital_read(port)
    json_sensor_boia.update({"port":port,"value":valor_boia})
    callback_publicar("response/"+port,json_sensor_boia)