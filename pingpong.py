from component import Component
from panda3d.core import Vec3

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
		self.model.parent.node().applyTorqueImpulse(Vec3(action[0], action[1], action[2]))
		self.model.parent.node().applyCentralImpulse(Vec3(action[3], 0, 0))


	def update(self, task):

		correction = (Vec3(0,5,5) - self.model.parent.getPos()) * 0.01
		self.model.parent.node().applyCentralImpulse(correction)

		return task.cont
