class Character:
    #implement levels later.

    def __init__(self, curr_health):
        curr_health = Character.health

        #for debugging purposes
    def __init__(self, health, damage, armor, mr, atk_spd, mv_spd, mana, range):
        self.health = health
        self.armor = armor
        self.mr = mr
        self.atk_spd = atk_spd
        self.mv_spd = mv_spd
        self.mana = mana
        self.range = range

    def attack(self, opponent):
        """ The fundamental gameplay operation. Assumed in range."""
        while opponent.health > 0:
            opponent.curr_health -= 3
        return 0

    def calculate_damage():
        return 0

    def cast_ult(self):
        print("this should not be printing. Cast Ult on your champion.")




class Garen(Character):
    name = "Garen"
    health = 100
    damage = 10
    armor = 10
    mr = 10
    atk_spd = .5 # will depend on frames and shit
    mv_spd = .75  # will depend on pixels and shit
    mana = 0
    range = 125

    def __init__(self):
        super().__init__(self, curr_health)

    # prob just for testing, making a unique garen for testing gameplay functionality.
    def __init__(self, health, damage, armor, mr, atk_spd, mv_spd, mana):
        super().__init__(self, health, damage, armor, mr, atk_spd, mv_spd, mana)

    def attack(self, opponent):
        """ The fundamental gameplay operation. Assumed in range."""
        return 0

    def castUlt(self):
        """ not sure how to specify if aoe versus against certain targets... etc"""
        return 0




class Minion(Character):
    name = "Minion"
    
    def __init__(self):
        super().__init__(self, curr_health)

    def __init__(self, health, damage, armor, mr, atk_spd, mv_spd, mana):
        super().__init__(self, health, damage, armor, mr, atk_spd, mv_spd, mana)

    def attack(self, opponent):
        """ The fundamental gameplay operation. Assumed in range."""
        return 0

    def castUlt(self):
        """ not sure how to specify if aoe versus against certain targets... etc"""
        return 0
