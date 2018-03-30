class ParkingLot:
	def __init__(self, numberOfSlots):
		self.numberOfSlots = numberOfSlots
		self.filledSlots = []
		self.freeSlots = list(range(numberOfSlots))
		self.colorToSlots = {}
		self.colorToNumberplate = {}
		self.numberPlateToSlot = {}

	def appendToKey(self, dic, key, val):
		try:
			dic[key].append(val)
		except KeyError:
			dic[key] = [val]
		return dic

	def getListFromDict(self, dic, key):
		try:
			return dic[key]
		except KeyError:
			return []

	def parkCar(self, car):
		if len(self.filledSlots) == self.filledSlots:
			return False
		slotAlloted = min(self.freeSlots)
		self.filledSlots.append(slotAlloted)
		self.freeSlots.remove(slotAlloted)
		self.appendToKey(self.colorToSlots, car.getColor(), slotAlloted)
		self.appendToKey(self.colorToNumberplate, car.getColor(), car.getNumberPlate())
		self.numberPlateToSlot[car.getNumberPlate()] = slotAlloted
		return True

	