from utils.CharRace import CharRace


class Racifier:

    # def __init__(self, character):
    #     self.character = character
    #     pass

    @staticmethod
    def applyRaceToCharacter(character):
        if character.charRace == CharRace.aarakocra:
            character.abilities.dexterity += 2
            character.abilities.wisdom += 1

            character.speed = 25
            character.alignment = character.Alignment.neutral_good

            character.languages.append("Common")
            character.languages.append("Aarakocra")
            character.languages.append("Auran")
            pass
        elif character.charRace == CharRace.aasimar:
            pass
        elif character.charRace == CharRace.bugbear:
            pass
        elif character.charRace == CharRace.centaur:
            pass
        elif character.charRace == CharRace.changeling:
            pass
        elif character.charRace == CharRace.dragonborn:
            pass
        elif character.charRace == CharRace.dwarf:
            pass
        elif character.charRace == CharRace.elf:
            pass
        elif character.charRace == CharRace.fairy:
            pass
        elif character.charRace == CharRace.firbolg:
            pass
        elif character.charRace == CharRace.genasi:
            pass
        elif character.charRace == CharRace.gith:
            pass
        elif character.charRace == CharRace.gnome:
            pass
        elif character.charRace == CharRace.goblin:
            pass
        elif character.charRace == CharRace.goliath:
            pass
        elif character.charRace == CharRace.grung:
            pass
        elif character.charRace == CharRace.half_elf:
            pass
        elif character.charRace == CharRace.halfling:
            pass
        elif character.charRace == CharRace.half_orc:
            pass
        elif character.charRace == CharRace.harengon:
            pass
        elif character.charRace == CharRace.hobgoblin:
            pass
        elif character.charRace == CharRace.human:
            pass
        elif character.charRace == CharRace.kalashtar:
            pass
        elif character.charRace == CharRace.kenku:
            pass
        elif character.charRace == CharRace.kobold:
            pass
        elif character.charRace == CharRace.leonin:
            pass
        elif character.charRace == CharRace.lizardfolk:
            pass
        elif character.charRace == CharRace.locathah:
            pass
        elif character.charRace == CharRace.loxodon:
            pass
        elif character.charRace == CharRace.minotaur:
            pass
        elif character.charRace == CharRace.orc:
            pass
        elif character.charRace == CharRace.owlin:
            pass
        elif character.charRace == CharRace.satyr:
            pass
        elif character.charRace == CharRace.shifter:
            pass
        elif character.charRace == CharRace.simic_hybrid:
            pass
        elif character.charRace == CharRace.tabaxi:
            pass
        elif character.charRace == CharRace.tiefling:
            pass
        elif character.charRace == CharRace.tortle:
            pass
        elif character.charRace == CharRace.triton:
            pass
        elif character.charRace == CharRace.vedalken:
            pass
        elif character.charRace == CharRace.verdan:
            pass
        elif character.charRace == CharRace.warforged:
            pass
        elif character.charRace == CharRace.yuan_ti:
            pass
        else:
            raise NotImplementedError


    # TODO: description should be of the character (colour/etc.)? or of the race itcharacter. Not sure. Probably of character
    # character.description = 