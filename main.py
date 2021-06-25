print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

road= input("You are at a cross road choose which way you want to go? Type left or right \n").lower()
if road == "left":
  water= input("You are in front of a lake. Do you swim or wait? Type swim or wait \n").lower()
  if water == "wait":
    door = input("You wait for the lake to dry up and find three doors at the bottom. Choose which one to open. Type yellow, blue or red\n").lower()
    if door == "red":
      print("The door you opened takes you too a room full of hungry lions. You died.")
      print('''
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/   jgs                              \_)
  ''')
    elif door == "yellow":
      print("You have found the pirate treasure! You win!")
      print('''            clap                                                 
                                          clap                           
                                                                         
                         Clap      clap                                  
                  clap                                                   
          clap              clap    clap      Clap                       
                      clap                                               
                  clap       clap         clap                           
                          ,         clap                                 
                 clap   clap   Clap        clap                          
           clap                 .  \  `                                  
                  Clap   \ ( (\  ) /                                     
                       `  ` / _\      ,                                  
                            \(")                                         
                  ___    .-  )=|                                         
                 (`  ') ' _  /'|                                         
                 |-n___n '  (/\|                                         
  a:f____________|_L___J__ <   L _______________________    ''')

    elif door == "blue":
      print("You don't find the treasure, but you find a dog. At least you have a buddy. Game over....")
      print('''  ,--.
                          _/ <`-'
                      ,-.' \--\_
                     ((`-.__\   )
                      \`'    @ (_
                      (        (_)
                     ,'`-._(`-._/
                  ,-'    )&&) ))
               ,-'      /&&&%-'
             ,' __  ,- {&&&&/
            / ,'  \|   |\&&'\
           (       |   |' \  `--.
       (%--'\   ,--.\   `-.`-._)))
        `---'`-/__)))`-._))) ''') 
  else:
    print("You looked a trout in a funny way and die a watery death. Game Over.") 
    print('''
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/   jgs                              \_)
  ''')
else:
  print("Wrong way! you find a pirate and he stabs you in the belly. Game Over.")
  print('''
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/   jgs                              \_)
  ''')
