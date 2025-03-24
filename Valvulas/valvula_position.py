from librpiplc import rpiplc as rp
from Callbacks import callback_publicar 

def leitura_valvula_position(client,port):
      
    rp.pin_mode(pin_name=port, mode=rp.INPUT)

    porta = rp.digital_read(port)
      
    valvula_position = {
        "value":None,
        "port":None
    }
    valvula_position.update({"port":port})
    valvula_position.update({"value":porta})
    callback_publicar.callback_publicar("response/"+port,valvula_position)