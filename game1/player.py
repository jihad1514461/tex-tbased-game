from character import Cheracter



def player_base_stats(name,a):
    #pl = Cheracter(name, 'worage', 140, 140,   7,   7,    7,    7,   7,    3,    3, 1)
    if a == 1:
        pl = Cheracter(name,'worrior', 200, 100,  10,   5,   10,    5,   5,    4,    2, 1)
    elif a == 2 :
        pl = Cheracter(name,   'mage', 100, 200,   5,   5,    5,   10,  10,    2,    4, 1)
    elif a == 3 :
        pl = Cheracter(name,'warlock', 140, 140,   7,   7,    7,    7,   7,    3,    3, 1)
    return pl

#player = player_base_stats()
#player.show()


        