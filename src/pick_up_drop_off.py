#!/usr/bin/env python3
from time import sleep
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import GyroSensor

## Sets mt Equal to the MoveTank of two motors allowing
## them to run concurrently
mt = MoveTank(OUTPUT_A,OUTPUT_D)
mm = Motor(OUTPUT_C)
gyro_sensor = GyroSensor(INPUT_4)

TURN_SPEED = 20
BASE_SPEED_PERCENT = -25
STRAIGHT_SPEED = 4.9375
runtime = 21/STRAIGHT_SPEED

mm = MediumMotor()

gyro_sensor.calibrate()

gyro_sensor.reset()
while abs(gyro_sensor.angle) < 90:
    mt.on(SpeedPercent(TURN_SPEED),SpeedPercent(-TURN_SPEED))

mm.on_for_seconds(SpeedPercent(5),7)
time.sleep(1)

time.sleep(2)
mt.on_for_seconds(SpeedPercent(-3),SpeedPercent-(3),1) 

# Pick up box
mm.on_for_seconds(SpeedPercent(-5),7)
time.sleep(2)

# Rotate 90
gyro_sensor.reset()
while abs(gyro_sensor.angle) < 90:
    mt.on(SpeedPercent(TURN_SPEED),SpeedPercent(-TURN_SPEED))

# Move forward to end of aisle
mt.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),5) 
time.sleep(1)

mt.on_for_seconds(SpeedPercent(-10),SpeedPercent(-10),1) 

# Drop off box
mm.on_for_seconds(SpeedPercent(5),6)

