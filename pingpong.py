from component import Component
from panda3d.core import Vec3
from panda3d.core import LRotationf

class PingPong(Component):
	"""Base class for the scripting of a component"""
	def __init__(self, name, model, physics):
		self.model = model
		self.name = name
		self.physics = physics
		return

	#Move according to user actions
	def act(self, action, object_array):
		#4 axes - yaw pitch roll rotation
		# + x position
		self.model.addTorque(LRotationf(action[0], action[1], action[2]))
		self.model.addImpulse(Vec3(action[3], 0, 0))
