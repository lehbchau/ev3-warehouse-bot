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

TURN_SPEED = 20
BASE_SPEED_PERCENT = -25
STRAIGHT_SPEED = 4.9375
runtime1 = 8/STRAIGHT_SPEED
runtime2 = 92/STRAIGHT_SPEED

gyro_sensor.calibrate()
mt.on_for_seconds(SpeedPercent(-BASE_SPEED_PERCENT),SpeedPercent(-BASE_SPEED_PERCENT), runtime1)
time.sleep(1)

gyro_sensor.reset()
while abs(gyro_sensor.angle) < 90:
    mt.on(SpeedPercent(-TURN_SPEED),SpeedPercent(TURN_SPEED))

mt.on_for_seconds(SpeedPercent(BASE_SPEED_PERCENT),SpeedPercent(BASE_SPEED_PERCENT), runtime2/2)
time.sleep(0.5)
mt.on_for_seconds(SpeedPercent(2),SpeedPercent(-2),0.5)
mt.on_for_seconds(SpeedPercent(BASE_SPEED_PERCENT),SpeedPercent(BASE_SPEED_PERCENT), runtime2/2)
time.sleep(0.5)

while abs(gyro_sensor.angle) < 90:
    mt.on(SpeedPercent(TURN_SPEED),SpeedPercent(-TURN_SPEED))

mt.on_for_seconds(SpeedPercent(BASE_SPEED_PERCENT),SpeedPercent(BASE_SPEED_PERCENT), runtime1)
