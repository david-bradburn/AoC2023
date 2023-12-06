#################################################################
###### https://adventofcode.com/2022/day/2 #######################
#################################################################

file = "test.txt"

DAY_NO = "2"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = [i.strip("\n") for i in rawInput]
print(cleanerInput)

class ColourGame():
  def __init__(self, input) -> None:
    self.input = input
    self.maxColours_dict = {"r": 12, "g": 13, "b": 14}
