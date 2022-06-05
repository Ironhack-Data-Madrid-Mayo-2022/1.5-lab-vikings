
# Soldier


class Soldier:
    
    def __init__(self,health, strength): # siempre que se inicie una "class" se debe iniciar con __init__
        self.health = health
        self.strength = strength
       
        
    def attack (self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.damage = damage
        self.health -= self.damage
    
# Viking


class Viking:
    
    def __init__(self,name,health,strength):
        
        Soldier.__init__(self, health, strength)
        self.name=name
    
    def attack (self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.damage = damage
        self.health -= self.damage
        
        if self.health>0: return f"{self.name} has received {self.damage} points of damage"
                                      
        else: return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return 'Odin Owns You All!'
        
    

#Saxon

class Saxon:
    
    def __init__(self,health,strength):
        
        Soldier.__init__(self, health, strength)
    
    def attack (self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.damage = damage
        self.health -= self.damage
        
        if self.health>0: return f"A Saxon has received {self.damage} points of damage"
                                       
        else: return 'A Saxon has died in combat'   

# War


class War:
    
    def __init__(self):
         
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking):
           self.vikingArmy.append(viking)
    
    
    def addSaxon(self, saxon):
           self.saxonArmy.append(saxon)
  
    
    
    def vikingAttack(self):
        
           if receiveDamage == strength
    
    
    
    
    def saxonAttack(self):

        
        
        
    def showStatus(self):
          
        
        
        
    
