print(r'''

                                   .-----.
                                 .'       `.
                                :      ^v^  :
                                :           :
                                '           '
                 |~        www   `.       .'
                /.\       /#^^\_   `-/\--'
               /#  \     /#%    \   /# \
              /#%   \   /#%______\ /#%__\
             /#%     \   |= I I ||  |- |
             ~~|~~~|~~   |_=_-__|'  |[]|
               |[] |_______\__|/_ _ |= |`.
        ^V^    |-  /= __   __    /-\|= | :;
               |= /- /\/  /\/   /=- \.-' :;
               | /_.=========._/_.-._\  .:'
               |= |-.'.- .'.- |  /|\ |.:'
               \  |=|:|= |:| =| |~|~||'|
                |~|-|:| -|:|  |-|~|~||=|      ^V^
                |=|=|:|- |:|- | |~|~|| |
                | |-_~__=_~__=|_^^^^^|/___
                |-(=-=-=-=-=-(|=====/=_-=/\
                | |=_-= _=- _=| -_=/=_-_/__\
                | |- _ =_-  _-|=_- |]#| I II
                |=|_/ \_-_= - |- = |]#| I II
                | /  _/ \. -_=| =__|]!!!I_II!!
               _|/-'/  ` \_/ \|/' _ ^^^^`.==_^.
             _/  _/`-./`-; `-.\_ / \_'\`. `. ===`.
            / .-'  __/_   `.   _/.' .-' `-. ; ====;\
           /. jgs./    \ `. \ / -  /  .-'.' ====='  >
          /  \  /  .-' `--.  / .' /  `-.' ======.' /
''')

first_choice=input("“You enter a haunted house. Do you go upstairs or into the basement?”")
if first_choice.lower()=="upstairs":
    second_choice=input("Next choice is “Enter the bedroom or the attic?”")
    if second_choice.lower()=="bedroom":
        print("You see a door and a hidden passage behind the wardrobe\n")
        next_choice=input("you have a choice to follow hidden passage or the door ")
        if next_choice.lower()=="door":
            print(r'''

                                              _
                              /\              )\
                _           __)_)__        .'`--`'.
                )\_      .-'._'-'_.'-.    /  ^  ^  \
             .'`---`'. .'.' /o\'/o\ '.'.  \ \/\/\/ /
            /  <> <>  \ : ._:  0  :_. : \  '------'       _J_
            |    A    |:   \\/\_/\//   : |     _/)_    .'`---`'.
            \  <\_/>  / :  :\/\_/\/:  : /   .'`----`'./.'0\ 0\  \
           _?_._`"`_.'`'-:__:__:__:__:-'   /.'<\   /> \:   o    |
        .'`---`'.``  _/(              /\   |:,___A___,|' V===V  /
       /.'a . a  \.'`---`'.        __(_(__ \' \_____/ /'._____.'
       |:  ___   /.'/\ /\  \    .-'._'-'_.'-:.______.' _?_
       \'  \_/   |:   ^    |  .'.' (o\'/o) '.'.     .'`"""`'.
        '._____.'\' 'vvv'  / / :_/_:  A  :_\_: \   /   ^.^   \
                  '.__.__.' | :   \'=...='/   : |  \  `===`  /
               jgs           \ :  :'.___.':  : /    `-------`
                              '-:__:__:__:__:-'
                  
                        G A M E   O V E R
                ''')
            print("\nGHOST!!!!..\n YOU LOSE!!!")
        elif next_choice.lower()=="passage":
            print("You hanage to escape\n")
            print("YOU WIN!!!")
    elif second_choice.lower()=="attic":
        print(r'''
           ________________________
          /                       /|
         /      CURSED MIRROR    / |
        /_______________________/  |
        |  .-"""""""""""""""-.  |  |
        | /  _  _   _  _    / |  | |
        | | |_| |_| |_| |  |  |  | |
        | |   _________   |  |  | |
        | |  /  ___    \  |  |  | |
        | | |  (   )    | |  |  | |
        | |  \  ---   /  |  |  | |
        | |   `-.___-'   |  |  | |
        | |    (  * )    |  |  | |
        | |     \_/      |  |  | |
        | |   YOUR FACE  |  |  | |
        | |   TWISTS AND |  |  | |
        | |   VANISHES…  |  |  | |
        | |______________|  |  | |
        |/__________________| /  /
         \____________________/ /

          G A M E   O V E R
''')
elif first_choice.lower()=="basement":
    third_choice=input("“Turn on the light or walk in the dark?”")
    if third_choice.lower()=="light":   
        print("You find a hidden passage\n")
        print("YOU WIN!!!")
    elif third_choice.lower()=="dark":
        print(r'''
                 _..-----._
              .-`  _---_   `-.
            .'   .'     `.    `.
           /    /  _   _  \     \
          /    /  (_) (_)  \     \
         |    |    ___      |    |
         |    |   /   \     |    |
         |    |   \___/     |    |
         |    |             |    |
         |    |             |    |
         |    |             |    |
         |    |             |    |
          \   |   .-"""-.   |   /
           `\ |  /  .-.  \  | /`
             \|  |  | |  |  |/
              |  |  | |  |  |
              |  |  | |  |  |
          ____|__|__|_|__|__|____
       .-`          P I T         `-.
     .'   You trip and fall into     `.
    /       the darkness below...      \
   /____________________________________\

      G   A   M   E       O   V   E   R
''')
