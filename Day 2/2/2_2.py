#################################################################
###### https://adventofcode.com/2022/day/2 #######################
#################################################################

file = "input.txt"

DAY_NO = "2"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = [i.strip("\n") for i in rawInput]
# print(cleanerInput)

class ColourGame():
  def __init__(self, input) -> None:
    self.input = input
    # self.maxColours_dict = {"r": 12, "g": 13, "b": 14}
    self.gamedict = {}
    self.sumofpossiblegames = 0
    self.processInput()

    print(self.sumofpossiblegames)

  def processInput(self):
    cleaner = [i.split(":") for i in self.input]
    # print(cleaner)
    for game in cleaner:
      maxballs = {"r": 0, "g": 0, "b": 0 }
      
      turns = game[1].split(";")
      for turn in turns:
        temp = turn.split(",")

        for ball in temp:
          clean_balls = ball.strip()

          match clean_balls.split(" "):
             
            case [number_of_red_balls, "red"]:
              red = int(number_of_red_balls)
              if red > maxballs["r"]:
                maxballs["r"] = red
                 
            case [number_of_green_balls, "green"]:
              green = int(number_of_green_balls)
              if green > maxballs["g"]:
                maxballs["g"] = green
                 
            case [number_of_blue_balls, "blue"]:
              blue = int(number_of_blue_balls)
              if blue > maxballs["b"]:
                maxballs["b"] = blue
            case _:
                raise Exception
            
          # print(clean_balls)

      productofballs = maxballs["r"] * maxballs["g"] * maxballs["b"]
      self.sumofpossiblegames += productofballs
    #   print(game_ID)
      

      
      
    # gameStr, turns = self

p1 = ColourGame(cleanerInput)