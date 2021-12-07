from templates.CharacterAbilities import CharacterAbilities
from utils.Abilities import Abilities
from utils.Utils import Utils


class Character:
    level = 0
    
    charClass = ""
    charRace = ""

    health = 0
    hitDie = 0

    # abilities = CharacterAbilities()
    # features = CharacterFeatures()
    # spells = CharacterSpells()

    def __init__(self, charClass, charRace, level, tags):
        self.charClass = charClass
        self.charRace = charRace
        self.level = level

        self.abilities = CharacterAbilities(charClass, charRace, tags)
        self.initialiseChar()

    # def __init__(self, str, dex, con, int, wis, cha):
    #     self.strength = str
    #     self.dexterity = dex
    #     self.constitution = con
    #     self.intelligence = int
    #     self.wisdom = wis
    #     self.charisma = cha


    def initialiseChar(self):
        self.charClass 
        self.hitDie = self.abilities.hitDie
        self.health = self.hitDie + Utils.getModifier(self.abilities.constitution)

    def levelUpChar(self):
        # call all the leveling up methods in abilities, features, spells
        pass

    def characterInfo(self):
        print("Hi I am a " + self.charRace + " " + str(self.charClass) + ". I am level " + str(self.level))
        print("My abilities are: ")
        print("Str: " + str(self.abilities.strength))
        print("Dex: " + str(self.abilities.dexterity))
        print("Con: " + str(self.abilities.constitution))
        print("Int: " + str(self.abilities.intelligence))
        print("Wis: " + str(self.abilities.wisdom))
        print("Cha: " + str(self.abilities.charisma))
        print("My health is currently " + str(self.health) + ", and my hit die is ") + str(self.hitDie)

