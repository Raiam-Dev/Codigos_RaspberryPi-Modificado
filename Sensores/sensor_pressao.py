from librpiplc import rpiplc as rp
from Callbacks import callback_publicar 
from Json_response.json_response import json_leitura_sensor 
import json

vref = 10
adcmax = 4096
pressaoMin = 0


def leitura_sensor(client=None,read=None, pressaoMax=None,porta=None,tensao_saida_padrao=None, calibracao=None):
    rp.pin_mode(pin_name=porta, mode=rp.INPUT)
    valor_sensor=rp.analog_read(porta)
    tensao = round((valor_sensor/adcmax)*vref, 2)
    pressao = round((tensao - tensao_saida_padrao)/calibracao, 2)

    json_leitura_sensor.update({"port":porta, "pressao":pressao}) 
    callback_publicar.callback_publicar("response/"+porta,json_leitura_sensor)
