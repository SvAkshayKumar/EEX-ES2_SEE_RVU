import machine

class NoiseSensor:
    def __init__(self, pin=26):
        self.pin = machine.ADC(pin)
        # Calibration constants for noise sensor
        self.sensor_min = 0        # Minimum raw sensor value
        self.sensor_max = 65535    # Maximum raw sensor value (for a 16-bit ADC)
        self.sound_min_dB = 30    # Minimum sound level in dB (corresponding to self.sensor_min)
        self.sound_max_dB = 120    # Maximum sound level in dB (corresponding to self.sensor_max)
        self.sensor_calibration = 1  # Example calibration factor (adjust according to your sensor)

    def read_sensor(self):
        sensor_value = self.pin.read_u16()
        normalized_value = (sensor_value - self.sensor_min) / (self.sensor_max - self.sensor_min)
        sound_level_dB = (normalized_value * (self.sound_max_dB - self.sound_min_dB)) + self.sound_min_dB
        sound_level_dB = sound_level_dB * self.sensor_calibration
        if sound_level_dB:
            print("collected Noise")
            return f"{sound_level_dB:.2f}"
        else:
            return None
