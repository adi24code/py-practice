import random

def rock_paper_scissors(n):
    if n==0:
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''')
    elif n==1:
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    elif n==2:
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

''')
        
print(r'''


██████████████████████████
█▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄███
██─▄─▄█─██─█─███▀██─▄▀████
▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
█████████████████████████████████
█▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀███
██─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
██████████████████████████████████████████████
█─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀█─▄▄▄▄█
█▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
''')
random_integer = random.randint(0, 2)
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
user_choice=int(input(" Enter your choice:"))
if user_choice in [0,1,2]:
    print("You choose:")
    rock_paper_scissors(user_choice)
    print("Computer choose:")
    rock_paper_scissors(random_integer)
    
if user_choice==0 and random_integer==1:
    print("You Lose")  
elif user_choice==0 and random_integer==2:
    print("You Win")
elif user_choice==1 and random_integer==0:
    print("You Win")  
elif user_choice==1 and random_integer==2:
    print("You Lose")
elif user_choice==2 and random_integer==0:
    print("You Lose")  
elif user_choice==2 and random_integer==1:
    print("You win")  
elif user_choice==random_integer:
    print("It's a Drow")  
else:
    print("Invalid choice!")
    

    
