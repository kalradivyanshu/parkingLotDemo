import sys
from commandHandling import handle

try:
	filePath = sys.argv[1]
except:
	filePath = None


if filePath != None:
	try:
		f = open(filePath)
		content = f.readlines()
		f.close()
		for command in content:
			try:
				handle(command[:-1]) #to remove \n
			except Exception as e:
				print("In command", command[:-1])
				print("Error: ", e)
				sys.exit()

	except FileNotFoundError:
		print(filePath, "does not exist.")
		sys.exit()

else:
	print("Type \"exit\" to exit.")
	while True:
		command = input(">> ")
		if command == "exit":
			sys.exit()
		try:
			handle(command) #to remove \n
		except Exception as e:
			print("In command", command)
			print("Error: ", e)
