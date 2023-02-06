import random

print("==== Rock, Paper, Scissor Game ====")

def playAgain():
  play_again = input('\n\rDo you want to play again [y/n]: ')
  
  while True:
    if play_again == 'y' or play_again == 'yes':
      return rock_paper_scissor()
    else:
      print("See you next time!")
      break


def rock_paper_scissor():
  generalChoices = ["rock", "paper", "scissor"]
  userChoice = input("\n\rChoose Rock, Paper or Scissors: ").lower()
  computerChoice = random.choice(generalChoices)  
  print(f"You: {userChoice}, Computer: {computerChoice}")
  
  while True:
    if userChoice == computerChoice:
      print("It's a tie!")
      playAgain()
      break
    if userChoice == 'rock' and computerChoice == 'scissor':
      print('You won!')
      playAgain()
      break
    elif userChoice == 'scissor' and computerChoice == 'paper':
      print('You won!')
      playAgain()
      break
    elif userChoice == 'paper' and computerChoice == 'rock':
      print('You won!')
      playAgain()
      break
    else:
      print('Computer won!')
      playAgain()
      break
rock_paper_scissor()