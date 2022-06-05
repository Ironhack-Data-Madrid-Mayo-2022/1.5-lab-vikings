'''
nota
Kike: !!! No me sale y NO sé por qué. No lo sé. Creo que voy a borrar todo y a hacer un archivo nuevo entregable. **cries in python

'''


# Soldier


class Soldier: #Aquí se define el objeto tipo soldado. características comunes
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

#Abajo son cosas que los soldado pueden hacer. Acciones
#attack
    def attack(self):
        return self.strength
#damage
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
         
    

# Viking

'''
class Viking(Soldier): #El vikingo es un tipo de soldado, comparte. Hija
    def __init__(self, name, health, strength): #constructor
        Soldier().__init__(health, strenght)
        self.name = name
            
            
    def receiveDamage(self, damage): #metodo

        self.health -= self.health -damage
            
        if self.health > 0: 
            return f"{self.name}, 'has received', {self.damage}, 'points of damage'"
            
        else: 
            return f"{self.name}, 'has has died in combat'"
        
    def battleCry(self): #metodo
            return 'Odin Owns You All!'
#El viernes me daba mal por la puta IDENTACIÓN. No desesperarr
'''
class Viking(Soldier):

    def name(self):
        self.name= ""
        
    def receiveDamage(self, damage): #metodo. Acciones que hacen los Kiking
        self.health -= damage
            
        if self.health > 0: 
            return f'{self.name}, has received {self.damage} points of damage'
            
        else: 
            return f"{self.name}, 'has has died in combat'"
        
    def battleCry(self): #metodo
            return 'Odin Owns You All!'


# Saxon


class Saxon(Soldier):
        
    def receiveDamage(self,damage):
        self.damage=damage
        self.health=self.health - damage
        
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return 'A Saxon has died in combat'

# War


class War:
    pass
