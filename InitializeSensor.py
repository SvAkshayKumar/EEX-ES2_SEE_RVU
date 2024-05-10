from machine import Pin
import time
class InitializeSensor:
    def __init__(self):
        self.dht_vcc_pin = Pin(21, Pin.OUT)  # DHT11 VCC pin connected to pin 21
        self.dust_vcc_pin = Pin(3, Pin.OUT)  # Dust sensor pin connected to pin 3
        self.mq135_vcc_pin = Pin(17, Pin.OUT)  # MQ135 pin connected to pin 17
        self.ldr_vcc_pin = Pin(19, Pin.OUT)  # LDR pin connected to pin 19
        self.noise_vcc_pin = Pin(21, Pin.OUT)  # Noise sensor pin connected to pin 21
        self.led_pin = Pin(22, Pin.OUT)  # Dust sensor pin connected to pin 3
        self.led1_pin = Pin(8, Pin.OUT)  # MQ135 pin connected to pin 17
    def power_on(self):
        self.ldr_vcc_pin.value(1)
        self.dust_vcc_pin.value(1)
        self.dht_vcc_pin.value(1)
        self.mq135_vcc_pin.value(1)
        self.noise_vcc_pin.value(1)
        self.dust_vcc_pin.value(1)
        self.led_pin.value(0)
        self.led1_pin.value(0)
    def power_off(self):
        self.ldr_vcc_pin.value(0)
        self.dust_vcc_pin.value(0)
        self.dht_vcc_pin.value(0)
        self.mq135_vcc_pin.value(0)
        self.noise_vcc_pin.value(0)
        self.dust_vcc_pin.value(0)
        self.led_pin.value(0)
        self.led1_pin.value(0)