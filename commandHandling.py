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

	elif first == "park":
		pass
	elif first == "leave":
		pass
	elif first == "registration_numbers_for_cars_with_colour":
		pass
	elif first == "slot_numbers_for_cars_with_colour":
		pass
	elif first == "slot_number_for_registration_number":
		pass