from coppeliasim_zmqremoteapi_client import *
import numpy as np
import time
import keyboard

client = RemoteAPIClient()

sim = client.require('sim')

dummy = sim.getObject('/Dummy')
print(dummy)

posdummy = sim.getObjectPosition(dummy)
print(posdummy)

right_motor = sim.getObject('/right_motor')
left_motor = sim.getObject('/left_motor')
caster_direction = sim.getObject('/caster_direction')
caster_free = sim.getObject('/caster_free')
print("Manejadores obtenidos:", right_motor, left_motor, caster_free, caster_direction)

sensor0 = sim.getObject('/ultrasonicSensor0')
sensor1 = sim.getObject('/ultrasonicSensor1')
sensor2 = sim.getObject('/ultrasonicSensor2')
sensor3 = sim.getObject('/ultrasonicSensor3')
sensor4 = sim.getObject('/ultrasonicSensor4')
sensor5 = sim.getObject('/ultrasonicSensor5')
sensor6 = sim.getObject('/ultrasonicSensor6')
sensor7= sim.getObject('/ultrasonicSensor7')
sensor8 = sim.getObject('/ultrasonicSensor8')
sensor9 = sim.getObject('/ultrasonicSensor9')
sensor10 = sim.getObject('/ultrasonicSensor10')
sensor11 = sim.getObject('/ultrasonicSensor11')
sensor12 = sim.getObject('/ultrasonicSensor12')
sensor13 = sim.getObject('/ultrasonicSensor13')
sensor14 = sim.getObject('/ultrasonicSensor14')
sensor15 = sim.getObject('/ultrasonicSensor15')
sensores = []
sensores.append(sensor0)
sensores.append(sensor1)
sensores.append(sensor2)
sensores.append(sensor3)
sensores.append(sensor4)
sensores.append(sensor5)
sensores.append(sensor6)
sensores.append(sensor7)
sensores.append(sensor8)
sensores.append(sensor9)
sensores.append(sensor10)
sensores.append(sensor11)
sensores.append(sensor12)
sensores.append(sensor13)
sensores.append(sensor14)
sensores.append(sensor15)
print(sensores)

nodetectiondist = 0.5
maxdetectiondist = 0.3
detect=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
braitenbergL=[-0.2,-0.4,-0.6,-0.8,-1,-1.2,-1.4,-1.6, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
braitenbergR=[-1.6,-1.4,-1.2,-1,-0.8,-0.6,-0.4,-0.2, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
v0= 3.0
sim.startSimulation()

while True:
    for i in range(16):
        res, dist, point, object, n = sim.readProximitySensor(sensores[i])
        if res > 0 and dist < nodetectiondist:
            if dist < maxdetectiondist:
                dist = maxdetectiondist
                detect[i] = 1 - ((dist-maxdetectiondist)/(nodetectiondist-maxdetectiondist))
        else:
            detect[i] = 0

    left_wheel_speed = v0
    right_wheel_speed = v0

    for i in range(16):
        left_wheel_speed = left_wheel_speed + braitenbergL[i]*detect[i]
        right_wheel_speed = right_wheel_speed + braitenbergR[i]*detect[i]

    sim.setJointTargetVelocity(left_motor, left_wheel_speed)
    sim.setJointTargetVelocity(right_motor, right_wheel_speed)

    if keyboard.is_pressed('q'):
        left_wheel_speed = 0.0
        right_wheel_speed = 0.0
        sim.setJointTargetVelocity(left_motor, left_wheel_speed)
        sim.setJointTargetVelocity(right_motor, right_wheel_speed)
        break
