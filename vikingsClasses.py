
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health -= damage 
        

# Viking

class Viking(Soldier):
    def __init__(self,name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return self.name + ' has received ' + str(damage) + ' points of damage'
        if self.health <= 0:
            return self.name + ' has died in act of combat'
    
    def battleCry(self):
        return "Odin Owns You All!"
    

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return 'A Saxon has received ' + str(damage) +' points of damage'
        if self.health <= 0:
            return 'A Saxon has died in combat'
    
    

# War


class War:
    def __init__(self, vikingArmy=[], saxonArmy=[]):
        self.vikingArmy = vikingArmy
        self.saxonArmy = saxonArmy
    
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)
            
        
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
            
    def vikingAttack():
        viking = self.vikingArmy[0]
        saxon = self.saxonArmy[0]
        vikingBattle = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0: 
            self.saxonArmy.pop(0)
        return vikingBattle
    
    
    def vikingAttack():
        viking = self.vikingArmy[0]
        saxon = self.saxonArmy[0]
        saxonBattle = viking.receiveDamage(saxon.strength)
        if viking.health <= 0: 
            self.vikingArmy.pop(0)
        return saxonBattle
        
    def showStatus():
        if len(self.saxonArmy) <= 0:
            return "Vikings have won the war of the century"
        elif len(self.vikingArmy) <= 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.vikingArmy)>0 and len(self.vikingArmy)>0:
            return "Vikings and Saxons are still in the thick of battle."
            
            
