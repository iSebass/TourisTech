from BME680 import *
from machine import I2C, Pin
import time
from time import sleep
from ProjectTurist import *



bus_i2c = I2C(0)
bus_i2c = I2C(1, scl=Pin(22), sda=Pin(21), freq=100000)


def run():
    
    #sensor bme
    bme = BME680_I2C(i2c=bus_i2c)
    
    #setup
    relay = Relay()
    ldr_A = LDR()
    while True:
        
        for i in range(6):
            relay.setRelay(i+1)
            sleep(0.5)
            relay.clearRelay(i+1)
            sleep(0.5)
        
        temperature = bme.temperature
        humidity    = bme.humidity
        pressure    = bme.pressure
        gas         = bme.gas
        
        statusRelay1 = relay.getValueRelay(0)
        statusRelay2 = relay.getValueRelay(1)
        statusRelay3 = relay.getValueRelay(2)
        statusRelay4 = relay.getValueRelay(3)
        statusRelay5 = relay.getValueRelay(4)
        statusRelay6 = relay.getValueRelay(5)
        
        print("Relay State")
        print("Status Relay1: ",statusRelay1)
        print("Status Relay2: ",statusRelay2)
        print("Status Relay3: ",statusRelay3)
        print("Status Relay4: ",statusRelay4)
        print("Status Relay5: ",statusRelay5)
        print("Status Relay6: ",statusRelay6)
        print("")
        print("BME MEASUREMENT")
        print("Tem: ",temperature)
        print("Humidity: ",humidity)
        print("Pressure: ",pressure)
        print("Gas: ",gas)
        print("")
        
        sleep(1)

if __name__=="__main__":
    run()
    