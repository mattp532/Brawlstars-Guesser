from random import randrange
file = open("brawl_chars.txt")

class Character:
  def __init__(self, name, role, race, release_year, hypercharge, rarity, gender):
    self.name = name
    self.role = role
    self.race = race
    self.release_year = release_year
    self.hypercharge = hypercharge
    self.rarity = rarity.strip()
    self.gender = gender

def brawler_line_check(brawler_name):
  line_number=0
  file.seek(0)
  for line in file:
    line_number+=1
    line=line.strip()
    parts = line.split(":")
    if brawler_name.lower() == parts[0].lower():
      parts = parts[1:8]
      brawlerList = [brawler.role, brawler.race, brawler.release_year, brawler.hypercharge, brawler.rarity, brawler.gender]
      for x in range(6):
         if brawlerList[x]==parts[x]:
           parts[x]+= u' \u2713'
         else:
           parts[x]+=" X"
      return parts

def check_all_brawlers(brawler_name):
  file.seek(0)
  for line in file:
    parts=line.split(":")
    if brawler_name.lower() == parts[0].lower():
      return True
  return False

def check_guessed_list(Guess, brawlers):
  if Guess in brawlers:
    return True
  else:
    return False
def brawler_guess(round_start, brawlers):
  valid_brawler = False
  in_list=True
  while (valid_brawler == False or in_list==True):
    if round_start ==True:
      Guess = input(f"Guess any Brawler to start:\n")
    else:
      Guess = input(f"Guess any Brawler:\ntype x to give up\n")
    if Guess.lower()=="x" and round_start!=True:
      return Guess
    valid_brawler = check_all_brawlers(Guess)
    in_list = check_guessed_list(Guess, brawlers)
    if valid_brawler == False:
      print("Brawler is not in list. Try again")
    if in_list ==True:
      print("Brawler was already guessed. Try again")

  return(Guess.lower())
play_again=True
rounds= True
count=0
high_score=0
choice=True
while(play_again==True):
  # Randomize Character Number
  char_num = randrange(1, 86)

  # Access Character from line
  file.seek(0)
  for x in range(char_num):
    line = file.readline()
    line = line.strip()
    attribs = line.split(":")

  # assign object attributes to brawler
  brawler = Character(attribs[0], attribs[1], attribs[2], attribs[3], attribs[4], attribs[5], attribs[6])

  round_start = True
  count=0
  wrong_guesses = []
  print("-" * 34)
  print("| Welcome to Brawl Stars guesser |")
  print("-" * 34)
  print(f"Current High Score is {high_score}")
  print("-" * 34)
  rounds=True
  while rounds==True:
    if round_start==True:
     Guess = brawler_guess(True, wrong_guesses)
     round_start=False
    else:
      Guess = brawler_guess(False, wrong_guesses)
    if Guess=="x":
      rounds=False
      print("You have quit the game.")
      count=0
      print(f"Brawler was {brawler.name.upper()}")
    if Guess==brawler.name.lower():
      count+=1
      print("-" * 80)
      print(brawler_line_check(Guess))
      print("-" * 80)
      print(f"{Guess} is correct!\n")
      print(f"You guessed in {count} tries")
      rounds=False
    elif Guess!=brawler.name.lower and Guess!="x":
      print("-" * 80)
      print(brawler_line_check(Guess))
      print("-" * 80)
      wrong_guesses.append(Guess)
      count += 1
  if count<high_score and count>=1:
    high_score=count
    print("New Highscore!")
  choice = input("Do you want to play again?\n")
  if choice.lower() == "yes":
    play_again = True
  else:
    play_again = False