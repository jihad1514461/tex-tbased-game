from character import Cheracter
from random import randint

def monster(name,clss,i):
    if name == "slime":
        if clss == 'worrior': #                                                  p     m           dp    md
            enemy   =      Cheracter("slime"  ,'worrior', 100, 100,   5,   5, 5+i*2,     5,   5,    2,    2,    i)
        elif clss == 'mage':
            enemy   =      Cheracter("slime"  ,   'mage', 100, 100,   5,   5,     5, 5+i*2,   5,    2,    2,    i)
        else: 
            enemy   =      Cheracter("slime"  , 'warlock', 100, 100,   5,   5,   5+i,   5+i,   5,    2,    2,    i)
    elif name == "goblin":
        if clss == 'worrior': #                                                  p     m
            enemy   =      Cheracter("goblin" ,'worrior', 119, 100,   6,   5, 5+i*2,     5,   5,    3,    2,    i)
        elif clss == 'mage':
            enemy   =      Cheracter("goblin" ,   'mage', 119, 100,   6,   5,     5, 5+i*2,   5,    3,    2,    i)
        else: 
            enemy   =      Cheracter("goblin" , 'warlock', 119, 100,   6,   5,   5+i,   5+i,   5,    3,    2,    i)   

    elif name == "spider":
        if clss == 'worrior': #                                                  p     m           dp    md
            enemy   =      Cheracter("spider"  ,'worrior', 100, 115,   5,   6, 5+i*2,     5,   5,    2,    3,    i)
        elif clss == 'mage':
            enemy   =      Cheracter("spider"  ,   'mage', 100, 115,   5,   6,     5, 5+i*2,   5,    2,    3,    i)
        else: 
            enemy   =      Cheracter("spider"  , 'warlock', 100, 115,   5,   6,   5+i,   5+i,   5,    2,    3,    i)
        
    
    return enemy


def monster_list(rank,lv):
    mn1=["slime","goblin","spider"]
    mc=["worrior","mage","warlock"]
    mon=randint(0,len(mn1)-1)
    moc = randint(0,2) 
    monsters_name=mn1[mon]
    monsters_class= mc[moc]
    return monsters_name,monsters_class
        