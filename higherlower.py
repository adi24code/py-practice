import random

logo ='''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/        

      '''

vs='''
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

'''
data = [
    {'name': 'Cristiano Ronaldo', 'followers': 670000000, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Lionel Messi', 'followers': 511000000, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'Selena Gomez', 'followers': 416000000, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Kylie Jenner', 'followers': 391000000, 'description': 'Media personality', 'country': 'United States'},
    {'name': 'Dwayne Johnson', 'followers': 391000000, 'description': 'Actor and wrestler', 'country': 'United States'},
    {'name': 'Ariana Grande', 'followers': 372000000, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Kim Kardashian', 'followers': 354000000, 'description': 'Media personality', 'country': 'United States'},
    {'name': 'Beyoncé', 'followers': 308000000, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Khloé Kardashian', 'followers': 300000000, 'description': 'Media personality', 'country': 'United States'},
    {'name': 'Justin Bieber', 'followers': 292000000, 'description': 'Musician', 'country': 'Canada'},
    {'name': 'Kendall Jenner', 'followers': 285000000, 'description': 'Media personality', 'country': 'United States'},
    {'name': 'Taylor Swift', 'followers': 281000000, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Virat Kohli', 'followers': 274000000, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Jennifer Lopez', 'followers': 246000000, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Neymar Jr', 'followers': 231000000, 'description': 'Footballer', 'country': 'Brazil'},
    {'name': 'Kourtney Kardashian', 'followers': 216000000, 'description': 'Media personality', 'country': 'United States'},
    {'name': 'Miley Cyrus', 'followers': 211000000, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Katy Perry', 'followers': 201000000, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Zendaya', 'followers': 176000000, 'description': 'Actress and singer', 'country': 'United States'},
    {'name': 'Kevin Hart', 'followers': 176000000, 'description': 'Comedian and actor', 'country': 'United States'},
    {'name': 'Cardi B', 'followers': 164000000, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'LeBron James', 'followers': 157000000, 'description': 'Basketball player', 'country': 'United States'},
    {'name': 'Demi Lovato', 'followers': 152000000, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Rihanna', 'followers': 149000000, 'description': 'Musician', 'country': 'Barbados'}
]

random.shuffle(data)
A=random.choice(data)
B=random.choice(data)
your_score=0
r_str=''
while A==B:
    B=random.choice(data)

while True:
    print(logo)
    print(f"{r_str}Current score: {your_score}")
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    your_choice=input("Who has more followers? Type 'A' or 'B':").upper()
    if your_choice=='A':
        if A['followers']>B['followers']:
            your_score+=1
            print(logo)
            r_str="You're right!"
            A=B
            B=random.choice(data)
            if A==B:
                B=random.choice(data)
        else:
            print(f"Sorry, that's wrong. Final score: {your_score}")
            break   
    elif your_choice=='B':
        if B['followers']>A['followers']:
            your_score+=1
            print(logo)
            r_str="You're right!"
            A=B
            B=random.choice(data)
            if A==B:
                B=random.choice(data)
        else:
            print(f"Sorry, that's wrong. Final score: {your_score}")
            break
    else:
        print("Invalid choice")
   