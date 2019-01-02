from morse.builder import *

class copter(object):
	def __init__(self,link_protocol,copter_name):
		'''
		new a copter and imu,gps,engines etc
		'''
		self.copter = Quadrotor()
		self.sim_name=copter_name
		self.copter.properties(Object = True, Graspable = False, Label = copter_name)
		self.pose = Pose()
		self.copter.append(self.pose)

		self.imu = IMU()
		self.copter.append(self.imu)

		self.gps = GPS()
		self.gps.alter('UTM')
		self.copter.append(self.gps)

		self.velocity = Velocity()
		self.copter.append(self.velocity)

		# create a compound sensor of all of the individual sensors and stream it
		self.all_sensors = CompoundSensor([self.imu, self.gps, self.velocity, self.pose])
		self.all_sensors.add_stream(link_protocol, port=60000)
		self.copter.append(self.all_sensors)

		self.camera = VideoCamera(name=copter_name+"_Camera")
		self.camera.translate(x=0, y=0, z=0.17)
		self.copter.append(self.camera)
		self.camera.properties(cam_far=800)
		self.camera.properties(Vertical_Flip=True)
		
		# make the vehicle controllable via force and torque
		# this will be available on port 4000 by default
		self.engines = QuadrotorDynamicControl()
		self.copter.append(self.engines)
		self.engines.add_stream(link_protocol, port=60001)
		
	def get_copter(self):
		return self.copter
	
	def get_sim_name(self):
		return self.sim_name
