#!/usr/bin/env python3

## Imports all Objects and Methods from the motor module
from ev3dev2.motor import *
from time import sleep
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import GyroSensor

## Sets mt Equal to the MoveTank of two motors allowing
## them to run concurrently
mt = MoveTank(OUTPUT_A,OUTPUT_D)
gyro_sensor = GyroSensor(INPUT_4)

# Initialize motors
y_distance = 36
distance_from_edge = 30.5 # Adjust according to box number
x_distance = 6 + distance_from_edge 
TURN_SPEED = 20
BASE_SPEED_PERCENT = -25
STRAIGHT_SPEED = 4.9375
run_time1 = y_distance/STRAIGHT_SPEED
run_time2 = x_distance/STRAIGHT_SPEED

gyro_sensor.reset()

# Move to the target y location
mt.on_for_seconds(SpeedPercent(BASE_SPEED_PERCENT),SpeedPercent(BASE_SPEED_PERCENT),run_time1)

# Rotate 90 deg
gyro_sensor.reset()
while abs(gyro_sensor.angle) < 90:
    mt.on(SpeedPercent(-TURN_SPEED),SpeedPercent(TURN_SPEED))

# Move to the target x location
mt.on_for_seconds(SpeedPercent(BASE_SPEED_PERCENT),SpeedPercent(BASE_SPEED_PERCENT),run_time2)

# Stop 5 seconds
time.sleep(5)
mt.on_for_seconds(SpeedPercent(2),SpeedPercent(-2),0.25)

# Move to x of home b
xdistance_to_b = 96 - x_distance
run_time3 = xdistance_to_b/STRAIGHT_SPEED
mt.on_for_seconds(SpeedPercent(BASE_SPEED_PERCENT),SpeedPercent(BASE_SPEED_PERCENT),run_time3)

# Rotate 90
time.sleep(1)
while abs(gyro_sensor.angle) < 90:
    mt.on(SpeedPercent(-TURN_SPEED),SpeedPercent(TURN_SPEED))

# Move to y of home b
ydistance_to_b = 34.5
run_time4 = ydistance_to_b/STRAIGHT_SPEED
mt.on_for_seconds(SpeedPercent(BASE_SPEED_PERCENT),SpeedPercent(BASE_SPEED_PERCENT),run_time4)








