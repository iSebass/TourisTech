import network
from time import sleep


from umqtt.robust import MQTTClient

class ESP_Connect():
    
    def __init__(self, SSID, PASS):
        self.SSID = SSID
        self.PASS = PASS
        self.sta_if = network.WLAN(network.STA_IF)
        self.sta_if.active(True)
        self._checkwifi()
    
    def _checkwifi(self):
        
        if not self.sta_if.isconnected():
            self.sta_if.connect(self.SSID, self.PASS)
            # Espera a que se establezca la conexión
            while not self.sta_if.isconnected():
                pass
            print('Conexión establecida a la red WiFi')
            print('Dirección IP:', self.sta_if.ifconfig()[0])
        else:
            print("El sistema ya esta conectado a una red wifi")
           
    def connect_ubidots(self, token):
        self.ubidotsToken = token 
        self.DEVICE_LABEL = "TourisTec"
        
    def publish_ubidots(self, typeVar, value, context):
        
        self.client = MQTTClient(self.DEVICE_LABEL,
                                 "industrial.api.ubidots.com",
                                 1883,user = self.ubidotsToken,
                                 password = self.ubidotsToken)
        self.client.connect()
        
        self.msg =  b'{"%s": {"value":%s, "context":"%s"}}' %(typeVar,value, context)
        self.topic = b"/v1.6/devices/{device_label}".format(device_label=self.DEVICE_LABEL)
        self.client.publish(self.topic, self.msg)
        print("msg: ", self.msg)
        print("topic: ", self.topic)
        self.client.disconnect()
        sleep(5)    
        
        