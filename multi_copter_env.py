from morse.builder import *
from copter import *
#import the blender api 
import bpy

copter_1=new_copter("socket","copter_1")
copter_2=new_copter("socket","copter_2")
copter_3=new_copter("socket","copter_3")
copter_4=new_copter("socket","copter_4")

#set the copter init pos
copter_1.translate(0, 0, 1.0)
copter_2.translate(0, 2, 1.0)
copter_3.translate(0, 4, 1.0)
copter_4.translate(0, 6, 1.0)

#set the copter color
bpy.data.materials["RotorGrey"].diffuse_color=(0.657,0.035,0.662)
bpy.data.materials["RotorGrey.001"].diffuse_color=(0.035,0.774,0.058)
bpy.data.materials["RotorGrey.002"].diffuse_color=(0.774,0.009,0.005)
bpy.data.materials["RotorGrey.003"].diffuse_color=(0.006,0.029,0.774)


env = Environment('land-1/trees', fastmode=False)

env.set_camera_location([10.0, -10.0, 10.0])
env.set_camera_rotation([1.0470, 0, 0.7854])

env.set_camera_clip(clip_end=1000)

# startup at CMAC. A location is needed for the magnetometer
env.properties(longitude = 149.165230, latitude = -35.363261, altitude = 584.0)

env.configure_multinode(protocol="socket", server_address="192.168.253.6", server_port="65000",distribution={
    "copter_1": [copter_1.name],
    "copter_2": [copter_2.name],
    "copter_3": [copter_3.name],
    "copter_4": [copter_4.name],
    })
    
#creat the sim env    
env.create()
