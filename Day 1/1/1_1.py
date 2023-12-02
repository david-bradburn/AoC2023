#################################################################
###### https://adventofcode.com/2022/day/1 #######################
#################################################################

file = "input.txt"

DAY_NO = "1"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

print(rawInput)
cleanerInput = []
for i in rawInput:
	cleanerInput.append(i.strip('\n'))

print(cleanerInput)

sum = 0
for line in cleanerInput:
	for char in line:
		if char.isdigit():
			firstDigit = char
			break
	
	for char in line[::-1]:
		if char.isdigit():
			lastDigit = char
			break
	
	val =  firstDigit + lastDigit
	val = int(val)
	print(val)
	sum += val

print(sum)