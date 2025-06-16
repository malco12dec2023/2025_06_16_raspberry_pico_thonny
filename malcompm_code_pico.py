# malcompm_code_pico.py
/*
Directions:
  DO NOT COPY THE CODE.
  Do NOT copy the code, type each code or
  edit each changes to better understand
  the logic of operation.
*/

#######################################################
#Code 000 Start: (resistor, LED, breadboard, wires)
from machine import Pin
import time

# Onboard LED on most Pico boards
led = Pin(25, Pin.OUT)  
led.value(1)
#Code 000 End.
#######################################################

#######################################################
#Code 001 Start: save as malcompm_code_001.py
from machine import Pin
import time

led = Pin(“LED”, Pin.OUT)
led.value(1)
#Code 001 End.
#######################################################

#######################################################
#Code 002 Start:
from machine import Pin
import time

led = Pin(“LED”, Pin.OUT)

led.value(0)
time.sleep(1)
led.value(1)
time.sleep(1)
#Code 002 End.
#######################################################

#######################################################
#Code 003 Start:
from machine import Pin
import time

led = Pin(“LED”, Pin.OUT)

led.off()
time.sleep(1)
led.on()
time.sleep(1)
#Code 003 End.
#######################################################

#######################################################
#Code 004 Start:
from machine import Pin
import time

led = Pin(“LED”, Pin.OUT)

# first blink
led.off()
time.sleep(1)
led.on()
time.sleep(1)

# second blink
led.off()
time.sleep(1)
led.on()
time.sleep(1)

# third blink
led.off()
time.sleep(1)
led.on()
time.sleep(1)
#Code 004 End.
#######################################################

#######################################################
#Code 005 Start: use while loop to blink infinitely
from machine import Pin
import time

led = Pin(“LED”, Pin.OUT)

# unlimited blink
while True:
  led.off()
  time.sleep(1)
  led.on()
  time.sleep(1)

#Code 005 End.
#######################################################

#######################################################
#Code 006 Start: use for loop to blink 10 times with 500ms interval
from machine import Pin
import time

led = Pin(“LED”, Pin.OUT)

# blink ten times
for i in range(10):
  led.off()          # Turn LED off
  time.sleep(0.5)    # Wait 500 milliseconds
  led.on()           # Turn LED on
  time.sleep(0.5)    # Wait 500 milliseconds
#Code 006 End.
#######################################################

#######################################################
#Code 007 Start: use led.toggle() with 250ms interval
from machine import Pin
import time

led = Pin(“LED”, Pin.OUT)

#  blink five times
for i in range(10):
  led.toggle()
  time.sleep(0.25)    # Wait 250 milliseconds
  
#Code 007 End.
#######################################################

#######################################################
#Code 008 Start: use led.toggle() with 250ms interval
from machine import Pin
import time

led = Pin(“LED”, Pin.OUT)

bilang = 0
while True:
  if bilang < 5:
    led.on()
    time.sleep(0.25)
    led.off()
    time.sleep(0.25)
    bilang += 1
  else:
    print("Tapos Na.")
    break
  
#Code 008 End.
#######################################################

#######################################################
#Code 009 Start:
from machine import Pin
import time

led = Pin(“LED”, Pin.OUT)

for i in range(10):
  led.on()
  time.sleep(0.5)
  led.off()
  time.sleep(0.5)

  match i:
    case 0:
      print("Unang blink")
    case 1:
      print("Pangalawang blink")
    case 2:
      print("Pangatlong blink")
    case 3:
      print("Pang-apat blink")
    case 4:
      print("Pang-limang blink")
    case 5:
      print("Pang-anim na blink")
    case 6:
      print("Pang-pitong blink")
    case 7:
      print("Pang-walong blink")
    case 8:
      print("Pang-siyam blink")
    case _:
      print("Tapos na manidn.")

#Code 009 End.
#######################################################

#######################################################
#Code 009 Start: micro-python equivalent
from machine import Pin
import time

led = Pin(“LED”, Pin.OUT)

for i in range(10):
  led.on()
  time.sleep(0.5)
  led.off()
  time.sleep(0.5)
  
  if i == 0:
    print("Unang blink")
  elif i == 1:
    print("Pangalawang blink")
  elif i == 2:
    print("Pangatlong blink")
  elif i == 3:
    print("Pang-apat blink")
  elif i == 4:
    print("Pang-limang blink")
  elif i == 5:
    print("Pang-anim na blink")
  elif i == 6:
    print("Pang-pitong blink")
  elif i == 7:
    print("Pang-walong blink")
  elif i == 8:
    print("Pang-siyam blink")
  else:
    print("Tapos na manidn.")

#Code 009 End.
#######################################################


#######################################################
#Code 010 Start:
from machine import ADC
import time

# Create ADC object on temperature sensor channel (ADC4)
sensor_temp = ADC(4)

# Reference voltage (typically 3.3V)
conversion_factor = 3.3 / 65535

while True:
  reading = sensor_temp.read_u16()           # Raw ADC value
  voltage = reading * conversion_factor      # Convert to voltage
  temperature_c = 27 - (voltage - 0.706) / 0.001721  # Formula from Pico datasheet

  print("Temperature: {:.2f}°C".format(temperature_c))
  time.sleep(0.25)
#Code 010 End.
#######################################################

#######################################################
#Code 011 Start: (in Python a function is defined using the def keyword)
from machine import ADC
import time

# Create ADC object on temperature sensor channel (ADC4)
sensor_temp = ADC(4)

# Reference voltage (typically 3.3V)
conversion_factor = 3.3 / 65535

def read_temp_c():
  reading = sensor_temp.read_u16()           # Raw ADC value
  voltage = reading * conversion_factor      # Convert to voltage
  temperature_c = 27 - (voltage - 0.706) / 0.001721  # Formula from Pico datasheet
  print("Temperature: {:.2f}°C".format(temperature_c))

while True:
  read_temp_c()
  time.sleep(0.25)

#Code 011 End.
#######################################################

#######################################################
#Code 012 Start: (to concatenate, or combine, two strings you can use the + operator.)
from machine import ADC
import time, sys

# Create ADC object on temperature sensor channel (ADC4)
sensor_temp = ADC(4)

# Reference voltage (typically 3.3V)
conversion_factor = 3.3 / 65535

def read_temp_c():
  reading = sensor_temp.read_u16()           # Raw ADC value
  voltage = reading * conversion_factor      # Convert to voltage
  temperature_c = 27 - (voltage - 0.706) / 0.001721  # Formula from Pico datasheet
  print("Temperature: {:.2f}°C".format(temperature_c))

def celsius_papuntang_fahrenheit(c):
    return c * 9 / 5 + 32

def celsius_papuntang_kelvin(c):
    return c + 273.15

while True:
  temp_reading_c = read_temp_c()
  print("Temp (°C): " + temp_reading_c)

  temp_reading_f = celsius_papuntang_fahrenheit(temp_reading_c))
  print("Temp (°F): " + temp_reading_f)

  temp_reading_k = celsius_papuntang_kelvin(temp_reading_c))
  print("Temp (K): " + temp_reading_k)

  time.sleep(0.25)

#Code 012 End.
#######################################################

#######################################################
#Code / Start:

#Code / End.
#######################################################
