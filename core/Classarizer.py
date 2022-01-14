import random
from utils.Abilities import Abilities
from utils.CharClass import CharClass

class CharUtils:

    @staticmethod
    def setAbilities(character, str, dex, con, int, wis, cha):
        character.strength = str
        character.dexterity = dex
        character.constitution = con
        character.intelligence = int
        character.wisdom = wis
        character.charisma = cha

    @staticmethod
    def randomiseAbilities():
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

    @staticmethod
    def assignClassAbilities(character):
        scores = CharUtils.randomiseAbilities()

        if character.charClass==CharClass.artificer:
            character.intelligence = scores[0]
            del scores[0]
            character.saves.append(Abilities.constitution)
            character.saves.append(Abilities.intelligence)
            pass
        elif character.charClass==CharClass.barbarian:
            character.strength = scores[0]
            del scores[0]
            character.saves.append(Abilities.strength)
            character.saves.append(Abilities.constitution)
            pass
        elif character.charClass==CharClass.bard:
            character.charisma = scores[0]
            del scores[0]
            character.saves.append(Abilities.dexterity)
            character.saves.append(Abilities.charisma)
            pass
        elif character.charClass==CharClass.blood_hunter:
            character.strength = scores[0]
            character.dexterity = scores[1]
            character.intelligence = scores[2]
            del scores[2]
            del scores[1]
            del scores[0]
            character.saves.append(Abilities.dexterity)
            character.saves.append(Abilities.intelligence)
            pass
        elif character.charClass==CharClass.cleric:
            character.wisdom = scores[0]
            del scores[0]
            character.saves.append(Abilities.wisdom)
            character.saves.append(Abilities.charisma)
            pass
        elif character.charClass==CharClass.druid:
            character.wisdom = scores[0]
            del scores[0]
            character.saves.append(Abilities.intelligence)
            character.saves.append(Abilities.wisdom)
            pass
        elif character.charClass==CharClass.fighter:
            character.strength = scores[0]
            character.dexterity = scores[1]
            del scores[1]
            del scores[0]
            character.saves.append(Abilities.strength)
            character.saves.append(Abilities.constitution)
            pass
        elif character.charClass==CharClass.monk:
            character.dexterity = scores[0]
            character.wisdom = scores[1]
            del scores[1]
            del scores[0]
            character.saves.append(Abilities.strength)
            character.saves.append(Abilities.dexterity)
            pass
        elif character.charClass==CharClass.paladin:
            character.strength = scores[0]
            character.charisma = scores[1]
            del scores[1]
            del scores[0]
            character.saves.append(Abilities.wisdom)
            character.saves.append(Abilities.charisma)
            pass
        elif character.charClass==CharClass.ranger:
            character.dexterity = scores[0]
            character.wisdom = scores[1]
            del scores[1]
            del scores[0]
            character.saves.append(Abilities.strength)
            character.saves.append(Abilities.dexterity)
            pass
        elif character.charClass==CharClass.rogue:
            character.dexterity = scores[0]
            del scores[0]
            character.saves.append(Abilities.dexterity)
            character.saves.append(Abilities.intelligence)
            pass
        elif character.charClass==CharClass.sorcerer:
            character.charisma = scores[0]
            del scores[0]
            character.saves.append(Abilities.constitution)
            character.saves.append(Abilities.charisma)
            pass
        elif character.charClass==CharClass.warlock:
            character.charisma = scores[0]
            del scores[0]
            character.saves.append(Abilities.wisdom)
            character.saves.append(Abilities.charisma)
            pass
        elif character.charClass==CharClass.wizard:
            character.int = scores[0]
            del scores[0]
            character.saves.append(Abilities.intelligence)
            character.saves.append(Abilities.wisdom)
            pass
        else:
            # throw error
            pass

        # shuffle and assign remaining scores
        random.shuffle(scores)
        if character.strength == 0:
            character.strength = scores[0]
            del scores[0]
        if character.dexterity == 0:
            character.dexterity = scores[0]
            del scores[0]
        if character.constitution == 0:
            character.constitution = scores[0]
            del scores[0]
        if character.intelligence == 0:
            character.intelligence = scores[0]
            del scores[0]
        if character.wisdom == 0:
            character.wisdom = scores[0]
            del scores[0]
        if character.charisma == 0:
            character.charisma = scores[0]
            del scores[0]

    @staticmethod
    def assignClassAbilitiesRandomly(character, scores):
        random.shuffle(scores)
        character.strength = scores[0]
        character.dexterity = scores[1]
        character.constitution = scores[2]
        character.intelligence = scores[3]
        character.wisdom = scores[4]
        character.charisma = scores[5]