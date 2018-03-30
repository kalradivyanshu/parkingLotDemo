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
			handle(command[:-1]) #to remove \n

	except FileNotFoundError:
		print(filePath, "does not exist.")
		sys.exit()