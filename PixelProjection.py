import numpy as np
import math as m
import matplotlib.pyplot as plt

#Input parameters
focal_length = float(input("What is your focal length in mm?"))*.001
altitude = float(input("What is your altitude in meters?"))
x = float(input("What is your pixel X-dimension in micrometers"))*.000001
y = float(input("What is your pixel y-dimension in micrometers"))*.000001

#Projection of pixel at NADIR
def New_VectorX(altitude,focal_length,x):
    
    vx = (altitude*x)/focal_length
   
    return[vx]

def New_VectorY(altitude,focal_length,y):

    vy = (altitude*y)/focal_length
    
    return [vy]

u = New_VectorX(altitude,focal_length,x)
v = New_VectorY(altitude,focal_length,y)

#New Projected Vector At NADIR
v1 = (u,v,[altitude])  
print("Your new projected pixel vector at NADIR =", v1)

#Euler Rotation Matrices
def Rx(theta):
  return np.matrix([[ 1, 0           , 0           ],
                   [ 0, m.cos(theta),-m.sin(theta)],
                   [ 0, m.sin(theta), m.cos(theta)]])
  
def Ry(theta):
  return np.matrix([[ m.cos(theta), 0, m.sin(theta)],
                   [ 0           , 1, 0           ],
                   [-m.sin(theta), 0, m.cos(theta)]])
  
def Rz(theta):
  return np.matrix([[ m.cos(theta), -m.sin(theta), 0 ],
                   [ m.sin(theta), m.cos(theta) , 0 ],
                   [ 0           , 0            , 1 ]])

#Euler Rotation Input Values for Inertial Sensor
phi = float(input("What is your roll angle in degrees?"))*m.pi/180 
theta = float(input("What is your pitch angle in degrees?"))*m.pi/180
psi =float(input("What is your yaw angle in degrees?"))*m.pi/180 
print("phi =", phi)
print("theta  =", theta)
print("psi =", psi)
  
#Obtaining rotation matrix based on order rotated, change order depending on rotation
R = Rz(psi) * Ry(theta) * Rx(phi)
print("Your Euler Rotation Matrix =", np.round(R, decimals=2)) 

#New projected vector after Euler Rotation
v2 = R * v1
print("Your pixel projection after the Euler rotation =", np.round(v2, decimals=2))

#Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Cartesian axes
ax.quiver(-1, 0, 0, 3, 0, 0, color='grey',linestyle='dashed')
ax.quiver(0, -1, 0, 0,3, 0, color='grey',linestyle='dashed')
ax.quiver(0, 0, -1, 0, 0, 3, color='grey',linestyle='dashed')

# Vector before rotation
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='blue')

# Vector after rotation change based on output value from v2
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='red')
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
plt.savefig("pixelprojection.png")
plt.show()
