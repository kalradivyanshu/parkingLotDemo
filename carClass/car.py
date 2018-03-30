class Car:
	def __init__(self, numberPlate, color):
		self.color = color
		self.numberPlate = numberPlate
		self.slot = -1

	def getColor(self):
		return self.color

	def getNumberPlate(self):
		return self.numberPlate

	def setSlot(self, slot):
		self.slot = slot

	def getSlot(self):
		return self.slot

	def __str__(self):
		return self.numberPlate + "; " + self.color