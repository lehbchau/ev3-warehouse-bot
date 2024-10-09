#!/usr/bin/env python3

## Imports all Objects and Methods from the motor module
from ev3dev2.motor import *
from time import sleep
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.display import Display

# Initialize motors and sensors
mt = MoveTank(OUTPUT_A,OUTPUT_D)
color_sensor = ColorSensor(INPUT_2)
screen = Display()
barcode_data = []

# Move to product
def MoveForward():
    mt.on_for_seconds(SpeedPercent(5), SpeedPercent(5), 1)

def ScanBarcode():
    strBarcode = ""
    for i in range(4):
        barcode_data.append(color_sensor.color())
        strBarcode += str(barcode_data[i])
        mt.on_for_seconds(SpeedPercent(-1),SpeedPercent(-1), 0.2) # Move forward to scan the next color
        time.sleep(0.25)
    return strBarcode

# List of 4 correct barcodes: 1 is black, 6 is white
correct_product = ["1666", "1616", "1166", "1661"]

def IsCorrectProduct():
    barcode = ScanBarcode()
    for k in range(4):
        if barcode == correct_product[k]:
            return True
    return False
        
barcode = ScanBarcode()
print("Scanned Barcode:", barcode)
screen.clear()

if IsCorrectProduct():
    print("Correct product detected. Pick up.")
    screen.text_pixels("Correct product detected. Pick up.", x=0, y=0, text_color='black')
    screen.update()

else:
    print("Incorrect product detected. This is box {0}.".format())
    screen.text_pixels("Incorrect product detected. Ignore.", x=0, y=0, text_color='black')
    screen.update()

    


    
    



