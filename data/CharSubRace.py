import enum

class CharSubRace(str, enum.Enum):
    none = "none"

    aarakocra_eagle = "eagle aarakockra"
    aarakocra_macaw = "macaw aarakockra"
    aarakocra_owl = "owl aarakockra"
    aarakocra_potoo = "potoo aarakockra"
    aarakocra_finch = "finch aarakockra"
    aarakocra_raven = "raven aarakockra"
    aarakocra_albatross = "albatross aarakockra"
    aarakocra_chicken = "chicken aarakockra"
    aarakocra_penguin = "penguin aarakockra"
    aarakocra_ostrich = "ostrich aarakockra"

    aasimar_protector = "protector aasimar"
    aasimar_scourge = "scourge aasimar"
    aasimar_fallen = "fallen aasimar"

    dragonborn_chromatic = "chromatic dragonborn"
    dragonborn_gem = "gem dragonborn"
    dragonborn_metallic = "metallic dragonborn"

    dwarf_hill = "hill dwarf"
    dwarf_mountain = "mountain dwarf"
    dwarf_grey = "grey dwarf"

    elf_high = "high elf"
    elf_wood = "wood elf"

    genasi_air = "air genasi"
    genasi_earth = "earth genasi"
    genasi_fire = "fire genasi"
    genasi_water = "water genasi"

    githyanki = "githyanki"
    githzerai = "githzerai"

    gnome_deep = "deep gnome"
    gnome_forest = "forest gnome"
    gnome_rock = "rock gnome"

    goblin_greenskin = "greenskin goblin"
    goblin_boggart = "boggart goblin"
    goblin_gremlin = "gremlin goblin"

    halfling_lightfoot = "lightfoot halfling"
    halfling_stout = "stout halfling"

    kobold_burrows = "burrows kobold"
    kobold_loredrake = "loredrake kobold"

    leonin_royal = "royal leonin"
    leonin_wild = "wild leonin"
    leonin_grey = "grey leonin"

    loxodon_ravnica = "ravnica loxodon"
    loxodon_mirrodin = "mirrodin loxodon"
    loxodon_tarkir = "tarkir loxodon"

    orc_common = "common orc"
    orc_grey = "grey orc"
    orc_blue = "blue orc"
    orc_purple = "purple orc"

    shifter_beasthide = "beasthide shifter"
    shifter_longtooth = "longtooth shifter"
    shifter_swiftstride = "swiftstride shifter"
    shifter_wildhunt = "wildhunt shifter"
    shifter_cliffwalk = "cliffwalk shifter"
    shifter_razorclaw = "razorclaw shifter"

    tabaxi_mountain = "mountain tabaxi"
    tabaxi_grassland = "grassland tabaxi"
    tabaxi_jungle = "jungle tabaxi"
    tabaxi_forest = "forest tabaxi"

    tiefling_asmodeus = "asmodeus tiefling"
    tiefling_baalzebul = "baalzebul tiefling"
    tiefling_dispater = "dispater tiefling"
    tiefling_fierna = "fierna tiefling"
    tiefling_glasya = "glasya tiefling"
    tiefling_levistus = "levistus tiefling"
    tiefling_mammon = "mammon tiefling"
    tiefling_mephistopheles = "mephistopheles tiefling"
    tiefling_zarial = "zarial tiefling"
    tiefling_abyssal = "abyssal tiefling"

    tortle_razorback = "razorback tortle"
    tortle_softshell = "softshell tortle"
    tortle_desert = "desert tortle"

    # TODO warforged has subraces but they are complex
    

    @staticmethod   
    def fromStr(subRace):
        if subRace == "nine":
            return CharSubRace.none

        elif subRace == "eagle aarakocra":
            return CharSubRace.aarakocra_eagle
        elif subRace == "macaw aarakocra":
            return CharSubRace.aarakocra_macaw
        elif subRace == "owl aarakocra":
            return CharSubRace.aarakocra_owl
        elif subRace == "potoo aarakocra":
            return CharSubRace.aarakocra_potoo
        elif subRace == "finch aarakocra":
            return CharSubRace.aarakocra_finch
        elif subRace == "raven aarakocra":
            return CharSubRace.aarakocra_raven
        elif subRace == "albatross aarakocra":
            return CharSubRace.aarakocra_albatross
        elif subRace == "chicken aarakocra":
            return CharSubRace.aarakocra_chicken
        elif subRace == "penguin aarakocra":
            return CharSubRace.aarakocra_penguin
        elif subRace == "ostrich aarakocra":
            return CharSubRace.aarakocra_ostrich

        elif subRace == "protector aasimar":
            return CharSubRace.aasimar_protector
        elif subRace == "scourge aasimar":
            return CharSubRace.aasimar_scourge
        elif subRace == "fallen aasimar":
            return CharSubRace.aasimar_fallen
            
        elif subRace == "chromatic dragonborn":
            return CharSubRace.dragonborn_chromatic
        elif subRace == "gem dragonborn":
            return CharSubRace.dragonborn_gem
        elif subRace == "metallic dragonborn":
            return CharSubRace.dragonborn_metallic


        elif subRace == "hill dwarf":
            return CharSubRace.dwarf_hill
        elif subRace == "mountain dwarf":
            return CharSubRace.dwarf_mountain
        elif subRace == "grey dwarf":
            return CharSubRace.dwarf_grey


        elif subRace == "high elf":
            return CharSubRace.elf_high
        elif subRace == "wood elf":
            return CharSubRace.elf_wood

        elif subRace == "air genasi":
            return CharSubRace.genasi_air
        elif subRace == "earth genasi":
            return CharSubRace.genasi_earth
        elif subRace == "fire genasi":
            return CharSubRace.genasi_fire
        elif subRace == "water genasi":
            return CharSubRace.genasi_water
        
        elif subRace == "githyanki":
            return CharSubRace.githyanki
        elif subRace == "githzerai":
            return CharSubRace.githzerai

        elif subRace == "deep gnome":
            return CharSubRace.gnome_deep
        elif subRace == "forest gnome":
            return CharSubRace.gnome_forest
        elif subRace == "rock gnome":
            return CharSubRace.gnome_rock

        elif subRace == "greenskin goblin":
            return CharSubRace.goblin_greenskin
        elif subRace == "boggart goblin":
            return CharSubRace.goblin_boggart
        elif subRace == "gremlin goblin":
            return CharSubRace.goblin_gremlin

        elif subRace == "lightfoot halfling":
            return CharSubRace.halfling_lightfoot
        elif subRace == "stout halfling":
            return CharSubRace.halfling_stout

        elif subRace == "burrows kobold":
            return CharSubRace.kobold_burrows
        elif subRace == "loredrake kobold":
            return CharSubRace.kobold_loredrake

        elif subRace == "royal leonin":
            return CharSubRace.leonin_royal
        elif subRace == "wild leonin":
            return CharSubRace.leonin_wild
        elif subRace == "grey leonin":
            return CharSubRace.leonin_grey

        elif subRace == "ravnica loxodon":
            return CharSubRace.loxodon_ravnica
        elif subRace == "mirrodin loxodon":
            return CharSubRace.loxodon_mirrodin
        elif subRace == "tarkir loxodon":
            return CharSubRace.loxodon_tarkir

        elif subRace == "common orc":
            return CharSubRace.orc_common
        elif subRace == "grey orc":
            return CharSubRace.orc_grey
        elif subRace == "blue orc":
            return CharSubRace.orc_blue
        elif subRace == "purple orc":
            return CharSubRace.orc_purple

        elif subRace == "beasthide shifter":
            return CharSubRace.shifter_beasthide
        elif subRace == "longtooth shifter":
            return CharSubRace.shifter_longtooth
        elif subRace == "swiftstride shifter":
            return CharSubRace.shifter_swiftstride
        elif subRace == "wildhunt shifter":
            return CharSubRace.shifter_wildhunt
        elif subRace == "cliffwalk shifter":
            return CharSubRace.shifter_cliffwalk
        elif subRace == "razorclaw shifter":
            return CharSubRace.shifter_razorclaw

        elif subRace == "mountain tabaxi":
            return CharSubRace.tabaxi_mountain
        elif subRace == "grassland tabaxi":
            return CharSubRace.tabaxi_grassland
        elif subRace == "jungle tabaxi":
            return CharSubRace.tabaxi_jungle
        elif subRace == "forest tabaxi":
            return CharSubRace.tabaxi_forest

        elif subRace == "asmodeus tiefling":
            return CharSubRace.tiefling_asmodeus
        elif subRace == "baalzebul tiefling":
            return CharSubRace.tiefling_baalzebul
        elif subRace == "dispater tiefling":
            return CharSubRace.tiefling_dispater
        elif subRace == "fierna tiefling":
            return CharSubRace.tiefling_fierna
        elif subRace == "glasya tiefling":
            return CharSubRace.tiefling_glasya
        elif subRace == "levistus tiefling":
            return CharSubRace.tiefling_levistus
        elif subRace == "mammon tiefling":
            return CharSubRace.tiefling_mammon
        elif subRace == "mephistopheles tiefling":
            return CharSubRace.tiefling_mephistopheles
        elif subRace == "zarial tiefling":
            return CharSubRace.tiefling_zarial
        elif subRace == "abyssal tiefling":
            return CharSubRace.tiefling_abyssal

        elif subRace == "razorback tortle":
            return CharSubRace.tortle_razorback
        elif subRace == "softshell tortle":
            return CharSubRace.tortle_softshell
        elif subRace == "desert tortle":
            return CharSubRace.tortle_desert

        else:
            return NotImplementedError