def start_story():
    pass

def s01():
    print(f"wellcome adventuarer. the kingdom is in a denger the king hope that you will bring the great artifact that can save the kingdom")

def s02():
    print(f''' your name: ''')
    a = input("")
    return a 

def s03():
    print(f''' your class?
          1. warrior
          2. Mage
          3. Battle Mage
          ''')
    try:
        clss = int(input(""))
    except:
        s03()
    return clss
    
def s04(player):
    print(f'''{player.name} sets out on a journey to find a powerful artifact that can save the kingdom ''')

def s05(player):
    print(f'''{player.name} faces challenges along the way ''')

def s06(player):
    print(f'''there are various monster to fight''')

def fight(enemy):
    print(f'''{enemy.name} is infront. Do you fight?''')
    try:
        yn = int(input("1.yes \n2.no \n  "))
    except:
        s06(enemy)
    return yn
    
def s07(player):
    print(f'''{player.name} encounters a mysterious guide who offers aid and advice ''')
    try:
        yn = int(input("1.yes \n2.no \n  "))
    except:
        s07()
    if yn == 1:
        print(f"{player.name} fill he is full of power")
    else: print(f"{player.name} refuses and goes his own way")
    return yn


def s08(player):
    print(f'''in a tevarn {player.name} learns about the artifact's location and how to acquire it  ''')

def s09(player):
    print(f'''{player.name} arrive at the entrance to a perilous dungeon where the artifact is hidden  ''')

def s10(player):
    print(f'''{player.name} solve riddles ''')

def s11(player):
    print(f'''{player.name} finds the artifact and battles the final guardian to claim it''')

def s12(player):
    print(f'''{player.name} must escape the dungeon, which is now collapsing  ''')

def s13(player):
    print(f'''{player.name} is pursued by enemy forces who want to claim the artifact for their own purposes  ''')

def s14(player):
    print(f'''{player.name} must outrun or defeat enemy forces while making his escape  ''')

def s15(player):
    print(f'''{player.name} meets allies who offer assistance and help him reach his destination  ''')

def s16(player):
    print(f'''{player.name} learns of a plot to assassinate the king and must race against time to stop the assassination  ''')

def s17(player):
    print(f'''{player.name} confronts the assassin and his minions  ''')

def s18(player):
    print(f'''{player.name} defeats the assassin and saves the king  ''')

def s19(player):
    print(f'''
    The kingdom is grateful, and the {player.name} is hailed as a hero 
    {player.name} is invited to a grand feast in his honor 
    {player.name} meets a mysterious figure who warns him of an impending danger 
    {player.name} learns of an ancient prophecy that foretells the rise of a great evil 
    {player.name} sets out on a new journey to prevent the evil from rising  ''')
    
# Branch 1: {player.name} fails to find the artifact
def b1_1(player):
    print(f'''{player.name} is unable to solve the riddles, bypass the traps, or defeat the guardians in the dungeon  ''')

def b1_2(player):
    print(f'''{player.name} fails to find the artifact and returns home empty-handed  ''')

#Branch 2: {player.name} is betrayed by an ally
def b2_1(player):
    print(f'''{player.name}'s ally turns on him and steals the artifact ''')

def b2_2(player):
    print(f'''{player.name} is forced to fight his former ally to retrieve the artifact ''')

def b2_3(player):
    print(f'''{player.name} defeats his former ally and reclaims the artifact  ''')

def b2_4(player):
    print(f'''{player.name} returns home with the artifact and is hailed as a hero  ''')

#Branch 3: {player.name} sacrifices himself to save the kingdom
def b3_1(player):
    print(f'''{player.name} returns home with the artifact, but discovers that a powerful enemy has invaded the kingdom  ''')

def b3_2(player):
    print(f'''{player.name} realizes that the artifact can only be used to defeat the enemy if he sacrifices himself ''')

def b3_3(player):
    print(f'''{player.name} makes the ultimate sacrifice, using the artifact to defeat the enemy and save the kingdom  ''')

def b3_4(player):
    print(f'''The people of the kingdom mourn the loss of their hero, but celebrate his sacrifice and legacy  ''')

#Branch 4: {player.name} discovers a greater threat than the one he set out to face
def b4_1(player):
    print(f'''{player.name} returns home with the artifact, but discovers that the real threat to the kingdom is not the one he set out to face  ''')

def b4_2(player):
    print(f'''{player.name} must convince the kingdom's leaders to take action against the new threat  ''')

def b4_3(player):
    print(f'''The kingdom is saved, but the {player.name}'s reputation is tarnished for not fulfilling the original mission ''')

#Branch 5: {player.name} falls in love and chooses to stay in a new land
def b5_1(player):
    print(f'''{player.name} falls in love with a local and decides to stay in the new land  ''')

def b5_2(player):
    print(f'''{player.name} abandons his original mission and starts a new life with his new love  ''')

#Branch 6: {player.name} becomes corrupted by the power of the artifact
def b6_1(player):
    print(f'''{player.name} returns home with the artifact, but the power of the artifact corrupts him  ''')

def b6_2(player):
    print(f'''{player.name} becomes a tyrant and the people of the kingdom suffer under his rule  ''')

def b6_3(player):
    print(f'''The people must overthrow the corrupted {player.name} to restore peace and order  ''')

