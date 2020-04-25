"""
	Map.py
	Author:

	Class responsible for holding information related section of terrain and
	characteristics related to that.
"""

from Speck import Speck
from PIL import Image

class TMap:
	"""
		Information about a section of terrain.
	"""

	name = ""
	terrain = []
	mapID = -1
	size = (-1,-1)

	def __init__(self, name, map = [], mapID = -1):
		self.name = name
		self.mapID = mapID
		if map:
			self.size = map.size
			self._tFromMap(map)

	def _tFromMap(self, map):
		mapPixels = list(map.getdata())
		newT = [[(0,0,0) for p in self.size[1]] for r in self.size[0]]
		for x in self.size[0]:
			for y in self.size[1]:
				newT.append(Speck(terr = [], 
				colo = mapPixels[x][y]))
		self.terrain = newT

	def _cMap(self):
		colors = [[sp.color() for sp in r] for r in self.terrain]
		return colors



	def getColors(self):
		"""
			get the array representation of a map
		"""
		return self._cMap()

	def saveToFile(self):
		"""
			Save the PIL object, mapImg, as an image.
		"""
		self.mapImg.save(self.name)
	
	