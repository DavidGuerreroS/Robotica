from coppeliasim_zmqremoteapi_client import *
import numpy as np

client = RemoteAPIClient()

sim = client.require('sim')

h = sim.getObject('/Base')
print(h)

joint1 = sim.getObject('/joint1')
joint2 = sim.getObject('/joint2')
joint3 = sim.getObject('/joint3')
joint4 = sim.getObject('/joint4')
joint5 = sim.getObject('/joint5')
gripperHandle = sim.getObject('/BaxterGripper')
grippername = sim.getObjectAlias(gripperHandle)
motor = sim.getObject('./closeJoint')
opened = 0.045
closed = -0.0235
intervalo = [0.05-opened,opened-closed]
sim.setJointInterval(motor, False, intervalo)

pos1 = sim.getJointPosition(joint1)
pos2 = sim.getJointPosition(joint2)
pos3 = sim.getJointPosition(joint3)
pos4 = sim.getJointPosition(joint4)
pos5 = sim.getJointPosition(joint5)
print(pos1, pos2, pos3, pos4, pos5)

sim.startSimulation()

while True:
    if sim.getSimulationTime() < 5:
        sim.setJointTargetPosition(joint1, 0*np.pi/180)
        sim.setJointTargetPosition(joint2, 35*np.pi/180)
        sim.setJointTargetPosition(joint3, 35*np.pi/180)
        sim.setJointTargetPosition(joint4, 35*np.pi/180)
        sim.setJointTargetPosition(joint5, 0*np.pi/180)
    if sim.getSimulationTime()> 7 and sim.getSimulationTime() < 12:
        sim.setJointTargetPosition(joint1, 0*np.pi/180)
        sim.setJointTargetPosition(joint2, 0*np.pi/180)
        sim.setJointTargetPosition(joint3, 55*np.pi/180)
        sim.setJointTargetPosition(joint4, 90*np.pi/180)
        sim.setJointTargetPosition(joint5, 0*np.pi/180)
    if sim.getSimulationTime()> 12 and sim.getSimulationTime() < 16:
        sim.setJointTargetPosition(joint1, -90*np.pi/180)
        sim.setJointTargetPosition(joint2, 45*np.pi/180)
        sim.setJointTargetPosition(joint3, 45*np.pi/180)
        sim.setJointTargetPosition(joint4, 90*np.pi/180)
        sim.setJointTargetPosition(joint5, 90*np.pi/180)
    if sim.getSimulationTime()> 16 and sim.getSimulationTime() < 18:
        sim.setJointTargetPosition(joint1, 0*np.pi/180)
        sim.setJointTargetPosition(joint2, 0*np.pi/180)
        sim.setJointTargetPosition(joint3, 55*np.pi/180)
        sim.setJointTargetPosition(joint4, 90*np.pi/180)
        sim.setJointTargetPosition(joint5, 90*np.pi/180)
    if sim.getSimulationTime()> 18 and sim.getSimulationTime() < 22:
        sim.setJointTargetPosition(joint1, 90*np.pi/180)
        sim.setJointTargetPosition(joint2, 45*np.pi/180)
        sim.setJointTargetPosition(joint3, 45*np.pi/180)
        sim.setJointTargetPosition(joint4, 95*np.pi/180)
        sim.setJointTargetPosition(joint5, 90*np.pi/180)
    if sim.getSimulationTime() > 23:
        
        break
sim.stopSimulation()
    