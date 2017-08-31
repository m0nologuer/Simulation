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
		#self.model.parent.node().addTorque(LRotationf(action[0], action[1], action[2]))
		#self.model.parent.node().addImpulse(Vec3(action[3], 0, 0))


	def update(self, task):

		#correction = (self.model.parent.getPos() - Vec3(0,5,5)) * 0.01
		#self.model.parent.node().addImpulse(correction)

		return task.cont
