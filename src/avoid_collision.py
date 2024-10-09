#!/usr/bin/env python3

from ev3dev2.motor import *
from time import sleep
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor.lego import UltrasonicSensor

ultrasonic = UltrasonicSensor(INPUT_1)
mt = MoveTank(OUTPUT_A,OUTPUT_D)

# Detect and avoid objects within 2 inches
THRESHOLD_DISTANCE = 2 

def AvoidingObjects():
    distance = UltrasonicSensor.distance_inches
    if distance <= THRESHOLD_DISTANCE:
        mt.on_for_seconds(15,-15,5)
    else:
        mt.on_for_seconds()
