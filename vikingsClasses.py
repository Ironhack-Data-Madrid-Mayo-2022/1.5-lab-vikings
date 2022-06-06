
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
        
    def attack(self):
        
        return self.strength
        
    def receiveDamage(self, damage):
        
        self.damage = damage
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        
        super(Viking, self).__init__(health, strength)
        self.name = name  
        
    def receiveDamage(self, damage):
        
        self.damage = damage
        self.health = self.health - damage
        
        if self.health > 0: 
            
            return f"{self.name} has received {self.damage} points of damage"
        
        else: 
            
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        
        return "Odin Owns You All!"
        
        
        

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        
        super(Saxon, self).__init__(health,strength)
        
    def receiveDamage(self, damage):
        
        self.damage = damage
        self.health = self.health - damage
        
        if self.health > 0:
            
            return f"A Saxon has received {self.damage} points of damage"
        
        else:
            
            return "A Saxon has died in combat"

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
        
        vikingSoldier = random.choice(self.vikingArmy)
        saxonSoldier = random.choice(self.saxonArmy)
        
        vikingSoldierAttack = saxonSoldier.receiveDamage(vikingSoldier.attack())
        
        if saxonSoldier.health < 1:
            self.saxonArmy.remove(saxonSoldier)
            
        return vikingSoldierAttack
    
    
    def saxonAttack(self):
    
        vikingSoldier = random.choice(self.vikingArmy)
        saxonSoldier = random.choice(self.saxonArmy)
        
        saxonSoldierAttack = vikingSoldier.receiveDamage(saxonSoldier.attack())
        
        if vikingSoldier.health < 1:
            self.vikingArmy.remove(vikingSoldier)
            
        return saxonSoldierAttack
        
    
    def showStatus(self):
        
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
    
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        
        else:
            return "Vikings and Saxons are still in the thick of battle."
    
