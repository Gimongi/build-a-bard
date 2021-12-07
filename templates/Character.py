from templates.CharacterAbilities import CharacterAbilities
from utils.Abilities import Abilities
from utils.Utils import Utils


class Character:
    level = 0
    
    charClass = ""
    charRace = ""

    health = 0
    hitDie = 0

    abilities = CharacterAbilities()
    # features = CharacterFeatures()
    # spells = CharacterSpells()

    def __init__(self, charClass, charRace, level, tags):
        self.abilities = self.abilities.__init__(self, charClass, charRace, tags)
        self.assignAbilities(charClass, self.randomiseAbilities())
        self.initialiseChar()
        return self

    # def __init__(self, str, dex, con, int, wis, cha):
    #     self.strength = str
    #     self.dexterity = dex
    #     self.constitution = con
    #     self.intelligence = int
    #     self.wisdom = wis
    #     self.charisma = cha


    def initialiseChar(self):
        self.health = self.hitDie + Utils.getModifier(self.abilities.constitution)
        pass