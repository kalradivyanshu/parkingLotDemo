import sys

try:
	filePath = sys.argv[1]
except:
	filePath = None

def handle(command):
	print(command)

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