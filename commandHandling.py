from carClass.car import Car
from parkingLotClass.parkingLot import ParkingLot

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
			print("Syntax for create_parking_lot: create_parking_lot <Number>.")
			sys.exit()
		number = int(second)
		handle.parkingLot = ParkingLot(number)

	elif first == "park":
		if second == None or third == None:
			print("Syntax for park: park <Registration Number> <Colour>.")
			sys.exit()
		if handle.parkingLot == None:
			print("Please Create parking lot first.")
			sys.exit()
		car = Car(second, third)
		flag, slot = handle.parkingLot.parkCar(car)
		if not flag:
			print("Sorry, parking lot is full.")
		else:
			print("Allocated slot number:", slot)

	elif first == "leave":
		pass
	elif first == "registration_numbers_for_cars_with_colour":
		pass
	elif first == "slot_numbers_for_cars_with_colour":
		pass
	elif first == "slot_number_for_registration_number":
		pass

handle.parkingLot = None