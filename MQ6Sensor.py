from machine import Pin
import time
import machine

class MQ6Sensor:
    def __init__(self, analog_pin=26):
        self.analog_pin = machine.ADC(analog_pin)
        self.RO_CLEAN_AIR_FACTOR = 3.59
        self.CALIBRATION_SAMPLE_TIMES = 20
        self.CALIBRATION_SAMPLE_INTERVAL = 100
        self.R0_RATIO_BENZENE = 4
        self.led1_pin = Pin(8, Pin.OUT)

    def read_R0(self):
        val = 0.0
        for _ in range(self.CALIBRATION_SAMPLE_TIMES):
            val += self.analog_pin.read_u16()
            time.sleep_ms(self.CALIBRATION_SAMPLE_INTERVAL)
        val /= self.CALIBRATION_SAMPLE_TIMES
        val = val / 65535 * 3.3
        RS_RO = val / self.RO_CLEAN_AIR_FACTOR
        return RS_RO

    def calculate_benzene_concentration(self, RS_RO):
        benzene_concentration = (self.R0_RATIO_BENZENE / RS_RO - 1) / 10
        return benzene_concentration

    def read_sensor(self):
        RS_RO_benzene = self.analog_pin.read_u16() / 65535 * 3.3 / self.read_R0()
        benzene_conc = self.calculate_benzene_concentration(RS_RO_benzene)
        if benzene_conc:
            return benzene_conc
        else:
            return None