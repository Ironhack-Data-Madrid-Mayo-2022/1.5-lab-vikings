
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    
    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.damage=damage
        self.health=self.health-damage
        return
            

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name=name
    
    def receiveDamage(self, damage):
        self.health=self.health-damage
        
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
    
    def receiveDamage(self, damage):
        self.health=self.health-damage
        
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
# War


class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
        
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
        return
        
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
        return

        

