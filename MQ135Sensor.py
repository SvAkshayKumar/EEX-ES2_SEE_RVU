import machine
import time

class MQ135Sensor:
    def __init__(self, pin=27):
        self.analog_pin = machine.ADC(pin)
        self.RO_CLEAN_AIR_FACTOR = 3.59
        self.CALIBRATION_SAMPLE_TIMES = 20
        self.CALIBRATION_SAMPLE_INTERVAL = 100  # milliseconds
        self.R0_RATIO_CO2 = 60
        self.R0_RATIO_CO = 4.5
        self.R0_RATIO_NH4 = 3.5
    def read_R0(self):
        val = 0.0
        for _ in range(self.CALIBRATION_SAMPLE_TIMES):
            val += self.analog_pin.read_u16()
            time.sleep_ms(self.CALIBRATION_SAMPLE_INTERVAL)
        val /= self.CALIBRATION_SAMPLE_TIMES
        val = val / 65535 * 3.3  # Convert to voltage

        self.RS_RO = val / self.RO_CLEAN_AIR_FACTOR
        self.R0_CO2=self.R0_RATIO_CO2 *self.RS_RO
        self.R0_CO=self.R0_RATIO_CO *self.RS_RO
        self.R0_NH4=self.R0_RATIO_NH4*self.RS_RO

    def Mq135_concentration(self , RS_RO , R0_RATIO):
        # Calculate benzene concentration based on the sensor ratio
        benzene_concentration = (R0_RATIO / RS_RO - 1) / 10
        return benzene_concentration
    
    def read_sensor(self):
        self.read_R0()
        RS_RO_CO2 = self.analog_pin.read_u16() / 65535 * 3.3 / self.R0_CO2
        RS_RO_CO = self.analog_pin.read_u16() / 65535 * 3.3 / self.R0_CO
        RS_RO_NH4 = self.analog_pin.read_u16() / 65535 * 3.3 / self.R0_NH4
        Concentration_CO2 = self.Mq135_concentration(RS_RO_CO2,self.R0_RATIO_CO2)
        Concentration_CO = self.Mq135_concentration(RS_RO_CO,self.R0_RATIO_CO)
        Concentration_NH4 = self.Mq135_concentration(RS_RO_NH4,self.R0_RATIO_NH4)
        A=[Concentration_CO2,Concentration_CO,Concentration_NH4]
        if A:
            return A[0],A[1],A[2]
        else:
            return None,None,None
