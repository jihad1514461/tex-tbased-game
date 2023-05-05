from player import player_base_stats

def update(player):
    print(f'''update:
          1.phy
          2.str
          3.inte
          4.wis
          5.spd
          6.pdef
          7.mdef
          ''')
    s = int(input())
    if s == 1:
        player.phy +=1
        player.hp  +=19
        
    elif s == 2:
        player.strn += 1
    
    elif s == 3:
        player.inte +=1
        
    elif s == 4:
        player.wis +=1
        player.mp +=15
    
    elif s == 5:
        player.spd +=1
        
    elif s == 6:
        player.pdef +=1
        
    elif s == 7:
        player.mdef +=1
    
    return player
        
    
    
        
    
    
    