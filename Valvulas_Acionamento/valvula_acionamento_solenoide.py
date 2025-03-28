from librpiplc import rpiplc as rp
from Callbacks import callback_publicar
from Json_response.json_response import json_acionamento_solenoide

def valvula_solenoide(port, value):
    rp.pin_mode(pin_name=port, mode=rp.OUTPUT)
    rp.digital_write(pin_name=port,value=value)
    json_acionamento_solenoide.update({"port":port,"value":value})
    callback_publicar.callback_publicar("response/"+port,json_acionamento_solenoide)
