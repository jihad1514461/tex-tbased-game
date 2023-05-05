from monster import monster_list,monster
from battle_moves import moves
from update import update
import copy


def progressing(player,count,rank,lv):
    battleplayer =copy.deepcopy(player) 
    name,clss=monster_list(rank,lv)
    enemy=monster(name,clss,lv)
    enemy.show()
    l = [3,5,7,9]
    status = moves(battleplayer,enemy)
    if status== "won":
        count+=1
    for i in l:
        if count == i:
            count = 0
            l.remove(i)
            player.show() 
            for i in range(5):    
                player = update(player)
                player.show()
    return count



