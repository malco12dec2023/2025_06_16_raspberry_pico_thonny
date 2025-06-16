# malcompm_code_pico.py
/*
Directions:
  DO NOT COPY THE CODE.
  Do NOT copy the code, type each code or
  edit each cganges to better understand
  the logic of operation.
*/

#######################################################
#Code 000 Start: (resistor, LED, breadboard, wires)
from machine import Pin
import time

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

#Code 005 End.
#######################################################

#######################################################
#Code 006 Start: use for loop to blink 10 times

#Code 006 End.
#######################################################

#######################################################
#Code / Start:

#Code / End.
#######################################################
