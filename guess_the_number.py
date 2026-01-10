import random

number=random.randint(1,100)
print('''
░█▀▀░█░█░█▀▀░█▀▀░█▀▀░░░▀█▀░█░█░█▀▀░░░█▀█░█░█░█▄█░█▀▄░█▀▀░█▀▄
░█░█░█░█░█▀▀░▀▀█░▀▀█░░░░█░░█▀█░█▀▀░░░█░█░█░█░█░█░█▀▄░█▀▀░█▀▄
░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░░░▀░░▀░▀░▀▀▀░░░▀░▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀
      ''')
print("Guess the number between 1 to 100 in 7 turns")
user_input=int(input("Enter you Guess:"))
turns=7
while user_input!=number and turns>0:
    if user_input<number:
        print(f"Number{user_input} is Lower")
        turns-=1
        print(f"****************************{turns}/7 ATTEMPTS LEFT****************************")
        user_input=int(input("Enter you Guess:"))
    elif user_input>number:
         print(f"Number{user_input} is High")
         turns-=1
         print(f"****************************{turns}/7 ATTEMPTS LEFT****************************")
         user_input=int(input("Enter you Guess:"))
    else:
        pass
if turns==0 and user_input!=number:
    print(f"You Lose,The Number was {number}.\n Better Luck Next Time.")
elif user_input==number:
    print(f"It took you {7-turns} Attempts to guess the number, which was {number}.")
else:
    pass
