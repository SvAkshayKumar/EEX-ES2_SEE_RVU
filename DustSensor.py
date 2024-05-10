import machine

class DustSensor:
    def __init__(self, pin=28, led_pin=2):
        self.pin = machine.ADC(pin)
        self.led_pin = machine.Pin(led_pin, machine.Pin.OUT)
        self.led_pin.on()  # Turn on the LED initially

    def voltage_to_dust_density(self, voltage):
        a = 0.17
        b = 0.0084
        dust_density = (voltage - b) / a
        return dust_density

    def read_sensor(self):
        sensor_value = self.pin.read_u16()
        voltage = sensor_value * (5.0 / 65535.0)
        dust_density = self.voltage_to_dust_density(voltage)
        if dust_density:
            print("collected Dust")
            return dust_density
        else:
            return None
