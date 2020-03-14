"""
	Mapper.py
	Author: 

	Class responsible for creating maps to be traversed.
"""
from sys import argv, maxsize
from PIL import Image
from collections import defaultdict
import datetime as d
from Speck import Speck

class Mapper:
	"""
		Makes and holds maps
	"""

	maps = {}
	mapIDs = []
	altNames = []
	options = []
	agents = []

	def new(self, fileName="", mode="RGB", size=(60,60), color=(0, 0, 0), altName = "" ):
		fileName = fileName if fileName else d.datetime.now().strftime("%b%d-%y-%H%M")+".png"
		altName = altName if altName else fileName
		map = Image.new(mode, size, color)

		self.maps[fileName] = map
		self.mapIDs.append(fileName)
		self.altNames.append(altName)
		return map

	def save(self, mapID = -1):
		map = self.maps[self.mapIDs[mapID]]
		name = self.mapIDs[mapID]
		map.save(name)

		print("'", self.altNames[mapID], "' map saved as '", name, "'")

	def default(self, map):
		pass
		pixels = map.load()
		for x in range(map.size[0]):
			for y in range(map.size[1]):
				pixels[x,y] = Speck.terrColo["land"]
				print(y,",",x, "changed to",pixels[x,y])


	def line(self, terr, width=20, length=20):
		pass




if __name__ == "__main__":
	m = Mapper()
	m.new(altName="test")
	#m.save()
	m.default(m.maps[m.mapIDs[-1]])
	m.save()

	