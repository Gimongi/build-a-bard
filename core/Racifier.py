from core.Character import Character
from data.CharRace import CharRace
from data.CharSubRace import CharSubRace


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
            character.strength += 1
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



    # Applies subrace to character
    @staticmethod
    def applySubRaceToCharacter(character):
        # type: (Character) -> None
        if character.charSubRace == CharSubRace.aarakocra_eagle:
            pass
        elif character.charSubRace == CharSubRace.aarakocra_macaw:
            pass
        elif character.charSubRace == CharSubRace.aarakocra_owl:
            pass
        elif character.charSubRace == CharSubRace.aarakocra_potoo:
            pass
        elif character.charSubRace == CharSubRace.aarakocra_finch:
            pass
        elif character.charSubRace == CharSubRace.aarakocra_raven:
            pass
        elif character.charSubRace == CharSubRace.aarakocra_albatross:
            pass
        elif character.charSubRace == CharSubRace.aarakocra_chicken:
            pass
        elif character.charSubRace == CharSubRace.aarakocra_penguin:
            pass
        elif character.charSubRace == CharSubRace.aarakocra_ostrich:
            pass

        elif character.charSubRace == CharSubRace.aasimar_protector:
            pass
        elif character.charSubRace == CharSubRace.aasimar_scourge:
            pass
        elif character.charSubRace == CharSubRace.aasimar_fallen:
            pass

        elif character.charSubRace == CharSubRace.dragonborn_chromatic:
            pass
        elif character.charSubRace == CharSubRace.dragonborn_gem:
            pass
        elif character.charSubRace == CharSubRace.dragonborn_metallic:
            pass

        elif character.charSubRace == CharSubRace.dwarf_hill:
            pass
        elif character.charSubRace == CharSubRace.dwarf_mountain:
            pass
        elif character.charSubRace == CharSubRace.dwarf_grey:
            pass

        elif character.charSubRace == CharSubRace.elf_high:
            pass
        elif character.charSubRace == CharSubRace.elf_wood:
            pass

        elif character.charSubRace == CharSubRace.genasi_air:
            pass
        elif character.charSubRace == CharSubRace.genasi_earth:
            pass
        elif character.charSubRace == CharSubRace.genasi_fire:
            pass
        elif character.charSubRace == CharSubRace.genasi_water:
            pass

        elif character.charSubRace == CharSubRace.githyanki:
            pass
        elif character.charSubRace == CharSubRace.githzerai:
            pass

        elif character.charSubRace == CharSubRace.gnome_deep:
            pass
        elif character.charSubRace == CharSubRace.gnome_forest:
            pass
        elif character.charSubRace == CharSubRace.gnome_rock:
            pass

        elif character.charSubRace == CharSubRace.goblin_greenskin:
            pass
        elif character.charSubRace == CharSubRace.goblin_boggart:
            pass
        elif character.charSubRace == CharSubRace.goblin_gremlin:
            pass

        elif character.charSubRace == CharSubRace.halfling_lightfoot:
            pass
        elif character.charSubRace == CharSubRace.halfling_stout:
            pass

        elif character.charSubRace == CharSubRace.kobold_burrows:
            pass
        elif character.charSubRace == CharSubRace.kobold_loredrake:
            pass

        elif character.charSubRace == CharSubRace.leonin_royal:
            pass
        elif character.charSubRace == CharSubRace.leonin_wild:
            pass
        elif character.charSubRace == CharSubRace.leonin_grey:
            pass

        elif character.charSubRace == CharSubRace.loxodon_ravnica:
            pass
        elif character.charSubRace == CharSubRace.loxodon_mirrodin:
            pass
        elif character.charSubRace == CharSubRace.loxodon_tarkir:
            pass

        elif character.charSubRace == CharSubRace.orc_common:
            pass
        elif character.charSubRace == CharSubRace.orc_grey:
            pass
        elif character.charSubRace == CharSubRace.orc_blue:
            pass
        elif character.charSubRace == CharSubRace.orc_purple:
            pass

        elif character.charSubRace == CharSubRace.shifter_beasthide:
            pass
        elif character.charSubRace == CharSubRace.shifter_longtooth:
            pass
        elif character.charSubRace == CharSubRace.shifter_swiftstride:
            pass
        elif character.charSubRace == CharSubRace.shifter_wildhunt:
            pass
        elif character.charSubRace == CharSubRace.shifter_cliffwalk:
            pass
        elif character.charSubRace == CharSubRace.shifter_razorclaw:
            pass

        elif character.charSubRace == CharSubRace.tabaxi_mountain:
            pass
        elif character.charSubRace == CharSubRace.tabaxi_grassland:
            pass
        elif character.charSubRace == CharSubRace.tabaxi_jungle:
            pass
        elif character.charSubRace == CharSubRace.tabaxi_forest:
            pass

        elif character.charSubRace == CharSubRace.tiefling_asmodeus:
            pass
        elif character.charSubRace == CharSubRace.tiefling_baalzebul:
            pass
        elif character.charSubRace == CharSubRace.tiefling_dispater:
            pass
        elif character.charSubRace == CharSubRace.tiefling_fierna:
            pass
        elif character.charSubRace == CharSubRace.tiefling_glasya:
            pass
        elif character.charSubRace == CharSubRace.tiefling_levistus:
            pass
        elif character.charSubRace == CharSubRace.tiefling_mammon:
            pass
        elif character.charSubRace == CharSubRace.tiefling_mephistopheles:
            pass
        elif character.charSubRace == CharSubRace.tiefling_zarial:
            pass
        elif character.charSubRace == CharSubRace.tiefling_abyssal:
            pass

        elif character.charSubRace == CharSubRace.tortle_razorback:
            pass
        elif character.charSubRace == CharSubRace.tortle_softshell:
            pass
        elif character.charSubRace == CharSubRace.tortle_desert:
            pass
        
        else:
            raise NotImplementedError


    # TODO: description should be of the character (colour/etc.)? or of the race itcharacter. Not sure. Probably of character
    # character.description = 