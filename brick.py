from component import Component

class Brick(Component):
	"""Base class for the scripting of a component"""
	def __init__(self, name, model, physics):
		Component.__init__(name, model, physics)
		return
		