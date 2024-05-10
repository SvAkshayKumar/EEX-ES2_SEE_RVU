from DHTSensor import DHTSensor
from DustSensor import DustSensor
from MQ135Sensor import MQ135Sensor
from MQ6Sensor import MQ6Sensor
from NoiseSensor import NoiseSensor
from machine import Pin

class DataFetching:
    def __init__(self):
        self.dust_sensor = DustSensor()
        self.mq135_sensor = MQ135Sensor()
        self.mq6_sensor = MQ6Sensor()
        self.noise_sensor = NoiseSensor()
        self.dht_sensor = DHTSensor()
    def read_all(self):
        try:
            dht_temp_data, dht_humidity_data = self.dht_sensor.read_sensor()
            dust_sensor_data = self.dust_sensor.read_sensor()
            mq135_CO2_data, mq135_CO_data, mq135_NH4_data = self.mq135_sensor.read_sensor()
            mq6_benzene_data = self.mq6_sensor.read_sensor()
            noise_data = self.noise_sensor.read_sensor()
            data = {
                        'dht_temp_data': dht_temp_data,
                        'dht_humidity_data': dht_humidity_data,
                        'dust_sensor': dust_sensor_data,
                        'mq135_CO2_data': mq135_CO2_data,
                        'mq135_CO_data': mq135_CO_data,
                        'mq135_NH4_data': mq135_NH4_data,
                        'mq6_benzene_data': mq6_benzene_data,
                        'noise_data': noise_data
                }
            if data:
                print("Success datafetchig")
            return data
        except Exception as e:
            print("An error occurred during data fetching:", e)
            return None
