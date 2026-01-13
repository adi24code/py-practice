import random

def print_cards(cards):
    height = len(cards[0])  

    for i in range(height):
        for card in cards:
            print(card[i], end="  ")
        print()

def calculate_score(cards, deck):
    score = 0
    aces = 0

    for card in cards:
        rank = card[:-1]  
        score += deck[card]["value"]
        if rank == "A":
            aces += 1

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


ranks = {
    "A": 11, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10
}

suits = ["♠", "♥", "♦", "♣"]

deck = {}

for r, v in ranks.items():
    for s in suits:
        key = f"{r}{s}"
        deck[key] = {
            "value": v,
            "ascii": [
                " ___ ",
                f"|{r:<2} |",
                f"| {s} |",
                f"|__{r}|"
            ]
        }

availables = list(deck.keys())
your_card=[]
computer_card=[]
random.shuffle(availables)


your_ascii_card=[]
computer_ascii_card=[]
temp_ascii_card=[[" ___ ","|## |","|###|","|_##|"]]


print("Welcome to blackjack")
print("Let's start the game")


for i in range(2):
    your_card.append(random.choice(availables))
    your_ascii_card.append(deck[your_card[i]]['ascii'])
    availables.remove(your_card[i])
    computer_card.append(random.choice(availables))
    computer_ascii_card.append(deck[computer_card[i]]['ascii'])
    availables.remove(computer_card[i])

your_score= calculate_score(your_card, deck)
computer_score=calculate_score(computer_card, deck)
temp_ascii_card.append(computer_ascii_card[0])
print("Computer Score:???")
print_cards(temp_ascii_card)
print(f"your Score:{your_score}")
print_cards(your_ascii_card)


print("Do you want to hit or stand?type 'h' for hit and 's' for stand.")
yourchoice=input("Enter:").lower()

while True:

    if yourchoice=='h':
       your_card.append(random.choice(availables))
       your_ascii_card.append(deck[your_card[-1]]['ascii'])
       availables.remove(your_card[-1])
       your_score= calculate_score(your_card, deck)
    
       if computer_score<17:
          computer_card.append(random.choice(availables))
          computer_ascii_card.append(deck[computer_card[-1]]['ascii'])
          availables.remove(computer_card[-1])
          computer_score=calculate_score(computer_card, deck)
          break

    elif yourchoice=='s':
       if computer_score<17:
          computer_card.append(random.choice(availables))
          computer_ascii_card.append(deck[computer_card[-1]]['ascii'])
          availables.remove(computer_card[-1])
          computer_score=calculate_score(computer_card, deck)
          break
    else:
        print("Do you want to hit or stand?type 'h' for hit and 's' for stand.")
        print("Invalid choice")
        yourchoice=input("Enter:").lower()
        

if your_score>computer_score and your_score<=21:
    print_cards(computer_ascii_card)
    print_cards(your_ascii_card)
    print(f"Computer Score:{computer_score}, your Score:{your_score}")
    print("You Win!!")
elif computer_score>your_score and computer_score<=21:
    print_cards(computer_ascii_card)
    print_cards(your_ascii_card)
    print(f"Computer Score:{computer_score}, your Score:{your_score}")
    print("You Lose!!")
elif your_score>21 and computer_score>21:
    print_cards(computer_ascii_card)
    print_cards(your_ascii_card)
    print(f"Computer Score:{computer_score}, your Score:{your_score}")
    print("It's a Draw!!")
elif your_score>21:
    print_cards(computer_ascii_card)
    print_cards(your_ascii_card)
    print(f"Computer Score:{computer_score}, your Score:{your_score}")
    print("You Lose!!")
elif computer_score>21:
    print_cards(computer_ascii_card)
    print_cards(your_ascii_card)
    print(f"Computer Score:{computer_score}, your Score:{your_score}")
    print("You Win!!")
else:
    pass