from machine import Pin, ADC
from time import sleep



# Definir los números de los pines
pines = [14, 27, 26, 25, 33, 32]

class Relay():
    
    def __init__(self):
        
        # Inicializar los pines como pines de salida
        self.relays = [Pin(pin, Pin.OUT) for pin in pines]
        
    def setRelay(self, pin):
        self.relays[pin-1].on()
    
    def clearRelay(self, pin):
        self.relays[pin-1].off()
    
    def getValueRelay(self,pin):
        return self.relays[pin-1].value()
    
class LDR_Sensor():
    
    def __init__(self, ldr_pin):
        self.LDR = ADC( Pin(ldr_pin) )
        
    def  getVal(self):
        val = self.LDR.read()
        
    