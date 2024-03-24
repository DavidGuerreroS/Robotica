import sim 
import numpy as np

def connect(port):
    sim.simxFinish(-1)
    clientID= sim.simxStart('127.0.0.1', port,True,True,2000,2)
    if clientID == 0: print('conectado a', port)
    else: print('No se pudo Conectar')
    return clientID

clientID = connect(19999)

returnCode, handle = sim.simxGetObjectHandle(clientID,'Dummy',sim.simx_opmode_blocking)
dummy = handle
print(dummy)

ret, joint1=sim.simxGetObjectHandle(clientID,'Joint1',sim.simx_opmode_blocking)
ret, joint2=sim.simxGetObjectHandle(clientID,'Joint2',sim.simx_opmode_blocking)
print(joint1, joint2)

returnCode, pos1 = sim.simxGetJointPosition(clientID, joint1,sim.simx_opmode_blocking)
returnCode, pos2 = sim.simxGetJointPosition(clientID, joint2,sim.simx_opmode_blocking)
print(pos1, pos2)

q1 = 0 * np.pi/180
returnCode = sim.simxSetJointTargetPosition(clientID, joint1, q1, sim.simx_opmode_oneshot)
q2 = 0 * np.pi/180
returnCode1 = sim.simxSetJointTargetPosition(clientID, joint2, q2, sim.simx_opmode_oneshot)
print(returnCode, returnCode1)

returnCode, pos = sim.simxGetObjectPosition(clientID, dummy, -1, sim.simx_opmode_blocking)
print(pos)