from story import *
from player import player_base_stats
from copy import deepcopy
from battle import progressing
from update import update
from riddles import riddles
def starts(): 
 
    count = 0
    start_story()
    s01()
    name = s02()
    classs = s03()
    player0 = player_base_stats(name,classs)
    player = deepcopy(player0)
    player.show()
    s04(player)
    s05(player)
    s06(player)
    rank=1
    count = progressing(player,count,rank,1)
    s06(player)
    count = progressing(player,count,rank,1)
    s06(player)
    count = progressing(player,count,rank,1)
    
    yn=s07(player)
    if yn == 1:
        player = update(player)
    
    s08(player)
    s09(player)
    riddles_answered = riddles()
    if riddles_answered == 4:
        player = update(player)
    s06(player)
    count = progressing(player,count,rank,2)
    s10(player)   
    s11(player)
    s12(player)
    s13(player)
    s14(player)
    s06(player)
    count = progressing(player,count,rank,3)
    s16(player)
    riddles_answered = riddles()
    if riddles_answered >= 4:
        player = update(player)
    s17(player)
    count = progressing(player,count,rank,4)
    s18(player)
    s19(player)
    
    

    

