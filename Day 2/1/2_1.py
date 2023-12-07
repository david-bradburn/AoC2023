#################################################################
###### https://adventofcode.com/2022/day/2 #######################
#################################################################

file = "input.txt"

DAY_NO = "2"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = [i.strip("\n") for i in rawInput]
# print(cleanerInput)

class ColourGame():
  def __init__(self, input) -> None:
    self.input = input
    self.maxColours_dict = {"r": 12, "g": 13, "b": 14}
    self.gamedict = {}
    self.sumofpossiblegames = 0
    self.processInput()

    print(self.sumofpossiblegames)

  def processInput(self):
    cleaner = [i.split(":") for i in self.input]
    # print(cleaner)
    for game in cleaner:
      turns = game[1].split(";")
      match game[0].split(" "):
        case ["Game", gameID]:
          game_ID = int(gameID)
      

      impossibleFlag = False
      for turn in turns:
        temp = turn.split(",")
        # print(temp)

        for ball in temp:
          clean_balls = ball.strip()

          match clean_balls.split(" "):
            case [number_of_red_balls, "red"]:
              red = int(number_of_red_balls)
              if red > self.maxColours_dict["r"]:
                 impossibleFlag = True
            case [number_of_green_balls, "green"]:
              green = int(number_of_green_balls)
              if green > self.maxColours_dict["g"]:
                 impossibleFlag = True
            case [number_of_blue_balls, "blue"]:
              blue = int(number_of_blue_balls)
              if blue > self.maxColours_dict["b"]:
                 impossibleFlag = True
            case _:
                raise Exception
            
          # print(clean_balls)

        if impossibleFlag:
          break
      if impossibleFlag:
          continue
      
      self.sumofpossiblegames += game_ID
      print(game_ID)
      

      
      
    # gameStr, turns = self

p1 = ColourGame(cleanerInput)