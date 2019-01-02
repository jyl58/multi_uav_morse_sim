from morse.builder import *
from copterlib.copter import *
import bpy
import configparser

cf=configparser.ConfigParser()
cf.read('./config/sim_config.cfg')

sim_copter_list=[]
sim_copter_list.append(copter("socket","copter_1"))
sim_copter_list.append(copter("socket","copter_2"))
sim_copter_list.append(copter("socket","copter_3"))
sim_copter_list.append(copter("socket","copter_4"))

copter_1=sim_copter_list[0].get_copter()
copter_2=sim_copter_list[1].get_copter()
copter_3=sim_copter_list[2].get_copter()
copter_4=sim_copter_list[3].get_copter()

#set the copter init pos
for i in range(len(sim_copter_list)):
	sim_copter_list[i].get_copter().translate(0, 2*i, 1.0)

# change the rotor color 
bpy.data.objects[copter_1.name].data.materials["RotorGrey"].diffuse_color=(0.657,0.035,0.662)
#text=bpy.ops.object.text_add()
bpy.data.objects[copter_2.name].data.materials["RotorGrey.001"].diffuse_color=(0.035,0.774,0.058)
bpy.data.objects[copter_3.name].data.materials["RotorGrey.002"].diffuse_color=(0.774,0.009,0.005)
bpy.data.objects[copter_4.name].data.materials["RotorGrey.003"].diffuse_color=(0.006,0.029,0.774)

env = Environment('land-1/trees', fastmode=False)

env.configure_multinode(protocol="socket", server_address=cf["sim_sever"]["sim_sever_address"], server_port=cf["sim_sever"]["sim_sever_port"], distribution={
	sim_copter_list[0].get_sim_name(): [copter_1.name],
	sim_copter_list[1].get_sim_name(): [copter_2.name],
	sim_copter_list[2].get_sim_name(): [copter_3.name],
	sim_copter_list[3].get_sim_name(): [copter_4.name]
	})
    
env.set_camera_location([10.0, -10.0, 10.0])
env.set_camera_rotation([1.0470, 0, 0.7854])
env.set_camera_clip(clip_end=1000)

#full screen set
bpy.context.scene.game_settings.show_fullscreen=True

# startup at CMAC. A location is needed for the magnetometer
env.properties(longitude = 149.165230, latitude = -35.363261, altitude = 584.0)

#creat the sim env    
env.create(sim_copter_list[2].get_sim_name())
