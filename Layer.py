"""
	Layer.py
	Author:

	Class reprsentating a "slice" of a Speck and
	the characteristics associated with that
"""

class Layer:

	location = {}
	material = {}

	def __init__(self, location = {}):
		self.location = location