'''

A menu of various test commands to send the robot to test that it is functioning well
before initiating scanning runs.

@author: Agusti Pellicer (Aalto University)

'''


import Gado_2.Robot as Robot

if __name__ == '__main__':

	gado = Robot.Robot('/dev/ttyACM0')

	while True:
		print "Test Robot menu"
		print "---------------"
		print "1. Move arm"
		print "2. Activate vacuum"
		print "3. Deactivate vacuum"
		print "4. Move actuator"
		print "5. Pick up an object"
		print "6. Print status of the robot"
		print "7. Exit"
		try:
			option = raw_input("What's going to be? ")
			if int(option) == 1:
				number = raw_input("Introduce the value for the arm:")
				gado.sendRawArmWithoutBlocking(int(number))
			if int(option) == 2:
				number = raw_input("Introduce the value for the vacuum:")
				gado.sendVacuum(int(number))
			if int(option) == 3:
				gado.sendVacuum(0)
			if int(option) == 4:
				number = raw_input("Actuator position:")
				gado.sendRawActuatorWithoutBlocking(int(number))
			if int(option) == 5:
				gado.lowerAndLiftInternal()
				gado.sendRawActuatorWithBlocking(60)
			if int(option) == 6:
				gado.sendCommand("d",True)
				print gado.status
			if int(option) == 7:
				exit()
		except ValueError:
			print 'Insert a proper option number'
			pass
