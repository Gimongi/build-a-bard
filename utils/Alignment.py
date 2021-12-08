import enum

class Alignment(str, enum.Enum):
    lawful_good = "lawful good"
    neutral_good = "neutral good"
    chaotic_good = "chaotic good"
    lawful_neutral = "lawful neutral"
    neutral = "neutral"
    chaotic_neutral = "chaotic neutral"
    lawful_evil = "lawful evil"
    neutral_evil = "neutral evil"
    chaotic_evil = "chaotic evil"

    # @staticmethod
    # def fromStr(charClass):
    #     if charClass == "artificer":
    #         return CharClass.artificer
    #     elif charClass == "barbarian":
    #         return CharClass.barbarian
    #     elif charClass == "bard":
    #         return CharClass.bard
    #     elif charClass == "blood hunter":
    #         return CharClass.blood_hunter
    #     elif charClass == "cleric":
    #         return CharClass.cleric
    #     elif charClass == "druid":
    #         return CharClass.druid
    #     elif charClass == "fighter":
    #         return CharClass.fighter
    #     elif charClass == "monk":
    #         return CharClass.monk
    #     elif charClass == "paladin":
    #         return CharClass.paladin
    #     elif charClass == "ranger":
    #         return CharClass.ranger
    #     elif charClass == "rogue":
    #         return CharClass.rogue
    #     elif charClass == "sorcerer":
    #         return CharClass.sorcerer
    #     elif charClass == "warlock":
    #         return CharClass.warlock
    #     elif charClass == "wizard":
    #         return CharClass.wizard
    #     else:
    #         raise NotImplementedError

        