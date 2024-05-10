import dht
from machine import Pin

class DHTSensor:
    def __init__(self, pin=16):
        self.pin = Pin(pin, Pin.IN)

    def read_sensor(self):
        try:
            dht_sensor = dht.DHT11(self.pin)  ## dht_sensor = dht.DHT11(machine.Pin(16)) if dont work remove init and checge this line
            dht_sensor.measure()
            temperature = dht_sensor.temperature()
            humidity = dht_sensor.humidity()
            print("collected DHT11")
            return temperature, humidity
        except Exception as e:
            #print('Error reading from DHT sensor:', e)
            return None, None
