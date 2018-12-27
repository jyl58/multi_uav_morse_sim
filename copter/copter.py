from morse.builder import *
def new_copter(link_protocol="socket",copter_name="Vehicle"):
	'''
	new a copter and imu,gps,engines etc
	'''
	copter = Quadrotor()
	copter.properties(Object = True, Graspable = False, Label = copter_name)
	pose = Pose()
	copter.append(pose)

	imu = IMU()
	copter.append(imu)

	gps = GPS()
	gps.alter('UTM')
	copter.append(gps)

	velocity = Velocity()
	copter.append(velocity)

	# create a compound sensor of all of the individual sensors and stream it
	all_sensors = CompoundSensor([imu, gps, velocity, pose])
	all_sensors.add_stream(link_protocol)
	copter.append(all_sensors)

	camera = VideoCamera(name=copter_name+"_Camera")
	camera.translate(x=0, y=0, z=0.2)
	copter.append(camera)
	camera.properties(cam_far=800)
	camera.properties(Vertical_Flip=True)
	
	# make the vehicle controllable via force and torque
	# this will be available on port 4000 by default
	engines = QuadrotorDynamicControl()
	copter.append(engines)
	engines.add_stream(link_protocol)

	return (copter)