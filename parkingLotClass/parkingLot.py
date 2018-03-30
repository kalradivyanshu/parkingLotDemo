class ParkingLot:
	def __init__(self, numberOfSlots):
		self.numberOfSlots = numberOfSlots
		self.filledSlots = []
		self.freeSlots = list(range(numberOfSlots))
		self.colorToSlots = {}
		self.colorToNumberplate = {}
		self.numberPlateToSlot = {}
		self.slotToCar = {}

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
		self.slotToCar[slotAlloted] = car
		return True

	def carLeft(self, slot):
		if slot in self.freeSlots:
			return False
		self.filledSlots.remove(slot)
		self.freeSlots.append(slot)
		try:
			car = self.slotToCar.pop(slot, None)
			self.numberPlateToSlot.pop(car.getNumberPlate(), None)
			color = car.getColor()
			self.colorToSlots[color].remove(slot)
			self.colorToNumberplate[color].remove(car.getNumberPlate())
			return True
		except:
			return False

	def getSlotNumbersForCarsWithColor(self, color):
		return getListFromDict(self, self.colorToSlots, color)

	def getNumberPlatesForCarsWithColor(self, color):
		return getListFromDict(self, self.colorToNumberplate, color)

	def getSlotNumberForNumberPlate(self, numberPlate):
		try:
			return numberPlateToSlot[numberPlate]
		except KeyError:
			return None
	