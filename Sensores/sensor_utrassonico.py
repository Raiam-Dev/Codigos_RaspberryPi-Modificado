import serial
import asyncio
from Json_response.json_response_erro import json_error_message
from Json_response.json_response import json_sensor_utrassonico
from Callbacks.callback_publicar import callback_publicar

def calcular_volume(metro,raio_caixa, altura_caixa, valor_sensor, port_serial):
    altura_restante = max(0, altura_caixa - valor_sensor)  
    volume = 3.1416 * (raio_caixa ** 2) * altura_restante * 1000  
    json_sensor_utrassonico.update({"litros":volume,"port_serial":port_serial, "altura_caixa":metro})
    callback_publicar("response"+port_serial, json_sensor_utrassonico)

async def sensor_utrassonico(port_serial,baud_rate,timeout, bytesize,raio_caixa,altura_caixa):
    ser = serial.Serial(port=port_serial, baudrate=baud_rate, timeout=timeout, parity=serial.PARITY_NONE, bytesize=bytesize)
    await asyncio.sleep(0.5)  
    try:
        if ser.in_waiting > 0:
            data = ser.read(4)  
                
            if len(data) == 4:
                if data[0] == 0xFF:
                    checksum = (data[0] + data[1] + data[2]) & 0x00FF
                        
                    if checksum == data[3]:
                        distancia = (data[1] << 8) + data[2]
                            
                        if distancia > 0:
                            metro = (distancia / 10)/100  
                            calcular_volume(metro,raio_caixa=raio_caixa, altura_caixa=altura_caixa, valor_sensor=metro, port_serial=port_serial)
                        else:
                            json_error_message.update({"erro":"erro distancia nao detectada", "details":"A distancia foi menor que 0"})
                    else:
                        pass
                else:
                    pass
            else:
                pass
    except Exception as error:
        json_error_message.update({"erro":str(error), "details":"A distancia foi menor que 0"})