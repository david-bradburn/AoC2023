#################################################################
###### https://adventofcode.com/2022/day/1 #######################
#################################################################

import re

file = "input.txt"

DAY_NO = "1"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanInput = []
for i in rawInput:
  cleanInput.append(i.strip("\n"))

# print(cleanInput)

# number_word_dict = {1: "one"}

number_word_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

sum = 0
for line in cleanInput:
  index_dict = {}
  for index, char in enumerate(line):
    if char.isdigit():
      if index in index_dict:
        raise Exception
      else:
        index_dict[index] = char
  print(index_dict)
  for num in number_word_dict.keys():
    num_index_arr = [m.start() for m in re.finditer(num, line)]
    num_index = line.find(num)
    print(num, num_index_arr)
    if len(num_index_arr):
      for found_index in num_index_arr:
        if found_index in index_dict:
          raise Exception
        else:
          index_dict[found_index] = number_word_dict[num]

  # print(index_dict)
  print(line)
  minindex = min(index_dict.keys())
  firstval = index_dict[minindex]
  maxindex = max(index_dict.keys())
  lastval  = index_dict[maxindex]

  print(f"{firstval} {lastval}")
  val = int(firstval + lastval)
  print(val)
  # print(val)
  sum += val

print(sum)
