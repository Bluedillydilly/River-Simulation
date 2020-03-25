"""
	Map.py
	Author:

	Class responsible for holding information related section of terrain and
	characteristics related to that.
"""

from Speck import Speck

class TMap:
	"""
		Information about a section of terrain.
	"""

	name = ""
	mapImg = []
	terrain = []
	mapID = -1
	size = (-1,-1)

	def __init__(self, name, mapImg, specks = [], mapID = -1):
		self.name = name
		self.terrain = specks
		self.mapID = mapID
		self.mapImg = mapImg
		self.size = mapImg.size

	def updateMap(self):
		upPixels = [[(0,0,0) for y in self.size[1]] for x in self.size[0]]
		for x in self.size[0]:
			for y in self.size[1]:
				upPixels[x,y] = self.terrain[x,y].color()	

	def updateTerrain(self, newT):
		self.terrain = newT

	def loadMap(self):
		"""
			get the array representation of a map
		"""
		return self.mapImg.load()

	def saveToFile(self):
		"""
			Save the PIL object, mapImg, as an image.
		"""
		self.mapImg.save(self.name)
	
	