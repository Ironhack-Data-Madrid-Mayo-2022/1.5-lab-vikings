
import random

class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
        
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.damage = damage
        
        self.health = self.health - self.damage
        

class Viking(Soldier):
    
    def __init__(self, name, health, strength):
       
        Soldier.__init__(self, health, strength)
        self.name = name
     
        
    def receiveDamage(self, damage):
        
        self.health = self.health - damage
        if self.health <= 0:
            return f'{self.name} has died in act of combat'
        else :
            return f'{self.name} has received {damage} points of damage'
    
    def battleCry(self):
        
        return "Odin Owns You All!"
        
    

class Saxon(Soldier):
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
    
    def receiveDamage(self, damage):
        
        self.damage = damage
        self.health = self.health - self.damage
        if self.health <= 0:
            return 'A Saxon has died in combat'
        else :
            return  f'A Saxon has received {damage} points of damage'
        
class War:
    
    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []
        
        
    def addViking(self, viking):
        
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
 
        self.saxonArmy.append(saxon)
    
    

    def vikingAttack(self):
        
       viking = random.choice(self.vikingArmy)
    
       saxon = random.choice(self.saxonArmy)
        
       attackviking = saxon.receiveDamage(viking.attack())
    
       if saxon.health <= 0 :
            
            self.saxonArmy.remove(saxon)

       return attackviking
    
    def saxonAttack(self):
        
       viking = random.choice(self.vikingArmy)
    
       saxon = random.choice(self.saxonArmy)
       
       attacksaxon = viking.receiveDamage(saxon.attack())
        
       if viking.health <= 0:
            
            self.vikingArmy.remove(saxon)
       
       return attacksaxon
    
    
    def showStatus(self):
        
        
        for viking in vikingArmy:
            
            if vikingArmy <= 0:
                
                return "Vikings have won the war of the century!"
            
            else:
                return "Vikings and Saxons are still in the thick of battle."
             
        
        
        for saxon in saxonArmy:
            
            if saxon in saxonArmy :
                
                if saxonArmy <= 0:
                    
                    return "Saxons have fought for their lives and survive another day..."
                
                else:
                    return "Vikings and Saxons are still in the thick of battle."
             
              
            
       
        
    # Me salen 6 errores pero no tengo ni idea ya de como cambiarlo, tengo el cerebro frito.
        
        
            

            

        
        
    
    
    


  