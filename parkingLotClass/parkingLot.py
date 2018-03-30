from tabulate import tabulate

class ParkingLot:
	def __init__(self, numberOfSlots):
		self.numberOfSlots = numberOfSlots
		self.filledSlots = []
		self.freeSlots = list(range(1, numberOfSlots + 1))
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
		if len(self.filledSlots) == self.numberOfSlots:
			return False, None
		slotAlloted = min(self.freeSlots)
		self.filledSlots.append(slotAlloted)
		self.freeSlots.remove(slotAlloted)
		self.appendToKey(self.colorToSlots, car.getColor(), slotAlloted)
		self.appendToKey(self.colorToNumberplate, car.getColor(), car.getNumberPlate())
		self.numberPlateToSlot[car.getNumberPlate()] = slotAlloted
		self.slotToCar[slotAlloted] = car
		return True, slotAlloted

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
		return self.getListFromDict(self.colorToSlots, color)

	def getNumberPlatesForCarsWithColor(self, color):
		return self.getListFromDict(self.colorToNumberplate, color)

	def getSlotNumberForNumberPlate(self, numberPlate):
		try:
			return self.numberPlateToSlot[numberPlate]
		except KeyError:
			return None

	def __str__(self):
		filledSlots = list(self.slotToCar.keys())
		filledSlots.sort()
		printList = []
		for slot in filledSlots:
			car = self.slotToCar[slot]
			numberPlate = car.getNumberPlate()
			color = car.getColor()
			printList.append([slot, numberPlate, color])
		return tabulate(printList, headers = ['Slot No.', 'Registration No', 'Colour'])
