class Cheracter:
      def __init__(self, name,   classs,  hp,  mp, phy, spd, strn, inte, wis, pdef, mdef, lv):
        self.name   = name
        self.classs = classs
        self.hp     = hp 
        self.mp     = mp 
        self.phy    = phy 
        self.spd    = spd 
        self.strn   = strn
        self.inte   = inte 
        self.wis    = wis 
        self.pdef   = pdef
        self.mdef   = mdef
        self.lv     = lv
        
      def show(self):
            print(f'''
                  name = {self.name}
                  classs={self.classs}
                  hp   = {self.hp}
                  mp   = {self.mp}
                  phy  = {self.phy}
                  strn = {self.strn}
                  inte = {self.inte}
                  wis  = {self.wis}
                  pdef = {self.pdef}
                  mdef = {self.mdef}
                  spd  = {self.spd}
                  lv   = {self.lv}
                  
                  ''')
            
        