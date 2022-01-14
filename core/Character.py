from data.CharClass import CharClass
from data.CharRace import CharRace
from data.CharSubRace import CharSubRace


class Character:
    name = ""
    charRace = CharRace
    charSubRace = CharSubRace
    charClass = CharClass

    level = 0

    health = 0
    hitDie = 0
    
    armorClass = 0
    initiative = 0
    speed = 0

    strength = 0
    dexterity = 0
    constitution = 0
    intelligence = 0
    wisdom = 0
    charisma = 0

    alignment = ""

    saves = []

    age = 0
    languages = []

    weapons = []
    skills = []
    features = []
    spells = []
    
    description = ""

    def __init__(self, charRace, charClass, level, tags):
        self.charRace = CharRace.fromStr(charRace)
        self.charClass = CharClass.fromStr(charClass)
        self.level = level
        
        self.initialiseChar()

    def initialiseChar(self):
        # self.hitDie = self.abilities.hitDie
        # self.health = self.hitDie + Utils.getModifier(self.abilities.constitution)
        self.applyRaceToCharacter()


    def levelUpChar(self):
        # call all the leveling up methods in abilities, features, spells
        pass

    
    def characterInfo(self):
        print("Hi I am a " + self.charRace + " " + self.charClass + ". I am level " + str(self.level))
        print("My abilities are: ")
        print("Str: " + str(self.abilities.strength))
        print("Dex: " + str(self.abilities.dexterity))
        print("Con: " + str(self.abilities.constitution))
        print("Int: " + str(self.abilities.intelligence))
        print("Wis: " + str(self.abilities.wisdom))
        print("Cha: " + str(self.abilities.charisma))
        print("My health is currently " + str(self.health) + ", and my hit die is ") + str(self.hitDie)
        print("My saving throws are: " + str(self.abilities.saves))