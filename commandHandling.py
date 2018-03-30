from carClass.car import Car
from parkingLotClass.parkingLot import ParkingLot

def printList(l):
	if len(l) == 0:
		print("None")
		return None
	for item in l:
		print(item, end = " ")
	print()

def handle(command):
	try:
		first, second = command.split(" ")
		third = None
	except ValueError:
		try:
			first, second, third = command.split(" ")
		except ValueError:
			first = command
			second, third = None, None
	if first == "create_parking_lot":
		if second == None or not second.isnumeric():
			raise ValueError("Syntax for create_parking_lot: create_parking_lot <Number>.")
		number = int(second)
		handle.parkingLot = ParkingLot(number)
		print("Created a parking lot with 6 slots")

	elif first == "park":
		if second == None or third == None:
			raise ValueError("Syntax for park: park <Registration Number> <Colour>.")
		if handle.parkingLot == None:
			raise ValueError("Please create parking lot first.")
		car = Car(second, third)
		flag, slot = handle.parkingLot.parkCar(car)
		if not flag:
			print("Sorry, parking lot is full.")
		else:
			print("Allocated slot number:", slot)

	elif first == "leave":
		if second == None or not second.isnumeric():
			raise ValueError("Syntax for leave: leave <SlotNumber>.")
		slot = int(second)
		if handle.parkingLot == None:
			raise ValueError("Please create parking lot first.")
		flag = handle.parkingLot.carLeft(slot)
		if flag == False:
			print("Slot already empty.")
		else:
			print("Slot number", slot, "is free")

	elif first == "status":
		if handle.parkingLot == None:
			print("No parking lot found.")
		print(handle.parkingLot)

	elif first == "registration_numbers_for_cars_with_colour":
		if handle.parkingLot == None:
			raise ValueError("No parking lot found.")
		if second == None:
			raise ValueError("Syntax for registration_numbers_for_cars_with_colour: registration_numbers_for_cars_with_colour <colour>.")
		printList(handle.parkingLot.getNumberPlatesForCarsWithColor(second))

	elif first == "slot_numbers_for_cars_with_colour":
		if handle.parkingLot == None:
			raise ValueError("No parking lot found.")
		if second == None:
			raise ValueError("Syntax for slot_numbers_for_cars_with_colour: slot_numbers_for_cars_with_colour <colour>.")
		printList(handle.parkingLot.getSlotNumbersForCarsWithColor(second))

	elif first == "slot_number_for_registration_number":
		if handle.parkingLot == None:
			raise ValueError("No parking lot found.")
		if second == None:
			raise ValueError("Syntax for slot_number_for_registration_number: slot_number_for_registration_number <RegistrationNumber>")
		slot = handle.parkingLot.getSlotNumberForNumberPlate(second)
		if slot == None:
			print("Not Found.")
		else:
			print(slot)
	else:
		raise ValueError("Command not found.")

handle.parkingLot = None