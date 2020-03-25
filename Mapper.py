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
from Map import TMap

class Mapper:
	"""
		Makes and holds maps
	"""

	maps = []

	def new(self, fn="", mode="RGB", size=(60,60), color=(0, 0, 0), an = "" ):
		fileName = fn if fn else d.datetime.now().strftime("%b%d-%y-%H%M")+".png"
		mapN = Image.new(mode, size, color)

		self.maps.append(
			TMap(fileName, mapN)
		)

	def saveToFile(self, mapID = -1):
		mapN = self.maps[mapID]
		self.maps[mapID].saveToFile()

		print("'"+mapN.name+"' map saved.")

	def drawLand(self, mapN):
		pixels = mapN.loadMap()
		for x in range(mapN.size[0]):
			for y in range(mapN.size[1]):
				pixels[x,y] = Speck.terrColo["land"]
				print(x, ",", y, "changed to",pixels[x,y])

	def drawRiver(self, mapN):
		# array representation of a map
		pixels = mapN.loadMap()
		
		# river parameters
		rWidth = mapN.size[0] * 0.20
		rWidth = int(rWidth)
		rHeight = mapN.size[1] 

		# location of river in the map
		sX = mapN.size[0] * 0.40
		sX = int(sX)
		sY = 0

		# write water pixels
		for x in range(sX, sX + rWidth):
			for y in range(sY, sY + rHeight):
				pixels[x,y] = Speck.terrColo["water"]
				print(x, ",", y, "changed to", pixels[x,y])





if __name__ == "__main__":
	m = Mapper()
	m.new()
	#m.save()
	m.drawLand(m.maps[-1])
	m.drawRiver(m.maps[-1])
	m.saveToFile()

	