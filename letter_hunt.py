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

'''
import random

words=['apple','space','house','random','banana', 'chair', 'dog', 'elephant','flower','guitar','ice','nation','python','javascript','money','paper','monkey','coffee']
random_word=random.choice(words)
#print(random_word)
#print(len(random_word))
display=[]
for i in range(len(random_word)):
    display.append("_")

#print(type(random_word))
letters=list(random_word)
#print(letters)
lifecount=7 
chars=[]
print("Guess the letters in the word, you have 7 lives")
print(''.join(display))
letter=input("Enter a letter:")


while lifecount>0 and len(set(letters))!=len(chars):
    if letter not in random_word:
        lifecount-=1
        print(''.join(display))
        print(f"****************************{lifecount}/7 LIVES LEFT****************************")
        #print(letters, chars)
        letter=input("Enter a letter:")
       
    elif letter in random_word:
        chars.append(letter)
        for i in range(len(random_word)):
            if letter==random_word[i]:
                display[i]=letter
        if "_" in display:
           print(''.join(display))
           print(f"****************************{lifecount}/7 LIVES LEFT****************************") 
        #print(letters, chars)
           letter=input("Enter a letter:")
           
if len(set(letters))==len(chars):
    print(''.join(display))
    print("You Win")
else:
    print("You Lose. \n Better Luck Next Time.")

░█▀▀░█▀█░█▀▀░█▀█░█▀█░░░█▀▀░█▀█░█▀▀░█▀█░█▀▀░░░█▀█░█▀█░█▀█░█▀█░█▀█░█▀█
░█░░░█░█░█░░░█░█░█░█░░░█░░░█░█░█░░░█░█░█░█░░░█░█░█░█░█░█░█░█░█░█░█░█
░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀
Usage in your game:

python
print(letter_hunt_ascii)
print("🔍 HUNT THE LETTERS! 7 LIVES TO REVEAL THE WORD!")
Features:

LETTER HUNT clearly readable in block letters

Perfectly matches your reference's block character style

3 lines, console-friendly width (~70 chars)

Professional for your letter_hunt.py GitHub project

Copy-paste directly into your game file! 🎯





Download the Perplexity app
+1 
Scan QR code






'''
