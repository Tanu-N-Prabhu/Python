with open("test.txt", "w") as file:
	for number in range(10):
		file.write(str(number))


data = open("test.txt").read()
print(data)


# automated close the file when read/write operation complete
with open("test.txt", "r") as file:
	line = file.readline()
	print(line)

