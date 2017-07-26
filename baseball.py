from component import Component
from direct.task import Task

class Baseball(Component):
	"""Base class for the scripting of a component"""
	def __init__(self, name, model, physics):
		Component.__init__(name, model, physics)
		self.runtime = 0
		return

	#Count frames survived
	def update(self, task):
		self.runtime += 1.0
		return Task.cont

	#Reward is time spent
	def reward(self, object_array):
		return self.runtime

	#If the baseball is it way back...
	def episode_over(self, object_array):
		return (self.model.getPos().z > 10)