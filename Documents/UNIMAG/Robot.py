from coppeliasim_zmqremoteapi_client import *
import numpy as np

client = RemoteAPIClient()

sim = client.require('sim')

h = sim.getObject('/Base')
print(h)

joint1 = sim.getObject('/Joint1')
joint2 = sim.getObject('/Joint2')
dummy = sim.getObject('/Dummy')
print(joint1, joint2, dummy)

pos1 = sim.getJointPosition(joint1)
pos2 = sim.getJointPosition(joint2)
pos3 = sim.getObjectPosition(dummy)
print(pos1, pos2, pos3)

sim.setJointTargetPosition(joint1, 65*np.pi/180)
sim.setJointTargetPosition(joint2, -90*np.pi/180)