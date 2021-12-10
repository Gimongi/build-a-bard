from templates.CharacterAbilities import CharacterAbilities
from utils.Abilities import Abilities
from utils.Alignment import Alignment
from utils.CharClass import CharClass
from utils.CharRace import CharRace
from utils.Utils import Utils


class Character:
    level = 0
    health = 0
    hitDie = 0
    # age = 0
    speed = 0
    languages = []

    features = []
    spells = []
    
    description = ""

    def __init__(self, charClass, charRace, level, tags):
        self.charClass = CharClass.fromStr(charClass)
        self.charRace = CharRace.fromStr(charRace)
        self.level = level

        self.abilities = CharacterAbilities(charClass, charRace, tags)
        self.initialiseChar()

    def initialiseChar(self):
        self.hitDie = self.abilities.hitDie
        self.health = self.hitDie + Utils.getModifier(self.abilities.constitution)
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


    def applyRaceToCharacter(self):
        if self.charRace == CharRace.aarakocra:
            self.abilities.dexterity += 2
            self.abilities.wisdom += 1

            self.speed = 25
            self.alignment = Alignment.neutral_good

            self.languages.append("Common")
            self.languages.append("Aarakocra")
            self.languages.append("Auran")

            # TODO: description should be of the character (colour/etc.)? or of the race itself. Not sure. Probably of character
            # self.description = 
            pass
        elif self.charRace == CharRace.aasimar:
            pass
        elif self.charRace == CharRace.bugbear:
            pass
        elif self.charRace == CharRace.centaur:
            pass
        elif self.charRace == CharRace.changeling:
            pass
        elif self.charRace == CharRace.dragonborn:
            pass
        elif self.charRace == CharRace.dwarf:
            pass
        elif self.charRace == CharRace.elf:
            pass
        elif self.charRace == CharRace.fairy:
            pass
        elif self.charRace == CharRace.firbolg:
            pass
        elif self.charRace == CharRace.genasi:
            pass
        elif self.charRace == CharRace.gith:
            pass
        elif self.charRace == CharRace.gnome:
            pass
        elif self.charRace == CharRace.goblin:
            pass
        elif self.charRace == CharRace.goliath:
            pass
        elif self.charRace == CharRace.grung:
            pass
        elif self.charRace == CharRace.half_elf:
            pass
        elif self.charRace == CharRace.halfling:
            pass
        elif self.charRace == CharRace.half_orc:
            pass
        elif self.charRace == CharRace.harengon:
            pass
        elif self.charRace == CharRace.hobgoblin:
            pass
        elif self.charRace == CharRace.human:
            pass
        elif self.charRace == CharRace.kalashtar:
            pass
        elif self.charRace == CharRace.kenku:
            pass
        elif self.charRace == CharRace.kobold:
            pass
        elif self.charRace == CharRace.leonin:
            pass
        elif self.charRace == CharRace.lizardfolk:
            pass
        elif self.charRace == CharRace.locathah:
            pass
        elif self.charRace == CharRace.loxodon:
            pass
        elif self.charRace == CharRace.minotaur:
            pass
        elif self.charRace == CharRace.orc:
            pass
        elif self.charRace == CharRace.owlin:
            pass
        elif self.charRace == CharRace.satyr:
            pass
        elif self.charRace == CharRace.shifter:
            pass
        elif self.charRace == CharRace.simic_hybrid:
            pass
        elif self.charRace == CharRace.tabaxi:
            pass
        elif self.charRace == CharRace.tiefling:
            pass
        elif self.charRace == CharRace.tortle:
            pass
        elif self.charRace == CharRace.triton:
            pass
        elif self.charRace == CharRace.vedalken:
            pass
        elif self.charRace == CharRace.verdan:
            pass
        elif self.charRace == CharRace.warforged:
            pass
        elif self.charRace == CharRace.yuan_ti:
            pass
        else:
            raise NotImplementedError