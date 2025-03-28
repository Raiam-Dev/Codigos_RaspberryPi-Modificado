from librpiplc import rpiplc as rp
from Callbacks import callback_publicar 
from Json_response.json_response import json_valvula_position

def leitura_valvula_position(client,port):
    rp.pin_mode(pin_name=port, mode=rp.INPUT)
    porta = rp.digital_read(port)
    json_valvula_position.update({"port":port,"value":porta})
    callback_publicar.callback_publicar("response/"+port,json_valvula_position)