import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Saved the images in a list and stored it in a variablle called images
images = [rock, paper, scissors]

#an input where by user will emter the the infomation needed
user_choice = int(input("Waht do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

#using an if statement to see if the user will type the wrong number or the right one 
#Here indicating that if the user type's 3 or more
#It will then kill the game
if user_choice >= 3 or user_choice < 0:
  print('You typed an invalid numbeer, you lose')
else:
  print(images[user_choice])

  #This makes the computer get a random number from 1-3 but in coding is 0-2 as an int
  #It print the image that coresponds to either rock paper or scissors
  computer_choice = random.randint(0, 2)
  print("Computer choice:")
  print(images[computer_choice])

  
  #if statements to identy if the user picks rock and the computer picks sciaaors
  #the user wins
  if user_choice == 0 and computer_choice == 2:
    print('You Won!')

  #if the computer picks rock and the user picks seciors
  #the computer wins
    
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
    
  elif computer_choice > user_choice:
    print("You lose")
    
  elif user_choice > computer_choice:
    print("You win")
    
  elif user_choice == computer_choice:
    print("It is a draw")
    
  e

  
  
    
