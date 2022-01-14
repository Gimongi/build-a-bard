import enum

class CharClass(str, enum.Enum):
    artificer = "artificer"
    barbarian = "barbarian"
    bard = "bard"
    blood_hunter = "blood hunter"
    cleric = "cleric"
    druid = "druid"
    fighter = "fighter"
    monk = "monk"
    paladin = "paladin"
    ranger = "ranger"
    rogue = "rogue"
    sorcerer = "sorcerer"
    warlock = "warlock"
    wizard = "wizard"

    @staticmethod
    def fromStr(charClass):
        if charClass == "artificer":
            return CharClass.artificer
        elif charClass == "barbarian":
            return CharClass.barbarian
        elif charClass == "bard":
            return CharClass.bard
        elif charClass == "blood hunter":
            return CharClass.blood_hunter
        elif charClass == "cleric":
            return CharClass.cleric
        elif charClass == "druid":
            return CharClass.druid
        elif charClass == "fighter":
            return CharClass.fighter
        elif charClass == "monk":
            return CharClass.monk
        elif charClass == "paladin":
            return CharClass.paladin
        elif charClass == "ranger":
            return CharClass.ranger
        elif charClass == "rogue":
            return CharClass.rogue
        elif charClass == "sorcerer":
            return CharClass.sorcerer
        elif charClass == "warlock":
            return CharClass.warlock
        elif charClass == "wizard":
            return CharClass.wizard
        else:
            return NotImplementedError

        