import random


def moves(player,enemy): 
    patck  = player.strn - enemy.pdef 
    pspatk = int(player.strn*(player.lv+player.lv*0.1)) - enemy.pdef 
    pmagic = int(player.inte+player.inte*0.1) - enemy.mdef 
    pmsatk = int(pmagic*(player.lv+player.lv*0.1)) - enemy.mdef 
    
    if patck  <=0: patck  = -1
    if pspatk <=0: pspatk = -1
    if pmagic <=0: pmagic = -1
    if pmsatk <=0: pmsatk = -1
    
    eatck  = enemy.strn - player.pdef
    espatk = int(enemy.strn*(enemy.lv+enemy.lv*0.1)) - player.pdef
    emagic = int(enemy.inte+enemy.inte*0.1) - player.mdef 
    emsatk = int(emagic*(enemy.lv+enemy.lv*0.1)) - player.mdef 
    
    if eatck  <=0: eatck  = -1
    if espatk <=0: espatk = -1
    if emagic <=0: emagic = -1
    if emsatk <=0: emsatk = -1

    
    result = "lost"   
    a = player.spd
    b = enemy.spd
    c=a+b
    while player.hp >=0 or enemy.hp >= 0:
        turn = random.randint(1, c)
        if turn <=a:
            t = 1
        else:t = 2
        if t == 1:
            print("player move")
            print("choose move: 1.patk 2.spatk 3.matk 4.smatk 5.fillhp 6.fillmp ")
                
            m=int(input())
            
            if m == 1 :
                
                enemy.hp -= patck
                print(f"player uses normal patk causing {patck} to the enemy")
                
            elif m == 2 :
                if player.mp <9:
                    enemy.hp -= patck
                    print(f"player uses normal patk causing {patck} to the enemy")
                else: 
                    enemy.hp -= pspatk
                    player.mp -= 10
                    print(f"player uses special patk causing {pspatk} to the enemy")
                
            elif m == 3 :
                enemy.hp -= pmagic
                print(f"player uses normal matk causing {pmagic} to the enemy")
            elif m == 4 :
                if player.mp <9:
                    enemy.hp -= pmagic
                    print(f"player uses normal matk causing {pmagic} to the enemy")
                else:
                    enemy.hp -= pmsatk
                    player.mp -= 10
                    print(f"player uses special matk causing {pmsatk} to the enemy")
                
            elif m == 5 :
                
                player.hp += player.wis*2
                player.mp -= player.wis
                print(f"player heal {player.wis} hp using {player.wis} mp")
            elif m == 6 :
                player.mp += player.phy/2
                player.hp -= player.phy
                print(f"player heal {player.phy} mp using {player.phy} hp")
                
                
        elif t == 2:
            print("enemy move")

            
            if enemy.mp>=10:
                if enemy.strn>enemy.inte:
                    player.hp -= espatk
                    print(f"enemy uses special patk causing {espatk} to the player")
                else:
                    player.hp -= emsatk
                    print(f"enemy uses special matk causing {emsatk} to the player")
                enemy.mp -= 10
                
            elif player.hp <= espatk or player.hp <= emsatk:
                if enemy.strn>enemy.inte:
                    player.hp -= eatck
                    print(f"enemy uses normal patk causing {eatck} to the player")
                else:
                    player.hp -= emagic
                    print(f"enemy uses normal matk causing {emagic} to the player")
                    
            elif enemy.mp<10 :
                enemy.mp +=enemy.phy/2
                enemy.hp -= enemy.phy
                print(f"enemy heal {enemy.phy} hp using {enemy.phy} mp")
                
            elif enemy.hp<enemy.hp/2:
                enemy.hp += enemy.wis*2
                enemy.mp -= enemy.wis
                print(f"enemy heal {enemy.wis} hp using {enemy.wis} mp")
                
            else:
                if enemy.strn>enemy.inte:
                    player.hp -= eatck
                    print(f"enemy uses normal patk causing {eatck} to the player")
                else:
                    player.hp -= emagic
                    print(f"enemy uses normal matk causing {emagic} to the player")
                    
        print(f'''
            player hp = {player.hp}  enemy hp = {enemy.hp}
            player mp = {player.mp}  enemy mp = {enemy.mp}''')
        if player.hp>0 and enemy.hp <= 0:
            print("player won")
            result = "won"
            break
        elif player.hp<=0 and enemy.hp >= 0:
            print("player lost")
            break
    return result
            
