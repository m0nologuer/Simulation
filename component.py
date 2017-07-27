class Component(object):
	"""Base class for the scripting of a component"""
	def __init__(self, name, model, physics):
		self.model = model
		self.name = name
		self.physics = physics
		return

	def setup(self):
		return

	def physics_setup(self, node_dict):
		return

	def update(self, task):
		return task.cont
