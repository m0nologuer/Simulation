from component import Component

class Brick(Component):
	"""Base class for the scripting of a component"""
	def __init__(self, name, model, physics):
		self.model = model
		self.name = name
		self.physics = physics
		return
		