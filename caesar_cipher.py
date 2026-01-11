import string
print(''''
░█▀▀░█▀█░█▀▀░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█▀█░█░█░█▀▀░█▀▄
░█░░░█▀█░█▀▀░▀▀█░█▀█░█▀▄░░░█░░░░█░░█▀▀░█▀█░█▀▀░█▀▄
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░░▀░░▀░░░▀░▀░▀▀▀░▀░▀   
      ''')
def caesar(text, shift, choice):
    result = ""
    direction = 1 if choice == 'encode' else -1
    for char in text:
        if char not in string.ascii_letters:
            result += char
            continue
        elif char.islower():
            pos = string.ascii_lowercase.index(char)
            new_pos = (pos + direction * shift) % 26
            result += string.ascii_lowercase[new_pos]
        else: 
            pos = string.ascii_uppercase.index(char)
            new_pos = (pos + direction * shift) % 26
            result += string.ascii_uppercase[new_pos]
    mode_str = "Encoded" if choice == 'encode' else "Decoded"
    print(f"{mode_str} text: {result}")
print("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
choice=input().lower()
if choice=='encode' or choice=='decode':
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, choice)  
else:
    print("Invalid choice")


