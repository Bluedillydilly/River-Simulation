"""
	Speck.py
	Author:

	Class representating "1 pixel" of a map and
	the characteristics associated with that.
"""

class Speck:

	location = {}
	#TODO implement terrainSlices
	#terrainSlice = []

	terrColo = {
		"water": (0,0,255),
		"land": (0, 255, 0),
		"rock": (127, 127, 127),
	}

	coloTerr = {
		v: k for k, v in terrColo.items()
	}

	def __init__(self, terr, colo):
		if terr:
			self.terrType = terr
		elif not terr and colo:
			self.terrType = self.terrColo[colo]
		else:
			self.terrType = "land"

	def color(self):
		return self.terrColo[self.terrType]
