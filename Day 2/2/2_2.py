#################################################################
###### https://adventofcode.com/2022/day/2 #######################
#################################################################

file = "test.txt"

DAY_NO = "2"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()