#################################################################
###### https://adventofcode.com/2022/day/4 #######################
#################################################################

file = "input.txt"

DAY_NO = "4"
PART = "2"

import numpy as np
import math

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()
	
cleanerInput = [i.strip() for i in rawInput]
# print(cleanerInput)

class card():
	def __init__(self, cleanerInput) -> None:
		self.input = cleanerInput
		self.numberOfCards = len(self.input)
		self.process()
		self.scoreArr = []
		self.cal()
		# print(self.total)
		self.createMoreCard()
		self.findtotalscore()


	def process(self):
		self.cardData = []
		for card in self.input:
			tempData = card.split(":")[1].split("|")
			givenNumbers = tempData[0].strip()
			winningNumbers = tempData[1].strip()
			# print(f"{givenNumbers} | {winningNumbers}")

			splitnum = givenNumbers.split(" ")
			# print(splitnum)
			splitWin = winningNumbers.split(" ")
			# print(splitWin)
			tempgivenArr = []
			tempWinningArr = []
			for num in splitnum:
				a = num.strip()
				if not a.isdigit():
					continue
				tempgivenArr.append(int(a))
			
			for num in splitWin:
				a = num.strip()
				if not a.isdigit():
					continue
				tempWinningArr.append(int(a))
			
			# print(tempgivenArr, tempWinningArr)
			self.cardData.append([tempgivenArr, tempWinningArr])

	def cal(self):
		for index, card in enumerate(self.cardData):
			tempscore = 0
			notFirstMatchingNum = False
			for givenNum in card[0]:
				if givenNum in card[1]:
					if notFirstMatchingNum:
						tempscore *= 2
					else:
						tempscore = 1
						notFirstMatchingNum = True
			# print(f"card {index+1}: {tempscore}")
			self.scoreArr.append(tempscore)

	def createMoreCard(self):
		self.numberOfCardsArr = np.ones(self.numberOfCards, dtype=int)
		# print(numberOfCards)
		for index, numcard in enumerate(self.numberOfCardsArr):
			cardscore = self.scoreArr[index]
			try:
				numberOfExtraCards = int(math.log2(cardscore)) + 1
			except ValueError:
				continue
			print(f"Card {numcard}, Index {index}, Score {cardscore}, Extra Cards: {numberOfExtraCards}")
			if cardscore == 0:
				continue
			else:
				for i in range(index + 1, index + 1 + numberOfExtraCards):
					self.numberOfCardsArr[i] += numcard

		total = 0
		for card in self.numberOfCardsArr:
			total += card
		print(total)
	
	def findtotalscore(self):
		self.total = 0
		for index, numcard in enumerate(self.numberOfCardsArr):
			self.total += numcard * self.scoreArr[index]
		print(self.total)




p1 = card(cleanerInput)