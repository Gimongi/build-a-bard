from core.Character import Character
from data.CharRace import CharRace


class Racifier:

    # def __init__(self, character):
    #     self.character = character
    #     pass

    @staticmethod
    def applyRaceToCharacter(character):
        # type: (Character) -> None
        if character.charRace == CharRace.aarakocra:
            character.dexterity += 2
            character.wisdom += 1

            character.speed = 25

            character.languages.append("Common")
            character.languages.append("Aarakocra")
            character.languages.append("Auran")
            pass
        elif character.charRace == CharRace.aasimar:
            character.charisma += 2

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Celestial")
            pass
        elif character.charRace == CharRace.bugbear:
            character.strength += 2
            character.dexterity += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Goblin")
            pass
        elif character.charRace == CharRace.centaur:
            character.strength += 2
            character.wisdom += 1

            character.speed = 40

            character.languages.append("Common")
            character.languages.append("Sylvan")
            pass
        elif character.charRace == CharRace.changeling:
            character.charisma += 2
            # TODO: 1 other ability score

            character.speed = 30

            character.languages.append("Common")
            # TODO: 2 other languages
            pass
        elif character.charRace == CharRace.dragonborn:
            character.strength += 2
            character.charisma += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Draconic")
            pass
        elif character.charRace == CharRace.dwarf:
            character.constitution += 2

            character.speed = 25

            character.languages.append("Common")
            character.languages.append("Dwarvish")
            pass
        elif character.charRace == CharRace.elf:
            character.dexterity += 2

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Elvish")
            pass
        elif character.charRace == CharRace.fairy:
            # TODO increase one ability by 2
            # TODO 1 other ability score

            character.speed = 30

            character.languages.append("Common")
            # TODO 1 other language
            pass
        elif character.charRace == CharRace.firbolg:
            character.wisdom += 2
            character.strength += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Giant")
            character.languages.append("Elvish")
            pass
        elif character.charRace == CharRace.genasi:
            character.constitution += 2

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Primordial")
            pass
        elif character.charRace == CharRace.gith:
            character.intelligence += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Gith")
            pass
        elif character.charRace == CharRace.gnome:
            character.intelligence += 2

            character.speed = 25

            character.languages.append("Common")
            character.languages.append("Gnomish")
            pass
        elif character.charRace == CharRace.goblin:
            character.dexterity += 2

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Goblin")
            pass
        elif character.charRace == CharRace.goliath:
            character.strength += 2
            character.constitution += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Giant")
            pass
        elif character.charRace == CharRace.grung:
            character.dexterity += 2
            character.constitution += 1

            character.speed = 25

            character.languages.append("Common")
            character.languages.append("Grung")
            pass
        elif character.charRace == CharRace.half_elf:
            character.charisma += 2
            #TODO 2 other ability scores increased by 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Elvish")
            #TODO 1 other language of your choice
            pass
        elif character.charRace == CharRace.halfling:
            character.strength += 2
            character.constitution += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Orc")
            pass
        elif character.charRace == CharRace.half_orc:
            character.intelligence += 2

            character.speed = 25

            character.languages.append("Common")
            character.languages.append("Gnomish")
            pass
        elif character.charRace == CharRace.harengon:
            # TODO increase one score by 2
            # TODO increase another score by

            character.speed = 30

            character.languages.append("Common")
            # TODO 1 other language
            pass
        elif character.charRace == CharRace.hobgoblin:
            character.strength += 1
            character.constitution += 1
            character.intelligence += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Goblin")
            pass
        elif character.charRace == CharRace.human:
            character.strength += 1
            character.dexterity += 1
            character.constitution += 1
            character.intelligence += 1
            character.wisdom += 1
            character.charisma += 1

            character.speed = 30

            character.languages.append("Common")
            #TODO 1 other language of your choice
            pass
        elif character.charRace == CharRace.kalashtar:
            character.wisdom += 1
            character.charisma += 1
            # TODO increase one score by 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Quori")
            # TODO 1 other language
            pass
        elif character.charRace == CharRace.kenku:
            character.dexterity += 2
            character.wisdom += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Auran")
            pass
        elif character.charRace == CharRace.kobold:
            character.dexterity += 2

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Draconic")
            pass
        elif character.charRace == CharRace.leonin:
            character.constitution += 2
            character.strength += 1

            character.speed = 35

            character.languages.append("Common")
            character.languages.append("Leonin")
            pass
        elif character.charRace == CharRace.lizardfolk:
            character.constitution += 2
            character.strength += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Draconic")
            pass
        elif character.charRace == CharRace.locathah:
            character.strength += 2
            character.dexterity += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Aquan")
            pass
        elif character.charRace == CharRace.loxodon:
            character.constitution += 1
            character.wisdom += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Loxodon")
            pass
        elif character.charRace == CharRace.minotaur:
            character.strength += 2
            character.constitution += 1

            character.speed = 30

            character.languages.append("Common")
            pass
        elif character.charRace == CharRace.orc:
            character.strength += 2

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Orc")
            pass
        elif character.charRace == CharRace.owlin:
            # TODO increase one ability by 2
            # TODO increase one ability by 1

            character.speed = 30

            character.languages.append("Common")
            # TODO 1 other language
            pass
        elif character.charRace == CharRace.satyr:
            character.charisma += 2
            character.dexterity += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Sylvan")
            pass
        elif character.charRace == CharRace.shifter:
            character.dexterity += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Quori")
            # TODO 1 other language
            pass
        elif character.charRace == CharRace.simic_hybrid:
            character.constitution += 2
            # TODO increase one ability by 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Elvish")
            character.languages.append("Vedalken")
            pass
        elif character.charRace == CharRace.tabaxi:
            character.dexterity += 2

            character.speed = 30

            character.languages.append("Common")
            # TODO 1 other language
            pass
        elif character.charRace == CharRace.tiefling:
            character.charisma += 2

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Infernal")
            pass
        elif character.charRace == CharRace.tortle:
            character.strength += 2
            character.wisdom += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Aquan")
            pass
        elif character.charRace == CharRace.triton:
            character.strength += 1
            character.constitution += 1
            character.charisma += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Aquan")
            character.languages.append("Primordial")
            pass
        elif character.charRace == CharRace.vedalken:
            character.intelligence += 2
            character.wisdom += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Vedalken")
            # TODO 1 other language
            pass
        elif character.charRace == CharRace.verdan:
            character.charisma += 2
            character.constitution += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Goblin")
            # TODO 1 other language
            pass
        elif character.charRace == CharRace.warforged:
            character.constitution += 2
            # TODO 1 other language

            character.speed = 30

            character.languages.append("Common")
            # TODO 1 other language
            pass
        elif character.charRace == CharRace.yuan_ti:
            character.charisma += 2
            character.intelligence += 1

            character.speed = 30

            character.languages.append("Common")
            character.languages.append("Abyssal")
            character.languages.append("Draconic")
            pass
        else:
            raise NotImplementedError


    # TODO: description should be of the character (colour/etc.)? or of the race itcharacter. Not sure. Probably of character
    # character.description = 