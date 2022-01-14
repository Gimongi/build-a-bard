import enum

class CharRace(str, enum.Enum):
    aarakocra = "aarakocra"
    aasimar = "aasimar"
    bugbear = "bugbear"
    centaur = "centaur"
    changeling = "changeling"
    dragonborn = "dragonborn"
    dwarf = "dwarf"
    elf = "elf"
    fairy = "fairy"
    firbolg = "firbolg"
    genasi = "genasi"
    gith = "gith"
    gnome = "gnome"
    goblin = "goblin"
    goliath = "goliath"
    grung = "grung"
    half_elf = "half elf"
    halfling = "halfling"
    half_orc = "half orc"
    harengon = "harengon"
    hobgoblin = "hobgoblin"
    human = "human"
    kalashtar = "kalashtar"
    kenku = "kenku"
    kobold = "kobold"
    leonin = "leonin"
    lizardfolk = "lizardfolk"
    locathah = "locathah"
    loxodon = "loxodon"
    minotaur = "minotaur"
    orc = "orc"
    owlin = "owlin"
    satyr = "satyr"
    shifter = "shifter"
    simic_hybrid = "simic hybrid"
    tabaxi = "tabaxi"
    tiefling = "tiefling"
    tortle = "tortle"
    triton = "triton"
    vedalken = "vedalken"
    verdan = "verdan"
    warforged = "warforged"
    yuan_ti = "yuan ti"
    

    @staticmethod   
    def fromStr(charRace):
        if charRace == "aarakocra":
            return CharRace.aarakocra
        elif charRace == "aasimar":
            return CharRace.aasimar
        elif charRace == "bugbear":
            return CharRace.bugbear
        elif charRace == "centaur":
            return CharRace.centaur
        elif charRace == "changeling":
            return CharRace.changeling
        elif charRace == "dragonborn":
            return CharRace.dragonborn
        elif charRace == "dwarf":
            return CharRace.dwarf
        elif charRace == "elf":
            return CharRace.elf
        elif charRace == "fairy":
            return CharRace.fairy
        elif charRace == "firbolg":
            return CharRace.firbolg
        elif charRace == "genasi":
            return CharRace.genasi
        elif charRace == "gith":
            return CharRace.gith
        elif charRace == "gnome":
            return CharRace.gnome
        elif charRace == "goblin":
            return CharRace.goblin
        elif charRace == "goliath":
            return CharRace.goliath
        elif charRace == "grung":
            return CharRace.grung
        elif charRace == "half elf":
            return CharRace.half_elf
        elif charRace == "halfling":
            return CharRace.halfling
        elif charRace == "half orc":
            return CharRace.half_orc
        elif charRace == "harengon":
            return CharRace.harengon
        elif charRace == "hobgoblin":
            return CharRace.hobgoblin
        elif charRace == "human":
            return CharRace.human
        elif charRace == "kalashtar":
            return CharRace.kalashtar
        elif charRace == "kenku":
            return CharRace.kenku
        elif charRace == "kobold":
            return CharRace.kobold
        elif charRace == "leonin":
            return CharRace.leonin
        elif charRace == "lizardfolk":
            return CharRace.lizardfolk
        elif charRace == "locathah":
            return CharRace.locathah
        elif charRace == "loxodon":
            return CharRace.loxodon
        elif charRace == "minotaur":
            return CharRace.minotaur
        elif charRace == "orc":
            return CharRace.orc
        elif charRace == "owlin":
            return CharRace.owlin
        elif charRace == "satyr":
            return CharRace.satyr
        elif charRace == "shifter":
            return CharRace.shifter
        elif charRace == "simic hybrid":
            return CharRace.simic_hybrid
        elif charRace == "tabaxi":
            return CharRace.tabaxi
        elif charRace == "tiefling":
            return CharRace.tiefling
        elif charRace == "tortle":
            return CharRace.tortle
        elif charRace == "triton":
            return CharRace.triton
        elif charRace == "vedalken":
            return CharRace.vedalken
        elif charRace == "verdan":
            return CharRace.verdan
        elif charRace == "warforged":
            return CharRace.warforged
        elif charRace == "yuan ti":
            return CharRace.yuan_ti
        else:
            return NotImplementedError