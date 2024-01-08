class Pokemon:
    def __init__(self,name,hp,attack1,spe,type,deck=5):
        self.name=name
        self.hp=hp
        self.type=type
        self.deck=deck
        self.attack1=attack1
        self.spe=spe
   
    def KO(self):
        if self.hp<=0:
            self.deck-=1
            return f"{self.name} est KO"
        else:
            pass
    def get_nom(self):
        return self.name
    
    def get_attack(self):
        return self.attack1
    
    def get_spe(self):
        return self.spe
    
    def get_HP(self):
        return self.hp
    
    def set_HP(self,new_hp):
        self.hp=new_hp
    
    def attack(self,damage):
        return self.hp-damage
    
    def special(self,damage):
        return self.hp-damage
    
    def deck_empty(self):
        if self.deck==0: 
            return f'Tu as perdu'
    
    def __str__(self):
        return f"┌───────────────┐\n│ {self.name.center(13)} │\n├───────────────┤\n│ Type: {self.type.ljust(7)} │\n│ PV: {str(self.hp).ljust(9)} │\n│ Attaque: {str(self.attack1).ljust(4)} │\n│ Special: {str(self.spe).ljust(4)} │\n└───────────────┘"

