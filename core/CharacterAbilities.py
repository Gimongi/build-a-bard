import enum, random
from utils.Abilities import Abilities
from utils.CharClass import CharClass
from utils.Utils import Utils


class CharacterAbilities:
    # strength = 0
    # dexterity = 0
    # constitution = 0
    # intelligence = 0
    # wisdom = 0
    # charisma = 0

    hitDie = 0

    saves = []

    def __init__(self, charClass, charRace, tags):
        self.assignClassAbilities(charClass, charRace, self.randomiseAbilities())

    @staticmethod
    def setAbilities(char, str, dex, con, int, wis, cha):
        char.strength = str
        self.dexterity = dex
        self.constitution = con
        self.intelligence = int
        self.wisdom = wis
        self.charisma = cha

    def randomiseAbilities(self):
        scores = []
        for x in range(6):
            current = []
            for y in range(4):
                current.append(random.randint(1, 6))
            current.sort(reverse=True)
            del current[-1]
            scores.append(sum(current))
        scores.sort(reverse=True)
        return scores

    def assignClassAbilities(self, charClass, charRace, scores):
        if charClass==CharClass.artificer:
            self.hitDie = 8
            self.intelligence = scores[0]
            del scores[0]
            self.saves.append(Abilities.constitution)
            self.saves.append(Abilities.intelligence)
            pass
        elif charClass==CharClass.barbarian:
            self.hitDie = 12
            self.strength = scores[0]
            del scores[0]
            self.saves.append(Abilities.strength)
            self.saves.append(Abilities.constitution)
            pass
        elif charClass==CharClass.bard:
            self.hitDie = 8
            self.charisma = scores[0]
            del scores[0]
            self.saves.append(Abilities.dexterity)
            self.saves.append(Abilities.charisma)
            pass
        elif charClass==CharClass.blood_hunter:
            self.hitDie = 10
            self.strength = scores[0]
            self.dexterity = scores[1]
            self.intelligence = scores[2]
            del scores[2]
            del scores[1]
            del scores[0]
            self.saves.append(Abilities.dexterity)
            self.saves.append(Abilities.intelligence)
            pass
        elif charClass==CharClass.cleric:
            self.hitDie = 8
            self.wisdom = scores[0]
            del scores[0]
            self.saves.append(Abilities.wisdom)
            self.saves.append(Abilities.charisma)
            pass
        elif charClass==CharClass.druid:
            self.hitDie = 8
            self.wisdom = scores[0]
            del scores[0]
            self.saves.append(Abilities.intelligence)
            self.saves.append(Abilities.wisdom)
            pass
        elif charClass==CharClass.fighter:
            self.hitDie = 10
            self.strength = scores[0]
            self.dexterity = scores[1]
            del scores[1]
            del scores[0]
            self.saves.append(Abilities.strength)
            self.saves.append(Abilities.constitution)
            pass
        elif charClass==CharClass.monk:
            self.hitDie = 8
            self.dexterity = scores[0]
            self.wisdom = scores[1]
            del scores[1]
            del scores[0]
            self.saves.append(Abilities.strength)
            self.saves.append(Abilities.dexterity)
            pass
        elif charClass==CharClass.paladin:
            self.hitDie = 10
            self.strength = scores[0]
            self.charisma = scores[1]
            del scores[1]
            del scores[0]
            self.saves.append(Abilities.wisdom)
            self.saves.append(Abilities.charisma)
            pass
        elif charClass==CharClass.ranger:
            self.hitDie = 10
            self.dexterity = scores[0]
            self.wisdom = scores[1]
            del scores[1]
            del scores[0]
            self.saves.append(Abilities.strength)
            self.saves.append(Abilities.dexterity)
            pass
        elif charClass==CharClass.rogue:
            self.hitDie = 8
            self.dexterity = scores[0]
            del scores[0]
            self.saves.append(Abilities.dexterity)
            self.saves.append(Abilities.intelligence)
            pass
        elif charClass==CharClass.sorcerer:
            self.hitDie = 6
            self.charisma = scores[0]
            del scores[0]
            self.saves.append(Abilities.constitution)
            self.saves.append(Abilities.charisma)
            pass
        elif charClass==CharClass.warlock:
            self.hitDie = 8
            self.charisma = scores[0]
            del scores[0]
            self.saves.append(Abilities.wisdom)
            self.saves.append(Abilities.charisma)
            pass
        elif charClass==CharClass.wizard:
            self.hitDie = 6
            self.int = scores[0]
            del scores[0]
            self.saves.append(Abilities.intelligence)
            self.saves.append(Abilities.wisdom)
            pass
        else:
            # throw error
            pass

        # shuffle and assign remaining scores
        random.shuffle(scores)
        if self.strength == 0:
            self.strength = scores[0]
            del scores[0]
        if self.dexterity == 0:
            self.dexterity = scores[0]
            del scores[0]
        if self.constitution == 0:
            self.constitution = scores[0]
            del scores[0]
        if self.intelligence == 0:
            self.intelligence = scores[0]
            del scores[0]
        if self.wisdom == 0:
            self.wisdom = scores[0]
            del scores[0]
        if self.charisma == 0:
            self.charisma = scores[0]
            del scores[0]

    def assignClassAbilitiesRandomly(self, scores):
        random.shuffle(scores)
        self.strength = scores[0]
        self.dexterity = scores[1]
        self.constitution = scores[2]
        self.intelligence = scores[3]
        self.wisdom = scores[4]
        self.charisma = scores[5]