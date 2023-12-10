#################################################################
###### https://adventofcode.com/2022/day/3 #######################
#################################################################

file = "input.txt"

DAY_NO = "3"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = [i.strip() for i in rawInput]
print(cleanerInput)
for i in cleanerInput:
	print(i.split("."))


class d3():
	def __init__(self, input) -> None:
		self.input = input
		self.HEIGHT = len(input)
		self.WIDTH = len(input[0])
		self.p1()

	def makeSymbolDict(self):
		self.symbolArr = []
		for yindex, row in enumerate(self.input):
			for xindex, val in enumerate(row):
				if not val.isdigit() and val != ".":
					if val in self.symbol_dict:
						self.symbol_dict[val].append((xindex, yindex))
					else:
						self.symbol_dict[val] = [(xindex, yindex)]
					
					self.symbolArr.append((xindex, yindex))
				# print(cleanerInput[yindex][xindex])

	def replaceSymbols(self):
		self.onlyNumbers = ["" for i in range(self.HEIGHT)]
		# print(self.onlyNumbers)
		for yindex, row in enumerate(self.input):
			for xindex, val in enumerate(row):
				if not val.isdigit():
					self.onlyNumbers[yindex] += "."
				else:
					self.onlyNumbers[yindex] += val

		print(self.onlyNumbers)


	def processNumbers(self):
		x = 0
		y = 0
		self.splitarr = [i.split(".") for i in self.onlyNumbers]
		# for yindex,y in enumerate(self.splitarr)
		print(self.splitarr)
		self.listofnumbers = []
		while y < self.HEIGHT:
			for row in self.splitarr:
				x = 0
				NumberonRow = False	
				for element in row:
					# print(Last3wasdidgt, Last2wasdidgt)

					elementlen = len(element)
					print(element, elementlen)
					if elementlen:
						if NumberonRow:
							print("correctinhg")
							modifier = 1	
						else:
							modifier = 0
						x += modifier

						NumberonRow = True
						val = int(element)
						coords = [(i, y) for i in range(x, x+elementlen)]
						print(val, coords)
						self.listofnumbers.append([val, coords])
						Lastwasdigit = True
					else:
						elementlen = 1
						Lastwasdigit = False
					
					x += elementlen
				y += 1
		
		print(self.listofnumbers)

	def adjcent(self, x1, y1, x2, y2):
		return abs(x1 - x2) < 2 and abs(y1 - y2) < 2
			
	
	def countNumbers(self):
		self.sum = 0
		for num in self.listofnumbers:
			val = num[0]
			coords = num[1]
			foundajcent = False
			for coord in coords:
				for symbolCoord in self.symbolArr:
					if self.adjcent(coord[0], coord[1], symbolCoord[0], symbolCoord[1]):
						foundajcent = True
						self.sum += val
						break
				if foundajcent:
					break
		print(self.sum)
			

					



	def p1(self):
		print(self.WIDTH, self.HEIGHT)
		self.symbol_dict = {}
		self.makeSymbolDict()
		print(self.symbol_dict)
		self.replaceSymbols()
		self.processNumbers()
		self.countNumbers()
		

p1 = d3(cleanerInput)