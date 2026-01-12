#Prints a poker-style ASCII card hand by vertically aligning multi-line card representations from a standard 52-card deck.
#Prints 52 poker-style ASCII cards
def print_hand(cards):
    height = len(cards[0])  

    for i in range(height):
        for card in cards:
            print(card[i], end="  ")
        print()

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♠", "♥", "♦", "♣"]
cards52=[]
for r in ranks:
    for s in suits:
        if r=="10":
            cards52.append( [
                " ___ ",
                f"|{r:<2} |",
                f"| {s} |",
                f"|_{r}|"
            ]
        )
        else:
            
            cards52.append( [
                " ___ ",
                f"|{r:<2} |",
                f"| {s} |",
                f"|__{r}|"
            ]
        )

for i in range(0,52,4):
    print_hand(cards52[i:i+4])
    print()

