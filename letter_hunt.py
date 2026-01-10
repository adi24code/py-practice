import random

words = ['apple','space','house','random','banana', 'chair', 'dog', 'elephant','flower','guitar','ice','nation','python','javascript','money','paper','monkey','coffee']
random_word = random.choice(words)
display = ["_"] * len(random_word)
letters = list(random_word)
lifecount = 7 
chars = []
guessed = set() 
print('''
░█░░░█▀▀░▀█▀░▀█▀░█▀▀░█▀▄░░░█░█░█░█░█▀█░▀█▀
░█░░░█▀▀░░█░░░█░░█▀▀░█▀▄░░░█▀█░█░█░█░█░░█░
░▀▀▀░▀▀▀░░▀░░░▀░░▀▀▀░▀░▀░░░▀░▀░▀▀▀░▀░▀░░▀░
''')
print("🔍 HUNT THE LETTERS! 7 LIVES TO REVEAL THE WORD!")
print(''.join(display))

while lifecount > 0 and len(set(letters)) != len(chars):
    letter = input("Enter a letter: ").lower().strip()
    
    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input! Please enter a single letter.\n You wasted a life.")
        lifecount -= 1
        print(''.join(display))
        print(f"****************************{lifecount}/7 LIVES LEFT****************************")
        continue
    
    if letter in guessed:
        print("Already guessed that!\n You wasted a life.")
        lifecount -= 1
        print(''.join(display))
        print(f"****************************{lifecount}/7 LIVES LEFT****************************")
        continue
    
    guessed.add(letter)
    
    if letter not in random_word:
        lifecount -= 1
        print(''.join(display))
        print(f"****************************{lifecount}/7 LIVES LEFT****************************")
    elif letter in random_word:
        chars.append(letter)
        for i in range(len(random_word)):
            if random_word[i] == letter:
                display[i] = letter
        print(''.join(display))  
        print(f"****************************{lifecount}/7 LIVES LEFT****************************")

if len(set(letters)) == len(chars):
    print(''.join(display))
    print("You Win")
else:
    print(f"You Lose. The word was '{random_word}'.\nBetter Luck Next Time.")
