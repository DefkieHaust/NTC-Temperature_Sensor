from machine import ADC
import math
import utime

# Analog sensor
adc = ADC(0)

# Resistance of the ntc sensor
R1 = 10_000

# steinhart-hart coeficients for thermistor
a = 0.001129148 
b = 0.000234125 
c = 0.0000000876741  

# Calculate the voltage from adc_value 
def get_voltage(adc16): 
  voltage = adc16 * (3.3 / 65536)  
  return voltage

# Calculate the resistance of the thermistor 
def get_resistance(voltage, ntc_resistance):
  resistance = (3.3 * ntc_resistance) / voltage 
  return resistance  

# Use the Steinhart-Hart equation to calculate temperature 
def get_temperature(a, b, c, resistance):   
  temperature = (    
    1 / (a + b * math.log(resistance) + c * math.log(resistance) ** 3)    
  ) - 273.15    
  return temperature   

while True:    
  readings = adc.read_u16()  
  volt = get_voltage(readings)  
  resistance = get_resistance(volt, R1) 
  temp = get_temperature(a, b, c, resistance)   
  print("Temperature: " + str(temp) + " C") 
  utime.sleep(0)
